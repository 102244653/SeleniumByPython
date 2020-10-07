"""
仓库管理
"""

import time

from src.pages.base_page import BasePage


class StoreManageActivity:
    # 仓库名称
    store_name_input = ('xpath', '//*[@placeholder="请输入仓库名称"]')

    # 渠道名称
    channel_name_input = ('xpath', '//*[@placeholder="请输入渠道名称"]')

    # 渠道编号
    channel_id_input = ('xpath', '//*[@placeholder="请输入渠道编号"]')


global page


class StoreManagePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        global page
        page = StoreManageActivity()

    def simple_query_store(self, name=None):
        """
        查询
        :return:
        """
        if name:
            self.send_keys(page.store_name_input, name)
        self.click_search_button()

    def read_query_name(self):
        """
        读取查询条件
        :return:
        """
        return self.get_text(page.store_name_input)

    def is_more_query(self):
        """
        是否显示了更多查询
        :return:
        """
        return self.wait_exist(page.channel_name_input)

    def click_more_query(self):
        """
        展开更多查询
        :return:
        """
        if not self.wait_exist(page.channel_name_input):
            self.click_show_more_query()

    def click_view_store_detail(self, index=1):
        """
        查看详情
        :param index:
        :return:
        """
        # 台账明细
        view_btn = ('xpath', '//div[5]/div[2]/table/tbody/tr[{}]/td[8]/div/button'.format(index))
        if self.wait_exist(view_btn):
            self.click_element(view_btn)
            time.sleep(2)
