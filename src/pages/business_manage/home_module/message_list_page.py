
import time
from src.pages.base_page import BasePage


class MessageListActivity:
    # 标题
    title_input = ('xpath', '//*[@placeholder="请输入标题"]')

    # 查询按钮
    search_msg_btn = ('css', '.search-bar-comp:nth-child(1) .el-form .el-button:nth-child(1) > span')

    # 重置按钮
    reset_btn = ('css', '.search-bar-comp:nth-child(1) .el-button:nth-child(2) > span')

    # 发布消息
    send_message_btn = ('id', 'messageList-add')

    # 消息条数
    msg_num = ('xpath', '//*[starts-with(text()," 共搜索到 ")]/em')

    # 表格单元格[需要传坐标]
    table_cell = ('xpath', '//tbody/tr[{}]/td[{}]/div')

    """
    发布消息弹窗
    """
    # 消息弹窗
    msg_window_name = ('xpath', '/html/body/div[7]/div/div[2]/div[2]/div/div/div[4]/div/div[1]/span')

    msg_window = ('xpath', '//div[@aria-label="发布消息"]')

    # 关闭消息弹窗
    close_msg_window = ('xpath', '/html/body/div[7]/div/div[2]/div[2]/div/div/div[4]/div/div[1]/button')

    # 标题输入框
    msg_title = ('xpath', '//div[@class="el-dialog__body"]/div/form/div[1]/div[1]/div[1]/input')

    # 取消按钮
    cancel_msg = ('id', 'messageList-cancel')

    # 确定按钮
    confirm_msg = ('id', 'messageList-enter')


global page


class MessageListPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        global page
        page = MessageListActivity()

    def query_msg(self, title=None, start=None, end=None):
        """
        设置查询条件
        :param title: 标题
        :param start: 开始时间
        :param end: 结束时间
        :return:
        """
        if title:
            self.send_keys(page.title_input, title)
        if start and end:
            self.select_date(start, end)
        self.click_element(page.search_msg_btn)
        self.loading()

    def reset_query(self):
        """
        重置查询
        :return:
        """
        self.click_element(page.reset_btn)

    def read_query_title(self):
        """
        读取查询条件：标题
        :return:
        """
        return self.get_text(page.title_input)

    def read_msg_num(self):
        """
        读取消息总数
        :return:
        """
        num = self.get_text(page.msg_num)
        if num:
            return int(num)
        else:
            return 0

    def read_msg_cell_title(self, row=1):
        """
        读取消息列表的标题
        :param row:
        :return:
        """
        title_cell = ('xpath', '//tbody/tr[{}]/td[2]/div'.format(row))
        if self.wait_exist(title_cell):
            return self.get_text(title_cell)
        else:
            return ''

    def write_new_msg(self, msg=None):
        """
        发布一条新消息
        :param msg:
        :return:
        """
        self.click_element(page.send_message_btn)
        pass

    def is_msg_window(self):
        """
        判断消息发布窗口是否打开
        :return:
        """
        time.sleep(2)
        return self.wait_exist(page.msg_window)

    def close_msg_window(self):
        """
        关闭消息发布窗口
        :return:
        """
        self.click_element(page.cancel_msg)

    def confirm_msg(self):
        """
        提交发布消息
        :return:
        """
        self.click_element(page.confirm_msg)
        time.sleep(2)

    def click_view_msg(self, index=1):
        """
        点击查看按钮
        :param row:
        :return:
        """
        view_btn = ('xpath', '//div[@id="pane-0"]/div/div[5]/div[2]/table/tbody/tr[{}]/td[6]/div/button'.format(index))
        self.click_element(view_btn)
        time.sleep(1)

