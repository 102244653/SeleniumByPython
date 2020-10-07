"""
入库管理
"""
import time

from src.pages.base_page import BasePage


class PutStoreManageActivity:
    # 单据编号
    id_input = ('xpath', '//*[@placeholder="请输入单据编号"]')

    # 操作类型
    type_select = ('xpath', '//*[@placeholder="请输入单据编号"]')

    # 打印
    print_btn = ('id', 'putStoreManage-print')

    # 待出库
    tab_waiting = ('id', 'tab-waiting')

    # 已出库
    tab_already = ('id', 'tab-already')


global page


class PutStoreManagePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        global page
        page = PutStoreManageActivity()

    def query_put_store(self, id=None, select=None):
        """
        入库查询
        :param id:
        :param select:
        :return:
        """
        if id:
            self.send_keys(page.id_input, id)
        if select:
            self.select_value(page.title_select, select)
        self.click_search_button()

    def read_query_id(self):
        return self.get_text(page.id_input)

    def switch_put_tab(self, tab='已入库'):
        """
        显示已入库、未入库
        :return:
        """
        if tab == '已入库':
            self.click_element(page.tab_already)
        elif tab == '未入库':
            self.click_element(page.tab_waiting)
        else:
            print('tab标签填写错误：'+tab)
        time.sleep(2)

    def click_view_put_store_detail(self, index=1):
        """
        查看入库单详情
        :return:
        """
        view_btn = ('xpath', '//div[5]/div[2]/table/tbody/tr[{}]/td[8]/div/button'.format(index))
        if self.wait_exist(view_btn):
            self.click_element(view_btn)
            time.sleep(2)

    def click_print_put_store(self):
        """
        点击打印
        :return:
        """
        self.click_element(page.print_btn)
        time.sleep(2)