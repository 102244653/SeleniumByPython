"""
维护知识库
"""
import time

from src.pages.base_page import BasePage


class KnowledgeMantainActivity:
    # 物品类别
    device_type_select = ('xpath', '//*[@placeholder="请选择物品类别"]')

    # 故障类型
    failure_type_select = ('xpath', '//*[@placeholder="请选择故障类型"]')


global page


class KnowledgeMaintainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        global page
        page = KnowledgeMantainActivity()

    def query_knowledge_maintain(self, device=None, failure=None):
        """
        查询
        :param device:
        :param failure:
        :return:
        """
        if device:
            self.select_pull_down_list(page.device_type_select, device)
        if failure:
            self.select_pull_down_list(page.failure_type_select, device)
        self.click_search_button()

    def read_query_device_type(self):
        """
        查看查询条件
        :return:
        """
        return self.get_text(page.device_type_select)

    def click_view_knowledge_detail(self, index=1):
        """
        查看详情
        :return:
        """
        # 查看
        view_btn = ('xpath', '//div[5]/div[2]/table/tbody/tr[{}]/td[6]/div/button'.format(index))
        if self.wait_exist(view_btn):
            self.click_element(view_btn)
            time.sleep(2)
