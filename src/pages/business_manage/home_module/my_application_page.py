import time

from src.pages.base_page import BasePage


class MyApplicationActivity:
    # 业务标题
    title_input = ('xpath', '//*[@placeholder="请输入业务标题"]')

    # 审批节点
    node_input = ('xpath', '//*[@placeholder="请输入审批节点"]')

    # 业务类型
    type_select = ('xpath', '//*[@placeholder="请选择业务类型"]')

    # 所属结构
    owner_select = ('', '')

    # 更新时间
    start = ('xpath', '//*[@placeholder="开始日期"]')

    # 查询
    search_btn = ('css', '.el-form-item__content > .el-button--primary > span')

    # 重置
    reset_btn = ('css', '.el-button--default > span')

    # 收起
    display_btn = ('css', '.el-button:nth-child(3) > span')

    # 打印
    print_btn = ('id', 'myApplication-print')

    # 导出
    export_btn = ('id', 'myApplication-export')


global page


class MyApplicationPage(BasePage):
    """
    我的申请界面
    """

    def __init__(self, driver):
        super().__init__(driver)
        global page
        page = MyApplicationActivity()

    def simple_query(self, title=None, node=None):
        """
        简单的搜索，两个条件
        :param title:
        :param node:
        :return:
        """
        if title:
            self.send_keys(page.title_input, title)
        if node:
            self.send_keys(page.node_input, node)
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
        if not self.wait_exist(page.type_select, 5):
            self.click_element(page.display_btn)

    def is_more_query(self):
        """
        已打开更多查询
        :return:
        """
        return self.wait_exist(page.type_select)

    def click_view_detail(self, index=1):
        """
        点击查看详情
        :return:
        """
        view_btn = ('xpath', '//div[5]/div[2]/table/tbody/tr[{}]/td[7]/div/div/button/span'.format(index))
        self.click_element(view_btn)
        time.sleep(1)

    def read_business_cell_title(self, index=1):
        """
        读取申请列表的标题
        :param index:
        :return:
        """
        title_cell = ('xpath', '//tbody/tr[{}]/td[2]/div'.format(index))
        if self.wait_exist(title_cell):
            return self.get_text(title_cell)
        else:
            return ''

    def click_print(self):
        """
        点击打印
        :return:
        """
        self.click_element(page.print_btn)

    def click_export(self):
        """
        点击导出
        :return:
        """
        self.click_element(page.export_btn)