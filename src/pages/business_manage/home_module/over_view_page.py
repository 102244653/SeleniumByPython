from src.pages.base_page import BasePage


# 概况
class OverViewActivity:
    # 待审核图标
    wait_confirm_icon = ('xpath', '//div[@class="nav-wrap"]/div[1]')

    # 已审核图标
    have_confirm_icon = ('xpath', '//div[@class="nav-wrap"]/div[2]')

    # 已申请图标
    have_apply_icon = ('xpath', '//div[@class="nav-wrap"]/div[3]')

    # 已知会图标
    have_notified_icon = ('xpath', '//div[@class="nav-wrap"]/div[4]')

    # 更多消息
    more_message = ('class', 'el-link--inner')


global page


class OverViewPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        global page
        page = OverViewActivity()

    def click_wait_confirm(self):
        """
        点击待审核
        :return:
        """
        self.click_element(page.wait_confirm_icon)

    def click_have_confirm(self):
        """
        点击已确认
        :return:
        """
        self.click_element(page.have_confirm_icon)

    def click_have_apply(self):
        """
        点击已申请
        :return:
        """
        self.click_element(page.have_apply_icon)

    def click_have_notified(self):
        """
        点击已通知
        :return:
        """
        self.click_element(page.have_notified_icon)

    def click_more_message(self):
        """
        点击更多消息
        :return:
        """
        self.click_element(page.more_message)

