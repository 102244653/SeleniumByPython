"""
渠道等级考核
"""

import time

from src.pages.base_page import BasePage


class LevelAssessActivity:
    # 渠道编号
    channel_id_input = ('xpath', '//*[@placeholder="请输入渠道编号"]')

    # 渠道类型
    type_select = ('xpath', '//*[@placeholder="请选择渠道类型"]')


global page


class LevelAssessPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        global page
        page = LevelAssessActivity()

    def query_level_assess(self, id=None):
        """
        查询等级列表
        :param name:
        :return:
        """
        if id:
            self.send_keys(page.channel_id_input, id)
        self.click_search_button()

    def click_more_query(self):
        """
        展示更多查询
        :return:
        """
        if not self.wait_exist(page.type_select):
            self.click_show_more_query()

    def is_more_query(self):
        """
        显示了更多查询
        :return:
        """
        return self.wait_exist(page.type_select)

    def click_view_level_assess_detail(self, index=1):
        """
        点击查看详情
        :param index:
        :return:
        """
        view_btn = ('xpath', '//div[5]/div[2]/table/tbody/tr[{}]/td[10]/div/button'.format(index))
        if self.wait_exist(view_btn):
            self.click_element(view_btn)
            time.sleep(2)