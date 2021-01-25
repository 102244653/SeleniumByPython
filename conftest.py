import os
import sys
import time
from datetime import datetime
import allure
from selenium import webdriver
import pytest
from src.common.log import Logger
from src.common.small_tools import SmallTool
from src.config.readconfig import data

'''
初始化driver
在执行命令中增加命令行选项
'''
log = Logger().get_logger()
driver = None


@pytest.fixture(scope="class")
# scope指定级别，取值可以是"function"(default),"class","module","package" or "session"
def init_browser(request):
    """
    启动浏览器，打开测试网页并最大化
    scope=class时使用cls，scope=function时使用instance
    """
    global driver
    browser = cmd_browser(request)
    log.info('###############初始化【{}】浏览器################'.format(browser))
    dr = cmd_dr(request)
    c = 0
    if c < 3:
        try:
            if browser == 'chrome':
                SmallTool.kill_process('chromedriver.exe')
                request.cls.driver = webdriver.Chrome(data.get_driver_path(dr, 'chrome'))  # 参数是驱动安装地址
            elif browser == 'ie':
                request.cls.driver = webdriver.Ie(executable_path=data.get_driver_path(dr, 'ie'))
            elif browser == 'firefox':
                SmallTool.kill_process('geckodriver.exe')
                request.cls.driver = webdriver.Firefox(executable_path=data.get_driver_path(dr, 'firefox'))
            else:
                raise Exception("浏览器类型{}设置错误,请选择：chrome/ie/firefox".format(browser))
        except Exception as e:
            log.error(e)
            c += 1

    # 浏览器配置
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--no-sandbox')
    # request.cls.driver = webdriver.Remote(command_executor='http://127.0.0.1:5001/wd/hub',
    #                                       desired_capabilities=chrome_options.to_capabilities())

    driver = request.cls.driver
    driver.maximize_window()
    driver.implicitly_wait(15)

    def teardown():
        """
        关闭浏览器
        """
        try:
            driver.close()
            driver.quit()
        except Exception as e:
            driver.quit()
            log.error('浏览器关闭失败：'+e)

    request.addfinalizer(teardown)


@pytest.fixture(scope="class")
def user_login(request):
    global driver
    env = cmd_env(request)
    username, password = data.get_account(env)
    driver.get(data.get_env(env))
    time.sleep(5)
    assert driver.title == '福乐彩运营管理平台', '打开登录页面失败'
    from src.pages.admin_page import AdminPage
    login_page = AdminPage(driver)
    login_page.login(username, password)

    def logout():
        login_page.logout()

    request.addfinalizer(logout)


def pytest_addoption(parser):
    # 增加一条命令行选项,在pytest执行命令中可以通过--cmd_driver=xxx配置参数
    parser.addoption("--cmd_browser", action="store", default="chrome", help="请选择浏览器类型")
    parser.addoption("--cmd_env", action="store", default="test", help="请选择测试环境")
    parser.addoption("--cmd_dr", action="store", default="jenkins", help="请选择执行场景：local/jenkins")


def cmd_env(request):
    # 脚本获取命令行参数的接口
    value = request.config.getoption("--cmd_env")
    return value.lower()


def cmd_browser(request):
    value = request.config.getoption("--cmd_browser")
    return value.lower()


def cmd_dr(request):
    value = request.config.getoption("--cmd_dr")
    return value.lower()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    '''
    hook pytest失败
    :param item:
    :param call:
    :return:
    '''
    outcome = yield
    rep = outcome.get_result()

    # we only look at actual failing test calls, not setup/teardown
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures") else "w"
        with open("failures", mode) as f:
            # let's also access a fixture for the fun of it
            if "tmpdir" in item.fixturenames:
                extra = " (%s)" % item.funcargs["tmpdir"]
            else:
                extra = ""
            f.write(rep.nodeid + extra + "\n")
            global driver
            path = make_path()
            name = datetime.now().strftime('%m%d%H%M%S')
            path_name = u'{}/{}.png'.format(path, name)
            driver.get_screenshot_as_file(path_name)
            allure.attach.file(path_name, "【断言失败截图:{}.png】".format(name), allure.attachment_type.PNG)


def make_path():
    '''
    创建保存失败截图的文件目录
    :param nodeid:
    :return:
    '''
    path = '{}/screenshot'.format(os.path.split(os.path.realpath(__file__))[0].replace('\src\cases', ''))
    if not os.path.exists(path):
        os.makedirs(path)
    return path
