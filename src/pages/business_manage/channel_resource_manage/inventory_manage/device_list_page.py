""""
设备列表
"""
import time

from src.pages.base_page import BasePage


class DeviceListActivity:
    # 设备名称
    name_input = ('xpath', '//*[@placeholder="请输入设备名称"]')

    # 设备型号
    type_input = ('xpath', '//*[@placeholder="请输入设备型号"]')

    # 打印
    print_btn = ('id', 'equipmentList-print')


global page


class DeviceListPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        global page
        page = DeviceListActivity()

    def query_device_list(self, name=None, _type=None):
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

    def click_view_device_detail(self, index=1):
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