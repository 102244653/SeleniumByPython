"""
配件损耗报表
"""

from src.pages.base_page import BasePage


class PartsLossActivity:
    # 设备名称
    name_select = ('xpath', '//*[@placeholder="请选择配件名称"]')

    # 设备型号
    type_select = ('xpath', '//*[@placeholder="请选择配件型号"]')

    # 所属机构
    orga_select = ('xpath', '//*[@placeholder="请选择所属机构"]')

    # 打印
    print_btn = ('id', 'accessoryLoss-print')


global page


class PartsLossPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        global page
        page = PartsLossActivity()

    def simple_query_parts_loss(self, name=None):
        """
        设备名称
        :param name:
        :return:
        """
        if name:
            self.select_pull_down_list(page.name_select, name)
        self.click_search_button()

    def read_query_name(self):
        """
        读取查询名称
        :return:
        """
        return self.get_text(page.name_select)

    def is_more_query(self):
        return self.wait_exist(page.orga_select)

    def click_more_query(self):
        """
        展开查询条件
        :return:
        """
        if not self.wait_exist(page.orga_select):
            self.click_show_more_query()

    def click_print_parts_loss(self):
        """
        点击打印
        :return:
        """
        self.click_element(page.print_btn)