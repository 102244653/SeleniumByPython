"""
耗材列表
"""

import allure
import pytest

from src.pages.admin_page import AdminPage
from src.pages.business_manage.channel_resource_manage.inventory_manage.consumable_list_page import ConsumableListPage

global consumable_list_page, admin_page


@pytest.mark.usefixtures('user_login')
@pytest.mark.usefixtures('init_browser')
@allure.story("耗材列表")
class TestDeviceList:

    @pytest.fixture(scope='function')
    def set_up(self):
        """
        前置操作
        :return:
        """
        global consumable_list_page, admin_page
        consumable_list_page = ConsumableListPage(self.driver)
        admin_page = AdminPage(self.driver)

        admin_page.into_subsystem('业务管理')
        admin_page.select_menu('首页/渠道资源管理/库存管理')

    @pytest.mark.facilitylist
    @pytest.mark.run(order=210)
    def test_query_consumable_list(self, set_up):
        """
        查寻耗材列表
        1.输入类型名称：终端机
        【check_point】第一条结果名称选项包含：终端机
        :return:
        """
        admin_page.select_menu('耗材列表')
        consumable_list_page.query_consumable_list(name='打印纸')
        assert '打印纸' in consumable_list_page.read_table_cell_value(1, 2), '设施列表搜索失败'

    @pytest.mark.facilitylist
    @pytest.mark.run(order=211)
    def test_reset_query_consumable_list(self):
        """
        清除查询
        :return:
        """
        admin_page.select_menu('耗材列表')
        consumable_list_page.click_reset_query_button()
        assert consumable_list_page.read_query_name() == '', '重置耗材列表查询失败'

    @pytest.mark.facilitylist
    @pytest.mark.run(order=212)
    def test_view_consumable_detail(self):
        """
        查看耗材详情列表
        :return:
        """
        admin_page.select_menu('耗材列表')
        consumable_list_page.click_view_consumable_detail()
        assert consumable_list_page.check_current_menu('耗材详情列表'), '查看耗材详情列表失败'

    @pytest.fixture(scope='function')
    def close_open_print(self):
        """
        关闭打印界面
        :return:
        """
        yield 1
        consumable_list_page.close_print_view()

    @pytest.mark.facilitylist
    @pytest.mark.run(order=213)
    def test_print_consumable_list(self, close_open_print):
        """
        打印设施清单
        :return:
        """
        admin_page.select_menu('耗材列表')
        consumable_list_page.click_print_button()
        assert consumable_list_page.is_print_view(), '打印设施清单失败'