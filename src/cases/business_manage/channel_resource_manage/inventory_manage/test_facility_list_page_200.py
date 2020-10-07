"""
设施列表
"""

import allure
import pytest

from src.pages.admin_page import AdminPage
from src.pages.business_manage.channel_resource_manage.inventory_manage.facility_list_page import FacilityListPage

global facility_list_page, admin_page


@pytest.mark.usefixtures('user_login')
@pytest.mark.usefixtures('init_browser')
@allure.story("设施列表")
class TestDeviceList:

    @pytest.fixture(scope='function')
    def set_up(self):
        """
        前置操作
        :return:
        """
        global facility_list_page, admin_page
        facility_list_page = FacilityListPage(self.driver)
        admin_page = AdminPage(self.driver)

        admin_page.into_subsystem('业务管理')
        admin_page.select_menu('首页/渠道资源管理/库存管理')

    @pytest.mark.facilitylist
    @pytest.mark.run(order=200)
    def test_query_facility_list(self, set_up):
        """
        查寻配件列表
        1.输入类型名称：终端机
        【check_point】第一条结果名称选项包含：终端机
        :return:
        """
        admin_page.select_menu('设施列表')
        facility_list_page.query_parts_list(name='椅子')
        assert '椅子' in facility_list_page.read_table_cell_value(1, 2), '设施列表搜索失败'

    @pytest.mark.facilitylist
    @pytest.mark.run(order=201)
    def test_reset_query_facility_list(self):
        """
        清除查询
        :return:
        """
        admin_page.select_menu('设施列表')
        facility_list_page.click_reset_query_button()
        assert facility_list_page.read_query_name() == '', '重置设施列表查询失败'

    @pytest.mark.facilitylist
    @pytest.mark.run(order=202)
    def test_view_facility_detail(self):
        """
        查看设施详情
        :return:
        """
        admin_page.select_menu('设施列表')
        facility_list_page.click_view_facility_detail()
        assert facility_list_page.check_current_menu('设施详情列表'), '查看设施列表详情失败'

    @pytest.fixture(scope='function')
    def close_open_print(self):
        """
        关闭打印界面
        :return:
        """
        yield 1
        facility_list_page.close_print_view()

    @pytest.mark.facilitylist
    @pytest.mark.run(order=203)
    def test_print_facility_list(self, close_open_print):
        """
        打印设施清单
        :return:
        """
        admin_page.select_menu('设施列表')
        facility_list_page.click_print_button()
        assert facility_list_page.is_print_view(), '打印设施清单失败'