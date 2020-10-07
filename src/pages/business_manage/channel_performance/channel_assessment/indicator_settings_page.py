"""
指标列表
"""
import time

from src.pages.base_page import BasePage


class IndicatorSettingsAcyivity:
    # 指标名称
    name_input = ('xpath', '//*[@placeholder="请输入指标名称"]')

    # 指标类别
    i_type_input = ('xpath', '//*[@placeholder="请选择指标类别"]')

    # 渠道类型
    c_type_input = ('xpath', '//*[@placeholder="请选择考核类型"]')

    # 新增指标
    create_btn = ('id', 'indicatorSettings-add')


global page


class IndicatorSettingsPage(BasePage):
    """
    1
    """

    def __init__(self, driver):
        super().__init__(driver)
        global page
        page = IndicatorSettingsAcyivity()

    def query_indicator_list(self, i_name=None, i_type=None):
        """
        指标列表查询
        :param i_name:
        :param i_type:
        :return:
        """
        if i_name:
            self.send_keys(page.name_input, i_name)
        if i_type:
            self.select_pull_down_list(page.i_type_input, i_type)
        self.click_search_button()

    def read_query_name(self):
        return self.get_text(page.name_input)

    def click_more_query(self):
        """
        展开更多查询
        :return:
        """
        if not self.wait_exist(page.c_type_input):
            self.click_show_more_query()

    def is_more_query(self):
        """
        是否显示了更多查询
        :return:
        """
        return self.wait_exist(page.c_type_input)

    def click_create_indicator(self):
        """
        点击新增按钮
        :return:
        """
        self.click_element(page.create_btn)

    def click_view_indicator_detail(self, index=1):
        """
        点击查看指标详情
        :return:
        """
        view_btn = ('xpath', '//div[5]/div[2]/table/tbody/tr[{}]/td[8]/div/button[1]'.format(index))
        if self.wait_exist(view_btn):
            self.click_element(view_btn)
            time.sleep(2)

    def click_edit_indicator_detail(self, index=1):
        """
        点击编辑指标详情
        :return:
        """
        edit_btn = ('xpath', '//div[5]/div[2]/table/tbody/tr[{}]/td[8]/div/button[2]'.format(index))
        if self.wait_exist(edit_btn):
            self.click_element(edit_btn)
            print('$$$$$$$')
            time.sleep(2)

    def click_delete_indicator(self, index=1):
        """
        点击编辑指标详情
        :return:
        """
        delete_btn = ('xpath', '//div[5]/div[2]/table/tbody/tr[{}]/td[8]/div/button[3]'.format(index))
        if self.wait_exist(delete_btn):
            self.click_element(delete_btn)
            print('#######')
            time.sleep(2)