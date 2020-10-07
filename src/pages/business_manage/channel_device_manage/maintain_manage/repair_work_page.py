"""
维修工单
"""
import time

from src.pages.base_page import BasePage


class RepairWorkActivity:

    # 维修人员
    worker_input = ('xpath', '//*[@placeholder="请输入维修人员"]')

    # 设备名称
    device_select = ('xpath', '//*[@placeholder="请选择设备名称"]')

    # 工单状态
    status_select = ('xpath', '//*[@placeholder="请选择工单状态"]')

    # 一键提醒
    all_remind = ('id', 'repairWork-oneClickReminder')


global page


class RepairWorkPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        global page
        page = RepairWorkActivity()

    def simple_query_repair(self, device=None, status=None):
        """
        设备名称查询
        :param device:
        :param status:
        :return:
        """
        if device:
            self.select_pull_down_list(page.device_select, device)
        if status:
            self.click_show_more_query()
            self.select_pull_down_list(page.status_select, status)
        self.click_search_button()

    def read_query_device_name(self):
        """
        读取查询：设备名称
        :return:
        """
        return self.get_text(page.device_select)

    def is_more_query(self):
        """
        是否显示了更多的查询
        :return:
        """
        return self.wait_exist(page.status_select)

    def click_more_query(self):
        """
        点击展开
        :return:
        """
        if not self.wait_exist(page.status_select):
            self.click_show_more_query()

    def click_all_remind(self):
        """
        点击一件提醒
        :return:
        """
        self.click_element(page.all_remind)

    def click_view_repair_detail(self, index=1):
        """
        点击查看详情
        :param index:
        :return:
        """
        # 查看
        view_btn = ('xpath', '//div[5]/div[2]/table/tbody/tr[{}]/td[11]/div/div/button[1]'.format(index))
        if self.wait_exist(view_btn):
            self.click_element(view_btn)
            time.sleep(2)

    def click_remind_btn(self, index=1):
        """
        点击提醒按钮
        :param index:
        :return:
        """
        # 提醒
        remind_btn = ('xpath', '//div[5]/div[2]/table/tbody/tr[{}]/td[11]/div/div/button[2]'.format(index))
        if self.wait_exist(remind_btn):
            self.click_element(remind_btn)
            time.sleep(2)