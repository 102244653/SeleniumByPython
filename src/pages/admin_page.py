import time

from src.pages.base_page import BasePage
"""
登录界面、登录后的主页
"""


class AdminActivity:
    """
    登录
    """
    username = ('xpath', '//*[starts-with(@placeholder,"请输入用户账号")]')
    display_pw = ('css', "i.iconfont.icon-mima-bukan")
    password = ('xpath', '//*[starts-with(@placeholder,"请输入用户密码")]')
    verify_code = ('xpath', '//*[starts-with(@placeholder,"请输入验证码")]')
    login_btn = ('xpath', '//div[@class="registerPwd"]//button')
    platform_name = ('css', '//div[@class="hd-logo"]//strong[@class="name"]')

    """
    退出
    """
    logout_btn = ('css', 'span.opr-icon.iconfont.icon-tuichu')


global page


class AdminPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        global page
        page = AdminActivity()

    def login(self, username, password):
        """
        登录
        :param username:
        :param password:
        :return:
        """
        self.send_keys(page.username, username)
        self.click_element(page.display_pw)
        self.send_keys(page.password, password)
        self.send_keys(page.verify_code, '1108')
        self.click_element(page.login_btn)
        time.sleep(5)
        if self.wait_not_exist(page.logout_btn):
            raise Exception('登录失败')

    def logout(self):
        if self.wait_not_exist(page.logout_btn):
            raise Exception('暂未登录')
        self.click_element(page.logout_btn)
        time.sleep(2)
        self.alert_confirm('提示')
        time.sleep(2)

    def into_subsystem(self, subsystem):
        """
        进入子系统
        :param sdbsystem:
        :return:
        """
        if subsystem == "业务管理":
            menu_css = "dt.iconfont.icon-yewuguanli"
        elif subsystem == "业务运营":
            menu_css = "dt.iconfont.icon-yewuyunying"
        elif subsystem == "业务监控":
            menu_css = "dt.iconfont.icon-yewujiankong"
        elif subsystem == "系统管理":
            menu_css = "dt.iconfont.icon-xitongguanli"
        elif subsystem == "客服系统":
            menu_css = "dt.iconfont.icon-kefuxitong"
        elif subsystem == "外部监管":
            menu_css = "dt.iconfont.icon-waibujianguan"
        else:
            raise Exception('未找到子系统：'+subsystem)
        subsystem_icon = ('css', menu_css)
        self.click_element(subsystem_icon)
        time.sleep(1)

    def select_menu(self, menu_list, is_load=None):
        """
        选择业务管理菜单
        :param menu_list: 首页/概况
        :param is_load:
        :return:
        """
        menu_list = menu_list.split('/')
        for menu in menu_list:
            menu_icon = ('xpath', '//*[starts-with(text(),"{}")][1]'.format(menu))
            self.click_element(menu_icon)
            time.sleep(2)
        if is_load:
            if type(is_load) == 'int':
                self.loading(is_load)
            else:
                self.loading()

    def select_same_menu(self, menu_list, is_load=False):
        """
        :param menu_list:  主子菜单同名的菜单列表
        :param is_load:
        :return:
        """
        menu_list = menu_list.split('/')
        for menu in menu_list:
            if menu.find("#") == -1:
                menu_icon = ('xpath', f'//div[@class="submenu-title"]//*[starts-with(text(),"{menu}")]')      # 一级菜单
            else:
                menu_icon = ('xpath', f'//li[@class="el-menu-item"]//*[starts-with(text(),"{menu[1:]}")]')      # 二级菜单
            self.click_element(menu_icon)
            time.sleep(2)
        if is_load:
            self.loading()


