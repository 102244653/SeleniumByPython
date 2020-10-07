import time

from src.pages.base_page import BasePage


class RecordManageActivity:
    # 业务标题
    title_input = ('xpath', '//*[@placeholder="请输入业务标题"]')

    # 业务类型
    type_select = ('xpath', '//placeholder="请选择业务类型"')

    # 完成时间
    start = ('xpath', '//*[@placeholder="开始日期"]')

    # 查询
    search_btn = ('css', '.el-button > span:nth-child(2)')

    # 重置
    reset_btn = ('css', '.el-form-item__content > .el-button--default > span')

    # 展开
    more_query_btn = ('css', '.el-button:nth-child(3) > span')

    # 审批详情
    detail_btn = ('', '//div[5]/div[2]/table/tbody/tr/td[10]/div/button/span')

    # 表单数据
    data_btn = ('', '//div[5]/div[2]/table/tbody/tr/td[10]/div/button[2]/span')


global page


class RecordManagePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        global page
        page = RecordManageActivity()

    def simple_query(self, title=None, _type=None):
        """
        简单查询
        :return:
        """
        if _type:
            self.send_keys(page.type_select, _type)
        if title:
            self.send_keys(page.title_input, title)
        self.click_element(page.search_btn)
        self.loading(3)

    def read_record_cell_title(self, index=1):
        """
        读取列表的标题
        :return:
        """
        title_cell = ('xpath', '//tbody/tr[{}]/td[2]/div'.format(index))
        if self.wait_exist(title_cell):
            return self.get_text(title_cell)
        else:
            return ''

    def reset_query(self):
        """
        重置查询
        :return:
        """
        self.click_element(page.reset_btn)

    def read_query_title(self):
        """
        读取查询标题
        :return:
        """
        return self.get_text(page.title_input)

    def click_more_query(self):
        """
        展开更多查询
        :return:
        """
        if not self.wait_exist(page.start, 5):
            self.click_element(page.more_query_btn)

    def is_more_query(self):
        """
        是否打开更多查询
        :return:
        """
        return self.wait_exist(page.start, 5)

    def click_view_detail(self, index=1):
        """
        查看详情
        :return:
        """
        view_btn = ('xpath', '//div[5]/div[2]/table/tbody/tr[{}]/td[10]/div/button/span'.format(index))
        self.click_element(view_btn)
        time.sleep(1)

    def click_view_data(self, index=1):
        """
        查看表单数据
        :return:
        """
        view_btn = ('xpath', '//div[5]/div[2]/table/tbody/tr[{}]/td[10]/div/button[2]/span'.format(index))
        self.click_element(view_btn)
        time.sleep(1)
