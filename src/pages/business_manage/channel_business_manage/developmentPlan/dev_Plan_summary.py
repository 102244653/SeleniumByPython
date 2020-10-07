import time
from datetime import datetime

from src.pages.base_page import BasePage


class DevPlanSummaryActivity:
    """
    年度计划汇总
    """



global page


class ChannelManagePage(BasePage):
    """
    渠道列表，暂不写
    """

    def __init__(self, driver):
        super().__init__(driver)
        global page
        page = DevPlanSummaryActivity()




