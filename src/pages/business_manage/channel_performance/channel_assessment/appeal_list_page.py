"""
申诉列表
"""
import time

from src.pages.base_page import BasePage


class AppealListActivity:
    # 渠道编号
    channel_id_input = ('xpath', '//*[@placeholder="请输入渠道编号"]')

    # 负责人手机号
    phone_input = ('xpath', '//*[@placeholder="请输入负责人手机号"]')

    # 处理状态
    status_select = ('xpath', '//*[@placeholder="请选择处理状态"]')


global page


class AppealListPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        global page
        page = AppealListActivity()

    def query_appeal_list(self, id=None, phone=None):
        """
        查询
        :param id:
        :param phone:
        :return:
        """
        if id:
            self.send_keys(page.channel_id_input, id)
        if phone:
            self.send_keys(page.phone_input, phone)
        self.click_search_button()

    def read_query_phone(self):
        """
        读取查询条件
        :return:
        """
        return self.get_text(page.phone_input)

    def click_more_query(self):
        """
        展示更多查询
        :return:
        """
        if not self.wait_exist(page.status_select):
            self.click_show_more_query()

    def is_more_query(self):
        """
        是否展示更多查询
        :return:
        """
        return self.wait_exist(page.status_select)

    def click_view_appeal_list(self, index=1):
        """
        点击详情
        :return:
        """
        view_btn = ('xpath', '//div[5]/div[2]/table/tbody/tr[{}]/td[8]/div/button'.format(index))
        if self.wait_exist(view_btn):
            self.click_element(view_btn)
            time.sleep(2)