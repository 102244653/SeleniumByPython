"""
渠道等级配置
"""
import time

from src.pages.base_page import BasePage


class LevelConfigActivity:
    # 等级名称
    level_name_input = ('xpath', '//*[@placeholder="请输入等级名称"]')

    # 等级状态
    level_status_input = ('xpath', '//*[@placeholder="请选择等级状态"]')

    # 新增等级
    create_btn = ('id', 'channelLevelConfig-add')


global page


class LevelConfigPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        global page
        page = LevelConfigActivity()

    def query_level_config(self, name=None):
        """
        查询等级列表
        :param name:
        :return:
        """
        if name:
            self.send_keys(page.level_name_input, name)
        self.click_search_button()

    def click_more_query(self):
        """
        展示更多查询
        :return:
        """
        if not self.wait_exist(page.level_status_input):
            self.click_show_more_query()

    def is_more_query(self):
        """
        显示了更多查询
        :return:
        """
        return self.wait_exist(page.level_status_input)

    def click_create_level(self):
        """
        点击新增等级
        :return:
        """
        self.click_element(page.create_btn)

    def click_view_level_detail(self, index=1):
        """
        点击查看详情
        :param index:
        :return:
        """
        view_btn = ('xpath', '//div[5]/div[2]/table/tbody/tr[{}]/td[11]/div/button[1]'.format(index))
        if self.wait_exist(view_btn):
            self.click_element(view_btn)
            time.sleep(2)

    def click_edit_level(self, index=1):
        """
        编辑详情
        :param index:
        :return:
        """
        edit_btn = ('xpath', '//div[5]/div[2]/table/tbody/tr[{}]/td[11]/div/button[2]'.format(index))
        if self.wait_exist(edit_btn):
            self.click_element(edit_btn)
            time.sleep(2)

    def click_delete_level(self, index=1):
        """
        删除详情
        :param index:
        :return:
        """
        delete_btn = ('xpath', '//div[5]/div[2]/table/tbody/tr[{}]/td[11]/div/button[3]'.format(index))
        if self.wait_exist(delete_btn):
            self.click_element(delete_btn)
            time.sleep(2)
