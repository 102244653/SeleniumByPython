"""
配件列表
"""

import allure
import pytest

from src.pages.admin_page import AdminPage
from src.pages.business_manage.channel_device_manage.device_manage.parts_list_page import PartsListPage

global parts_list_page, admin_page


@pytest.mark.usefixtures('user_login')
@pytest.mark.usefixtures('init_browser')
@allure.story("配件管理")
class TestPartsList:

    @pytest.fixture(scope='function')
    def set_up(self):
        """
        前置操作
        :return:
        """
        global parts_list_page, admin_page
        parts_list_page = PartsListPage(self.driver)
        admin_page = AdminPage(self.driver)

        admin_page.into_subsystem('业务管理')
        admin_page.select_menu('首页/渠道终端管理/设备管理')

    @pytest.mark.partslist
    @pytest.mark.run(order=310)
    def test_query_parts_list(self, set_up):
        """
        查询配件列表
        """
        admin_page.select_menu('T配件列表')
        parts_list_page.simple_query_parts(store='海南省')
        assert '海南省' in parts_list_page.read_table_cell_value(1, 3), '查询配件列表失败'

    @pytest.mark.partslist
    @pytest.mark.run(order=311)
    def test_reset_query_parts_list(self):
        """
        重置查询配件列表
        """
        admin_page.select_menu('T配件列表')
        parts_list_page.click_reset_query_button()
        assert parts_list_page.read_query_store() == '', '重置查询配件列表失败'

    @pytest.mark.partslist
    @pytest.mark.run(order=312)
    def test_click_more_query_parts_list(self):
        """
        显示更多查询
        """
        admin_page.select_menu('T配件列表')
        parts_list_page.click_more_query()
        assert parts_list_page.is_more_query(), '显示更多查询失败'

    @pytest.mark.partslist
    @pytest.mark.run(order=313)
    def test_view_parts_record(self):
        """
        配件履历
        """
        admin_page.select_menu('T配件列表')
        parts_list_page.click_view_parts_record()
        assert parts_list_page.check_current_menu('配件履历'), '查看配件履历失败'

    @pytest.mark.partslist
    @pytest.mark.run(order=314)
    def test_view_parts_detail(self):
        """
        查看配件详情
        :return:
        """
        admin_page.select_menu('T配件列表')
        parts_list_page.click_view_parts_detail()
        assert parts_list_page.check_current_menu('配件详情'), '查看配件详情失败'
