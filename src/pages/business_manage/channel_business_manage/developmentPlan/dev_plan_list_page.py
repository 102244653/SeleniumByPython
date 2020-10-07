import time
from datetime import datetime

from src.pages.base_page import BasePage


class DevPlanListActivity:
    """
    年度计划
    """
    # 计划年份
    plan_year_input = ('css', '.el-date-editor > .el-input__inner')

    # 查询
    search_btn = ('css', '.el-form-item__content > .el-button--primary')

    # 重置
    reset_btn = ('css', '.el-form-item__content > .el-button--default')

    # 新建发展计划
    create_dev_plan_btn = ('id', 'developmentPlanList-new')


global page


class DevPlanListPage(BasePage):
    """
    渠道列表
    """

    def __init__(self, driver):
        super().__init__(driver)
        global page
        page = DevPlanListActivity()

    def query_by_year(self, _year=None):
        """
        按年份查询
        :return:
        """
        if _year:
            _year = datetime.now().year
        self.send_keys(page.plan_year_input, _year)
        self.click_element(page.search_btn)
        time.sleep(2)

    def reset_query(self):
        """
        重置查询
        :return:
        """
        self.click_element(page.reset_btn)

    def read_query_year(self):
        """
        读取查询的时间
        :return:
        """
        return self.get_text(page.plan_year_input)

    def click_create_dev_plan(self):
        """
        点击新建发展计划
        :return:
        """
        self.click_element(page.create_dev_plan_btn)

    def click_shi_plan_btn(self, index=1):
        """
        点击查看市级计划
        :return:
        """
        # 市级计划列表
        shi_plan_btn = ('xpath', '//div[5]/div[2]/table/tbody/tr[{}]/td[16]/div/div/button[1]'.format(index))
        if self.wait_exist(shi_plan_btn):
            self.click_element(shi_plan_btn)
            time.sleep(2)

    def click_view_plan_btn(self, index=1):
        """
        点击查看计划
        :return:
        """
        # 查看
        view_btn = ('xpath', '//div[5]/div[2]/table/tbody/tr[{}]/td[16]/div/div/button[2]'.format(index))
        if self.wait_exist(view_btn):
            self.click_element(view_btn)
            time.sleep(2)

    def click_edit_plan_btn(self):
        """
        编辑计划
        :return:
        """
        # 编辑
        edit_btn = ('xpath', '//div[5]/div[2]/table/tbody/tr[{}]/td[16]/div/div/button[3]')
        if self.wait_exist(edit_btn):
            self.click_element(edit_btn)
            time.sleep(2)