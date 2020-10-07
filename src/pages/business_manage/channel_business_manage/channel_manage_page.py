import time

from src.pages.base_page import BasePage


class ChannelManageActivity:
    """
    渠道管理
    """
    # beijing
    beijing = ('css', '.el-input__suffix-inner > .el-icon-arrow-down')

    # 销售厅名称
    name_input = ('xpath', '//*[@placeholder="请输入销售厅名称"]')

    # 流程状态
    status_select = ('xpath', '//*[@placeholder="请选择流程状态"]')

    # 下拉按钮
    owner_select = ('css', '.el-input__suffix-inner > .el-icon-arrow-down')

    # 查询
    search_btn = ('css', '.el-form-item__content > .el-button--primary')

    # 重置
    reset_btn = ('css', '.el-form-item__content > .el-button--default')

    # 展开
    more_query = ('css', '.el-button:nth-child(3) > span')

    """
    编辑弹窗
    """
    # 确认
    confirm_btn = ('xpath', '//div[9]/div/div/button[1]')

    # 取消
    cancel_btn = ('xpath', '//div[9]/div/div/button[2]')


global page


class ChannelManagePage(BasePage):
    """
    渠道列表
    """

    def __init__(self, driver):
        super().__init__(driver)
        global page
        page = ChannelManageActivity()

    def query_channel_name(self, name=None):
        """
        渠道机构查询
        """
        if name:
            self.send_keys(page.name_input, name)
        self.click_element(page.search_btn)
        time.sleep(2)

    def reset_query(self):
        """
        查询重置
        """
        self.click_element(page.reset_btn)

    def read_query_name(self):
        """
        读取查询条件：名称
        :return:
        """
        return self.get_text(page.name_input)

    def click_more_query(self):
        """
        显示更多查询条件
        :return:
        """
        if not self.wait_exist(page.status_select):
            self.click_element(page.more_query)
            time.sleep(1)

    def is_more_query(self):
        """
        显示了更多查询条件
        :return:
        """
        return self.wait_exist(page.status_select)

    def click_view_organization(self, index=1):
        """
        查看机构详情
        :return:
        """
        # 查看
        view_btn = ('xpath', '//div[5]/div[2]/table/tbody/tr[{}]/td[20]/div/button[1]'.format(index))
        if self.wait_exist(view_btn):
            self.click_element(view_btn)
            time.sleep(2)

    def click_edit_organization(self, index=1):
        """
        编辑机构
        :param index:
        :return:
        """
        # 编辑
        edit_btn = ('xpath', '//div[5]/div[2]/table/tbody/tr/td[20]/div/button[2]'.format(index))
        if self.wait_exist(edit_btn):
            self.click_element(edit_btn)
            time.sleep(2)

    def confirm_fee(self):
        """
        提交编辑
        :return:
        """
        self.click_element(page.confirm_btn)

    def cancel_fee(self):
        """
        取消提交
        :return:
        """
        self.click_element(page.cancel_btn)
