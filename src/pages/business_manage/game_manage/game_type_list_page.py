import time

from src.pages.base_page import BasePage


class GameTypeActivity:
    # 类型名称
    name_input = ('xpath', '//*[@placeholder="请输入类型名称"]')

    # 类型状态
    status_input = ('xpath', '//*[@placeholder="请选择类型状态"]')

    # 查询
    search_btn = ('css', '.el-form-item__content > .el-button--primary')

    # 重置
    reset_btn = ('css', '.el-form-item__content > .el-button--default')

    # 新增类型
    add_type_btn = ('id', 'gameTypeList-add')

    """
    编辑弹窗
    """
    # 名称输入框
    type_name_input = ('xpath', '//form//*[@placeholder="请输入类型名称"]')

    # 编码输入框
    type_code_input = ('xpath', '//form//*[@placeholder="请输入类型编码"]')

    # 状态
    status_btn = ('xpath', '//div[@id="main"]/div/div/div[4]/div/div[2]/div/form/div[3]/div/div/span')

    # 类型说明
    type_desc_input = ('xpath', '//form//textarea')


global page


class GameTypePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        global page
        page = GameTypeActivity()

    def query_game_type(self, name=None, status=None):
        """
        查询游戏类型
        :param name:
        :param status:
        :return:
        """
        if name:
            self.send_keys(page.name_input, name)
        if status:
            self.send_keys(page.status_input, status)
        self.click_element(page.search_btn)
        time.sleep(1.5)

    def read_query_name(self):
        """
        读取输入的查询条件
        :return:
        """
        return self.get_text(page.name_input)

    def reset_query(self):
        """
        重置查询条件
        :return:
        """
        self.click_element(page.reset_btn)

    def read_type_status(self, index=1):
        """
        读取类型的启用状态
        :param index:
        :return:
        """
        type_status = ('xpath', '//div[@id="main"]/div/div/div[2]/div[3]/table/tbody/tr[{}]/td[4]/div/div/span[2]/span'.format(index))
        if self.wait_exist(type_status):
            return self.get_text(type_status)
        else:
            return ' '

    def click_type_status_btn(self, index=1):
        """
        点击状态按钮
        :param index:
        :return:
        """
        type_status_btn = ('xpath', '//div[@id="main"]/div/div/div[2]/div[3]/table/tbody/tr[{}]/td[4]/div/div/span[1]'.format(index))
        if self.wait_exist(type_status_btn):
            self.click_element(type_status_btn)
            time.sleep(1)

    def click_edit_btn(self, index=1):
        """
        点击编辑按钮
        :param index:
        :return:
        """
        edit_btn = ('xpath', '//div[5]/div[2]/table/tbody/tr[{}]/td[8]/div/button/span'.format(index))
        if self.wait_exist(edit_btn):
            self.click_element(edit_btn)
            time.sleep(1)

    def edit_game_type(self, name=None, desc=None):
        """
        编辑游戏类型
        :return:
        """
        if self.check_alert_is_exist('编辑类型'):
            if name:
                self.clear_text(page.type_name_input)
                self.send_keys(page.type_name_input, name)
            if desc:
                self.clear_text(page.type_desc_input)
                self.send_keys(page.type_desc_input, desc)
            self.confirm_alter()
            time.sleep(2)

    def click_add_type(self):
        """
        点击新增按钮
        :return:
        """
        self.click_element(page.add_type_btn)

    def add_game_type(self, name, code, desc=None, status=False):
        """
        新增游戏类型
        :param name:
        :param code:
        :param desc:
        :param status:
        :return:
        """
        if self.check_alert_is_exist('新增类型'):
            self.send_keys(page.type_name_input, name)
            self.send_keys(page.type_code_input, code)
            if desc:
                self.send_keys(page.type_desc_input, desc)
            if status:
                self.click_element(page.status_btn)
            self.confirm_alter()
            self.loading(2)

    def cancel_alter(self):
        """
        弹窗取消
        :return:
        """
        self.click_element(('xpath', '//*[@id="gameTypeList-form-cencel"]/span'))
        time.sleep(1.5)

    def confirm_alter(self):
        """
        弹窗确认
        :return:
        """
        self.click_element(('xpath', '//*[@id="gameTypeList-form-enter"]/span'))
        time.sleep(1.5)
