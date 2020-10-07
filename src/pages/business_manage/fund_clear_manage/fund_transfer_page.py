"""
资金划拨管理
"""
import time

from src.pages.base_page import BasePage


class FundTransferActivity:
    """
    资金划拨管理
    """
    # 新增
    create_btn = ('xpath', 'fundTransferList-create')


global page


class FundTransferPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        global page
        page = FundTransferActivity()

    def click_create_btn(self):
        """
        点击新增按钮
        :return:
        """
        self.click_element(page.create_btn)

    def click_on_off_btn(self, index=1):
        """
        点击启用、关闭开关
        :param index:
        :return:
        """
        on_off_btn = ('xpath', '//div[@id="main"]/div/div/div[2]/div[3]/table/tbody/tr[{}]/td[3]/div/div/span'.format(index))
        if self.wait_exist(on_off_btn):
            self.click_element(on_off_btn)
            time.sleep(2)

    def click_view_btn(self, index=1):
        """
        点击查看开关
        :param index:
        :return:
        """
        view_btn = ('xpath', '//div[@id="main"]/div/div/div[2]/div[3]/table/tbody/tr[{}]/td[3]/div/div/span'.format(index))
        if self.wait_exist(view_btn):
            self.click_element(view_btn)
            time.sleep(2)