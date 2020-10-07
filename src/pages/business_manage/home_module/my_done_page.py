from src.pages.base_page import BasePage


class MyDoneActivity:
    # 业务标题
    title_input = ('xpath', '//*[@placeholder="请输入业务标题"]')

    # 业务类型
    type_select = ('xpath', '//*[@placeholder="请选择业务类型"]')

    # 更新时间
    start = ('xpath', '//*[@placeholder="开始日期"]')

    # 查询
    search_btn = ('css', '.el-form-item__content > .el-button--primary > span')

    # 重置
    reset_btn = ('css', '.el-form-item__content > .el-button--primary > span')

    # 收起
    display_btn = ('css', '.el-button:nth-child(3) > span')

    # 导出
    export_btn = ('id', 'myToDo-export')


global page


class MyDonePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        global page
        page = MyDoneActivity()

    def simple_query(self, title=None):
        """
        简单的搜索，两个条件
        :param title:
        :return:
        """
        if title:
            self.send_keys(page.title_input, title)
        self.click_element(page.search_btn)
        self.loading(2)

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
        展示更多查询条件
        :return:
        """
        if not self.wait_exist(page.start, 5):
            self.click_element(page.display_btn)

    def is_more_query(self):
        """
        已打开更多查询
        :return:
        """
        return self.wait_exist(page.start)

    def read_mydone_cell_title(self, index=1):
        """
        读取已完成列表的标题
        :param index:
        :return:
        """
        title_cell = ('xpath', '//tbody/tr[{}]/td[2]/div'.format(index))
        if self.wait_exist(title_cell):
            return self.get_text(title_cell)
        else:
            return ''

