# 项目结构
 
    [vlt_web]:
        [localfile]:                        测试脚本需要的文件管理目录
        [*log]:                             脚本日志保存目录
        [*report]:                          测试报告保存目录
        [*result]:                          测试结果搜集目录
        [*screenshot]:                      失败截图目录
        [src]:
            [cases]:                        用例管理目录
                [用例目录]:                  根据需求按模块管理，推荐与pages模块的目录一一对应
                *conftest.py:               用于管理pytest的setup和teardown方法，文件名不可更改
                pytest.ini:                 pytest配置文件
            [common]:
                base_mothed.py:             用于管理selenium的基础api方法，可根据实际需求添加
                log.py:                     日志管理
                samll_tools.py:             用于管理通用的小工具方法
            [config]:
                *config.ini:                用于管理测试参数，添加参数后需要在readconfig中添加对应的读取参数方法
                                            【此文件未增减字段不建议上传gitlab，本地管理即可】
                config.py:                  用于管理项目的全局变量，暂未使用到
                readconfig.py:              用于读取config.ini的配置
            [pages]:
                [页面管理目录]:               用于保存页面的元素和页面操作方法，按模块分层管理
                base_page.py:               用于管理项目公共方法，所有页面需要继承 base_page
                admin_page.py:              登录、主页等界面，继承 base_page
        requestments:                       用于管理用到的python库
        vlt_path.py:                        用于读取项目根目录，项目所有路径均使用此方法读取根目录后拼接 

注意：

1.以*开头的文件或者目录默认不自动上传git，修改后需要手动上传

2.动手之前请先查看common/base_method.py和pages/base_page.py两个文件

# Page页面介绍
    以admin_page为例：
    
    class AdminActivity:   # 元素管理，以元祖的方式保存，支持定位方式在base_method里面的get_element_by_type定义

    username = ('xpath', '//*[starts-with(@placeholder,"请输入用户账号")]')
    display_pw = ('css', "i.iconfont.icon-mima-bukan")
    password = ('xpath', '//*[starts-with(@placeholder,"请输入用户密码")]')
    verify_code = ('xpath', '//*[starts-with(@placeholder,"请输入验证码")]')
    login_btn = ('xpath', '//div[@class="registerPwd"]//button')
    platform_name = ('css', '//div[@class="hd-logo"]//strong[@class="name"]')

    global page   # 申明全局变量:AdminActivity的实例对象


    class AdminPage(BasePage):   # 测试页面必须继承BasePage（或者BaseMethod）

        def __init__(self, driver):    
            super().__init__(driver)    # 执行base_method的init方法
            global page
            page = AdminActivity()      # 实例化AdminActivity

        def login(self, username, password):    # 写页面操作方法
            self.send_keys(page.username, username)
            self.click_element(page.display_pw)
            self.send_keys(page.password, password)
            self.send_keys(page.verify_code, '1108')
            self.click_element(page.login_btn)
            time.sleep(5)
            if self.wait_not_exist(page.logout_btn):
                raise Exception('登录失败')
                
# Case用例
    
    global over_view_page, admin_page   # 声明全局变量共全局调用，变量为需要操作的页面
    
    
    @pytest.mark.usefixtures('user_login')   # 调用conftest.py中user_login的方法
    @pytest.mark.usefixtures('init_browser')    # 调用conftest.py中init_browser返回的driver对象
    @allure.story("概况")
    class TestOverView:    # 用例类型需要以Test开头
    
        @pytest.fixture(scope='function')   #前置操作，实例化页面对象并打开菜单列表
        def set_up(self):
            """
            前置操作
            :return:
            """
            global over_view_page, admin_page
            over_view_page = OverViewPage(self.driver)
            admin_page = AdminPage(self.driver)
    
            admin_page.into_subsystem('业务管理')
    
        @pytest.fixture(autouse=True, scope='function')   # 后置操作，关闭浏览器弹窗，不受用例执行结果的影响
        def close_open_menu(self):
            """
            后置操作，关闭当前菜单
            :return:
            """
            yield 1   #  后置操作必须添加此行， yield [为真即可]
            admin_page.close_current_menu()
    
        @pytest.mark.home
        @pytest.mark.run(order=1)
        def test_check_wait_confirm(self, set_up, close_open_menu):  # 编写用例，以test开头或结尾，将前置后置函数名称以参数形式传入即可
            """
            检查待审核：
            1.点击 待审核 图标
            【check_point】当前菜单窗口标题==我的待办
            :return:
            """
            admin_page.select_menu('概况')
            over_view_page.click_wait_confirm()
            assert over_view_page.check_current_menu('我的待办'), "点击 【待审核】 未跳转至 我的待办"
            toast = over_view_page.read_toast()
            assert toast == '', '检查到错误提示信息：'+toast

# 运行环境
    python 3.6+
    slenium>=3.14.1
    pytest  【学习地址：https://www.cnblogs.com/luizyao/p/11771740.html】

# 启动参数说明
    参数格式：--cmd_env=test --cmd_browser=chrome --cmd_dr=local 
    
    --cmd_env    环境参数：对应config.ini的env字段
    
    --cmd_browser  测试浏览器参数：chrome/firefox/ie,在conftest.py里面管理
                                
    --cmd_dr     浏览器驱动参数：本地为local，集成环境为jenkins，具体参数在config.ini 文件里面配置
    
    完成命令：
    pytest src\cases\ --cmd_env=test --cmd_browser=chrome --cmd_dr=jenkins --alluredir=result

# 使用allure生成测试报告
    *使用方法：

    在启动命令行添加：--alluredir={测试数据保存目录}  本项目为：result

    *测试数据收集在./result目录

    *测试报告生成命令：
    allure generate {测试数据保存目录} -o {测试报告存放目录} --clean

    *allure其他函数说明：
    @allure.feature         # 用于描述被测试产品需求
    @allure.story           # 用于描述feature的用户场景，即测试需求
    with allure.step        # 用于描述测试步骤，将会输出到报告中
    @allure.attach          # 用于向测试报告中输入一些附加的信息，通常是一些测试数据，截图等
    @pytest.allure.step     # 用于将一些通用的函数作为测试步骤输出到报告，调用此函数的地方会向报告中输出步骤


# 测试浏览器配置说明
    如果想打开IE或者Chrome浏览器，也需要下载对应浏览器的driver.exe文件
    
    ① 在chrome 下运行脚本，需要将chromedriver.exe 放在chrome浏览器安装目录下
    
    （同时设置用户环境变量path:C:\Users\xxxxxx\AppData\Local\Google\Chrome\Application;）
    
    ② 在ie 下运行脚本，需要将IEDriverServer.exe 放在ie浏览器安装目录下
    （同时设置用户环境变量path：C:\Program Files\Internet Explorer ）,如果在调用浏览器遇到浏览器保护模式问题，可打开Ie浏览器–工具–Internet选
    项–安全–internet/本地intarnet/受信任的站点/受限制站点中的 启用保护模式全部勾选或者全部不选的勾去掉
    
    ③ 在firefox下运行脚本，直接调用（默认Python安装路径下，例如我的路径为：D:\Program Files (x86)\Python36\geckdriver.exe）

# 测试报告邮件
    jenkins新建任务使用src/common/send_email.py文件发送即可
    

    
