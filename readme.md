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
            [db]:                           数据库操作，暂未使用
            [pages]:
                [页面管理目录]:               用于保存页面的元素和页面操作方法，按模块分层管理
                base_page.py:               用于管理项目公共方法，所有页面需要继承 base_page
                admin_page.py:              登录、主页等界面，继承 base_page
        requestments:                       用于管理用到的python库
        vlt_path.py:                        用于读取项目根目录，项目所有路径均使用此方法读取根目录后拼接 

注意：*开头的文件或者目录默认不自动上传git，修改后需要手动上传

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
    
# 地址管理
    jenkin电脑：10.36.0.68
    jenkins地址：http://10.36.0.68:8080/   账号：tester   密码：123456
    jenkins启动方式：java -jar E:\jenkins\jenkins.war
    邮件报告地址：http://10.36.0.68:8989/id/   [需要启动Nginx服务，目录：E:\nginx]
    
    