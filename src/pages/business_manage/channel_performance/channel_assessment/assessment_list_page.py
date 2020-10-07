"""
考核列表
"""

import time

from src.pages.base_page import BasePage


class AssessmentListActivity:
    # 渠道编号
    channel_id_input = ('xpath', '//*[@placeholder="请输入渠道编号"]')

    # 所属机构
    orga_select = ('xpath', '//*[@placeholder="请选择所属机构"]')

    # 渠道类型
    type_select = ('xpath', '//*[@placeholder="请选择渠道类型"]')


global page


class AssessmentListPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        global page
        page = AssessmentListActivity()

    def query_assessment_list(self, id=None, orga=None):
        """
        查询
        :param id:
        :param phone:
        :return:
        """
        if id:
            self.send_keys(page.channel_id_input, id)
        if orga:
            self.send_keys(page.orga_select, orga)
        self.click_search_button()

    def read_query_id(self):
        """
        读取查询条件
        :return:
        """
        return self.get_text(page.channel_id_input)

    def click_more_query(self):
        """
        展示更多查询
        :return:
        """
        if not self.wait_exist(page.type_select):
            self.click_show_more_query()

    def is_more_query(self):
        """
        是否展示更多查询
        :return:
        """
        return self.wait_exist(page.type_select)

    def click_view_assessment_detail(self, index=1):
        """
        点击详情
        :return:
        """
        view_btn = ('xpath', '//div[5]/div[2]/table/tbody/tr[{}]/td[9]/div/button'.format(index))
        if self.wait_exist(view_btn):
            self.click_element(view_btn)
            time.sleep(2)

    def click_manual_assessment(self, index=1):
        """
        点击详情
        :return:
        """
        manual_btn = ('xpath', '//div[5]/div[2]/table/tbody/tr[{}]/td[9]/div/button[2]'.format(index))
        if self.wait_exist(manual_btn):
            self.click_element(manual_btn)
            time.sleep(2)