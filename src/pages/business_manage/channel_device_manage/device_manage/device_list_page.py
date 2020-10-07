"""
设备列表
"""

import time

from src.pages.base_page import BasePage


class DeviceListActivity:

    # 所属仓库
    store_input = ('xpath', '//*[@placeholder="请输入所属仓库"]')

    # 渠道名称
    channel_input = ('xpath', '//*[@placeholder="请输入渠道名称"]')

    # 设备名称
    device_input = ('xpath', '//*[@placeholder="请输入设备名称"]')


global page


class DeviceListPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        global page
        page = DeviceListActivity()

    def simple_query_device(self, store=None, channel=None):
        """
        查询
        :param store:
        :param channel:
        :return:
        """
        if store:
            self.send_keys(page.store_input, store)
        if channel:
            self.send_keys(page.channel_input, channel)
        self.click_search_button()

    def read_query_store(self):
        """
        读取查询条件
        :return:
        """
        return self.get_text(page.store_input)

    def click_more_query(self):
        """
        点击展示更多查询
        :return:
        """
        if not self.wait_exist(page.device_input):
            self.click_show_more_query()

    def is_more_query(self):
        """
        是否展示了更多的查询
        :return:
        """
        return self.wait_exist(page.device_input)

    def click_view_device_detail(self, index=1):
        """
        查看详情
        :param index:
        :return:
        """
        view_btn = ('xpath', '//div[5]/div[2]/table/tbody/tr[{}]/td[11]/div/button'.format(index))
        if self.wait_exist(view_btn):
            self.click_element(view_btn)
            time.sleep(2)

    def click_view_device_record(self, index=1):
        """
        查看履历
        :return:
        """
        record_btn = ('xpath', '//div[5]/div[2]/table/tbody/tr[{}]/td[11]/div/button[2]'.format(index))
        if self.wait_exist(record_btn):
            self.click_element(record_btn)
            time.sleep(2)