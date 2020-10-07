"""
配件列表
"""

import time

from src.pages.base_page import BasePage


class PartsListActivity:
    # 配件名称
    name_input = ('xpath', '//*[@placeholder="请输入配件名称"]')

    # 物品型号
    type_input = ('xpath', '//*[@placeholder="请输入物品型号"]')

    # 打印
    print_btn = ('id', 'mountingsList-print')


global page


class PartsListPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        global page
        page = PartsListActivity()

    def query_parts_list(self, name=None, _type=None):
        """
        设备列表查询
        :param name:
        :param _type:
        :return:
        """
        if name:
            self.send_keys(page.name_input, name)
        if _type:
            self.send_keys(page.type_input, _type)
        self.click_search_button()

    def read_query_data(self, input='name'):
        """
        读取查询条件
        :param input:
        :return:
        """
        if input == 'name':
            return self.get_text(page.name_input)
        if input == 'type':
            return self.get_text(page.type_input)

    def index_view_parts_detail(self, index=1):
        """
        查看设备信息
        :return:
        """
        view_btn = ('xpath', '//div[5]/div[2]/table/tbody/tr[{}]/td[6]/div/button'.format(index))
        if self.wait_exist(view_btn):
            self.click_element(view_btn)
            time.sleep(2)

    def click_print_button(self):
        """
        点击打印按钮
        :return:
        """
        self.click_element(page.print_btn)