import time

from src.pages.base_page import BasePage


class ChannelListActivity:
    """
    渠道列表
    """
    # 渠道编号
    channel_code_input = ('xpath', '//*[@placeholder="请输入渠道编号"]')

    # 渠道名称
    channel_name_input = ('xpath', '//*[@placeholder="请输入渠道名称"]')

    # 渠道类型
    channel_type_select = ('xpath', '//*[@placeholder="请选择渠道类型"]')

    # 渠道等级
    channel_level_select = ('xpath', '//*[@placeholder="请选择渠道等级"]')

    # 查询
    search_btn = ('css', '.el-form-item__content > .el-button--primary')

    # 重置
    reset_btn = ('css', '.el-form-item__content > .el-button--default')

    # 展开
    more_query_btn = ('css', '.el-button:nth-child(3) > span')

    # 导出当前

    # 导出全部


global page


class ChannelListPage(BasePage):
    """
    渠道列表
    """

    def __init__(self, driver):
        super().__init__(driver)
        global page
        page = ChannelListActivity()

    def simple_query_channel(self, channel_code=None, channel_name=None):
        """
        简单查询
        """
        if channel_code:
            self.send_keys(page.channel_code_input, channel_code)
        if channel_name:
            self.send_keys(page.channel_name_input, channel_name)
        self.click_element(page.search_btn)
        time.sleep(2)

    def read_query_name(self):
        """
        读取查询的渠道名称
        """
        return self.get_text(page.channel_name_input)

    def reset_query(self):
        """
        重置查询
        """
        self.click_element(page.reset_btn)

    def click_more_query(self):
        """
        展示更多查询
        """
        if not self.wait_exist(page.channel_type_select):
            self.click_element(page.more_query_btn)
            time.sleep(1)

    def is_more_query(self):
        """
        已显示更多查询
        """
        return self.wait_exist(page.channel_type_select)

    def view_channel_detail(self, index=1):
        """
        查看渠道详情
        :param index:
        """
        view_btn = ('xpath', '//div[5]/div[2]/table/tbody/tr[{}]/td[13]/div/button'.format(index))
        if self.wait_exist(view_btn):
            self.click_element(view_btn)
            time.sleep(2)
