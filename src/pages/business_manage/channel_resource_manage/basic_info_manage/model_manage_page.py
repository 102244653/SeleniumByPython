"""
型号管理
"""
import time

from src.pages.base_page import BasePage


class ModelManageActivity:
    # 物品类别
    type_select = ('xpath', '//*[@placeholder="请选择物品类别"]')

    # 物品名称
    name_select = ('xpath', '//*[@placeholder="请选择物品名称"]')

    # 物品状态
    status_select = ('xpath', '//*[@placeholder="请选择物品状态"]')

    # 新增
    create_btn = ('id', 'modelManage-add')


global page


class ModelManagePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        global page
        page = ModelManageActivity()

    def simple_query_model_manage(self, _type=None):
        """
        设备类别查询
        :param _type:
        :return:
        """
        if _type:
            self.select_pull_down_list(page.type_select, _type)
        self.click_search_button()

    def read_query_type(self):
        """
        读取查询条件：类别
        :return:
        """
        return self.get_text(page.type_select)

    def is_more_query(self):
        """
        是否显示了更多查询
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

    def click_create_model(self):
        """
        点击新增
        :return:
        """
        self.click_element(page.create_btn)

    def view_model_detail(self, index=1):
        """
        查看型号详情
        :param index:
        :return:
        """
        # 查看
        view_btn = ('xpath', '//div[5]/div[2]/table/tbody/tr[{}]/td[6]/div/button'.format(index))
        if self.wait_exist(view_btn):
            self.click_element(view_btn)
            time.sleep(2)

    def click_on_off_btn(self, index=1):
        """
        点击启用、关闭开关
        :param index:
        :return:
        """
        # 开启
        on_off_btn = ('xpath', '//div[@id="main"]/div/div/div[2]/div[3]/table/tbody/tr[{}]/td[4]/div/div/span'.format(index))
        if self.wait_exist(on_off_btn):
            self.click_element(on_off_btn)