"""
台账管理
"""
import time

from src.pages.base_page import BasePage


class LedgerManageActivity:
    # 仓库名称
    store_name_input = ('xpath', '//*[@placeholder="请输入仓库名称"]')

    # 仓库类型
    store_type_select = ('xpath', '//*[@placeholder="请选择仓库类型"]')

    # 渠道名称
    channel_name_input = ('xpath', '//*[@placeholder="请输入渠道名称"]')

    # 渠道编号
    channel_id_input = ('xpath', '//*[@placeholder="请输入渠道编号"]')

    # 打印
    ptint_btn = ('id', 'ledgerManage-print')


global page


class LedgerManagePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        global page
        page = LedgerManageActivity()

    def simple_query_ledger(self, name=None):
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

    def click_print_ledger(self):
        """
        点击打印按钮
        :return:
        """
        self.click_element(page.ptint_btn)

    def click_view_ledger_detail(self, index=1):
        """
        查看详情
        :param index:
        :return:
        """
        # 台账明细
        view_btn = ('xpath', '//div[5]/div[2]/table/tbody/tr[{}]/td[9]/div/button'.format(index))
        if self.wait_exist(view_btn):
            self.click_element(view_btn)
            time.sleep(2)