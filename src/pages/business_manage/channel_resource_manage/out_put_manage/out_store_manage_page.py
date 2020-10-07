"""
出库管理
"""
import time

from src.pages.base_page import BasePage


class OutStoreManageActivity:
    # 单据编号
    id_input = ('xpath', '//*[@placeholder="请输入单据编号"]')

    # 申请标题
    title_input = ('xpath', '//*[@placeholder="请输入申请标题"]')

    # 打印
    print_btn = ('id', 'outStoreManage-print')

    # 待出库
    tab_waiting = ('id', 'tab-waiting')

    # 已出库
    tab_already = ('id', 'tab-already')


global page


class OutStoreManagePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        global page
        page = OutStoreManageActivity()

    def query_out_store(self, id=None, title=None):
        """
        出库查询
        :param id:
        :param title:
        :return:
        """
        if id:
            self.send_keys(page.id_input, id)
        if title:
            self.send_keys(page.title_input, title)
        self.click_search_button()

    def read_query_title(self):
        """
        读取查询标题
        :return:
        """
        return self.get_text(page.title_input)

    def click_print_out_store(self):
        """
        打印出库清单
        :return:
        """
        self.click_element(page.print_btn)

    def switch_out_tab(self, tab='已出库'):
        """
        显示已出库、未出库
        :return:
        """
        if tab == '已出库':
            self.click_element(page.tab_already)
        elif tab == '未出库':
            self.click_element(page.tab_waiting)
        else:
            print('tab标签填写错误：'+tab)
        time.sleep(2)

    def click_view_out_store_detail(self, index=1):
        """
        查看出库单详情
        :return:
        """
        view_btn = ('xpath', '//div[5]/div[2]/table/tbody/tr[{}]/td[8]/div/button'.format(index))
        if self.wait_exist(view_btn):
            self.click_element(view_btn)
            time.sleep(2)

