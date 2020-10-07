"""
资源申请管理
"""

from src.pages.base_page import BasePage


class ResourceApplyFormActivity:
    # 渠道名称
    channel_name_input = ('xpath', '//*[@placeholder="请输入渠道名称"]')

    # 申请标题
    apply_title_select = ('xpath', '//*[@placeholder="请输入申请标题"]')

    # 收货人
    reciver_input = ('xpath', '//*[@placeholder="请输入收货人"]')


global page


class ResourceApplyFormPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        global page
        page = ResourceApplyFormActivity()

    def simple_query_resource(self, name=None, title=None):
        """
        查询
        :return:
        """
        self.click_more_query()
        if name:
            self.send_keys(page.channel_name_input, name)
        if title:
            self.send_keys(page.channel_name_input, title)
        self.click_search_button()

    def read_query_name(self):
        """
        读取查询条件
        :return:
        """
        return self.get_text(page.channel_name_input)

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
