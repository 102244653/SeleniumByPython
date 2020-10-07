"""
全局参数管理
"""
import time

from src.pages.base_page import BasePage


class FundConfigActivity:
    #  参数名称
    name_input = ('xpath', '//*[@请输入参数名称]')

    # 参数状态
    status_select = ('xpath', '//*[@请选择参数状态]')


global page


class FundConfigPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        global page
        page = FundConfigActivity()

    def query_fund_config(self, name=None):
        """
        查询资金配置
        :param name:
        :return:
        """
        if name:
            self.send_keys(page.name_input, name)
        self.click_search_button()

    def click_view_fund_detail(self, index=1):
        """
        点击查看资金配置详情
        :param index:
        :return:
        """
        view_btn = ('xpath', '//div[5]/div[2]/table/tbody/tr[{}]/td[8]/div/button'.format(index))
        if self.wait_exist(view_btn):
            self.click_element(view_btn)
            time.sleep(2)

    def click_edit_fund_config(self, index=1):
        """
        点击编辑资金配置详情
        :param index:
        :return:
        """
        edit_btn = ('xpath', '//div[5]/div[2]/table/tbody/tr[{}]/td[8]/div/button[2]'.format(index))
        if self.wait_exist(edit_btn):
            self.click_element(edit_btn)
            time.sleep(2)

    def click_on_off_fund(self, index=1):
        """
        点击编辑资金配置详情
        :param index:
        :return:
        """
        on_off_btn = ('xpath', '//div[5]/div[2]/table/tbody/tr[{}]///td[4]/div/div/span'.format(index))
        if self.wait_exist(on_off_btn):
            self.click_element(on_off_btn)
            time.sleep(2)