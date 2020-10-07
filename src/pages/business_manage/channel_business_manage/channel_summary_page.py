import time

from src.pages.base_page import BasePage


class ChannelSummaryActivity:
    """
    渠道汇总
    """
    # 所属机构
    owner_text = ('xpath', '//*[@placeholder="请选择所属机构"]')

    # beijing
    beijing = ('css', '.el-input__suffix-inner > .el-icon-arrow-down')

    # 查询
    search_btn = ('css', '.el-form-item__content > .el-button--primary')

    # 重置
    reset_btn = ('css', '.el-form-item__content > .el-button--default')


global page


class ChannelSummaryPage(BasePage):
    """
    渠道列表
    """

    def __init__(self, driver):
        super().__init__(driver)
        global page
        page = ChannelSummaryActivity()

    def query_channel(self):
        """
        渠道机构查询
        """
        self.select_beijing(page.owner_text, True)
        self.click_element(page.search_btn)
        time.sleep(2)

    def reset_query(self):
        """
        查询重置
        """
        self.click_element(page.reset_btn)

    def view_next_organization(self, index=1):
        """
        查看下级机构
        """
        view_btn = ('xpath', '//div[5]/div[2]/table/tbody/tr[{}]/td[9]/div/button'.format(index))
        if self.wait_exist(view_btn):
            self.click_element(view_btn)
            time.sleep(2)
