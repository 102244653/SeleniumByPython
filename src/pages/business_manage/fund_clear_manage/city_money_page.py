"""
城市资金参数
"""
import time

from src.pages.base_page import BasePage


class CityMoneyActivity:
    # 游戏名称
    name_select = ('xpath', '//*[@placeholder="请选择游戏名称"]')

    # 批量编辑
    select_edit_btn = ('xpath', '//*[@id="cardGeneration-add"][1]')

    # 全部编辑
    all_edit_btn = ('xpath', '//*[@id="cardGeneration-add"][2]')


global page


class CityMoneyPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        global page
        page = CityMoneyActivity()

    def query_city_money(self, name=None):
        """
        城市资金列表查询
        :param name:
        :return:
        """
        if name:
            self.select_pull_down_list(page.name_select, name)
        self.click_search_button()

    def click_selcet_edit_btn(self, index=[]):
        """
        批量编辑
        :param index:
        :return:
        """
        if len(index) != 0:
            for i in index:
                self.click_element(('xpath', '//div[2]/table/tbody/tr[{}]/td/div/label/span/span'.format(i)))
        self.click_element(page.select_edit_btn)

    def click_all_edit_btn(self):
        """
        全部编辑
        :return:
        """
        self.click_element(page.all_edit_btn)

    def click_edit_detail_btn(self, index=1):
        """
        点击编辑按钮
        :param index:
        :return:
        """
        edit_btn = ('xpath', '//div[5]/div[2]/table/tbody/tr[{}]/td[8]/div/button'.format(index))
        if self.wait_exist(edit_btn):
            self.click_element(edit_btn)
            time.sleep(2)