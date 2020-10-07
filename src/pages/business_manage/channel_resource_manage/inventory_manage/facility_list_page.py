"""
设施列表
"""
import time

from src.pages.base_page import BasePage


class FacilityLiastActivity:
    # 设施名称
    name_input = ('xpath', '//*[@placeholder="请输入设施名称"]')

    # 打印
    print_btn = ('id', 'facilityList-print')


global page


class FacilityListPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        global page
        page = FacilityLiastActivity()

    def query_parts_list(self, name=None):
        """
        设备列表查询
        :param name:
        :return:
        """
        if name:
            self.send_keys(page.name_input, name)
        self.click_search_button()

    def read_query_name(self):
        """
        读取查询条件
        :return:
        """
        return self.get_text(page.name_input)

    def click_view_facility_detail(self, index=1):
        """
        查看设备信息
        :return:
        """
        view_btn = ('xpath', '//div[5]/div[2]/table/tbody/tr[{}]/td[5]/div/button'.format(index))
        if self.wait_exist(view_btn):
            self.click_element(view_btn)
            time.sleep(2)

    def click_print_button(self):
        """
        点击打印按钮
        :return:
        """
        self.click_element(page.print_btn)
