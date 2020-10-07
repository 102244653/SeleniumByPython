"""
考核项列表
"""
import time

from src.pages.base_page import BasePage


class AssessItemSetActivity:
    # 考核名称
    name_input = ('xpath', '//*[@placeholder="请输入考核名称"]')

    # 状态
    status_select = ('xpath', '//*[@placeholder="请选择状态"]')

    # 新增考核
    create_btn = ('id', 'assessItemSet-add')


global page


class AssessItemSetPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        global page
        page = AssessItemSetActivity()

    def query_assess_item(self, name=None, status=None):
        """
        查询
        :param name:
        :param status:
        :return:
        """
        if name:
            self.send_keys(page.name_input, name)
        if status:
            self.select_pull_down_list(page.status_select, status)
        self.click_search_button()

    def read_query_name(self):
        """
        读取查询名称
        :return:
        """
        return self.get_text(page.name_input)

    def click_create_assess_item(self):
        """
        新增考核项
        :return:
        """
        self.click_element(page.create_btn)

    def click_view_assess_item(self, index=1):
        """
        查看考核项详情
        :param index:
        :return:
        """
        view_btn = ('xpath', '//div[5]/div[2]/table/tbody/tr[{}]/td[8]/div/button[1]'.format(index))
        if self.wait_exist(view_btn):
            self.click_element(view_btn)
            time.sleep(2)

    def click_edit_assess_item(self, index=1):
        """
        编辑考核项详情
        :param index:
        :return:
        """
        edit_btn = ('xpath', '//div[5]/div[2]/table/tbody/tr[{}]/td[8]/div/button[2]'.format(index))
        if self.wait_exist(edit_btn):
            self.click_element(edit_btn)
            time.sleep(2)

    def click_delete_assess_item(self, index=1):
        """
        删除考核项详情
        :param index:
        :return:
        """
        delete_btn = ('xpath', '//div[5]/div[2]/table/tbody/tr[{}]/td[8]/div/button[3]'.format(index))
        if self.wait_exist(delete_btn):
            self.click_element(delete_btn)
            time.sleep(2)
