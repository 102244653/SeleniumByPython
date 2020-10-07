"""
仓库管理
"""

import allure
import pytest

from src.pages.admin_page import AdminPage
from src.pages.business_manage.channel_resource_manage.store_manage_page import StoreManagePage

global store_manage_page, admin_page


@pytest.mark.usefixtures('user_login')
@pytest.mark.usefixtures('init_browser')
@allure.story("仓库管理")
class TestStoreManage:

    @pytest.fixture(scope='function')
    def set_up(self):
        """
        前置操作
        :return:
        """
        global store_manage_page, admin_page
        store_manage_page = StoreManagePage(self.driver)
        admin_page = AdminPage(self.driver)

        admin_page.into_subsystem('业务管理')
        admin_page.select_menu('首页/渠道资源管理')

    @pytest.mark.storemanage
    @pytest.mark.run(order=270)
    def test_query_store_manage(self, set_up):
        """
        查询仓库管理列表
        :return:
        """
        admin_page.select_menu('仓库管理')
        store_manage_page.simple_query_store(name='四川省')
        assert '四川省' in store_manage_page.read_table_cell_value(1, 2), '查询仓库管理列表失败'

    @pytest.mark.storemanage
    @pytest.mark.run(order=271)
    def test_reset_query_store_manage(self):
        """
        重置查询仓库管理列表
        :return:
        """
        admin_page.select_menu('仓库管理')
        store_manage_page.click_reset_query_button()
        assert store_manage_page.read_query_name() == '', '重置查询条件失败'

    @pytest.mark.storemanage
    @pytest.mark.run(order=272)
    def test_more_query_store_manage(self):
        """
        显示更多查询
        :return:
        """
        admin_page.select_menu('仓库管理')
        store_manage_page.click_more_query()
        assert store_manage_page.is_more_query(), '显示更多查询失败'

    @pytest.mark.storemanage
    @pytest.mark.run(order=273)
    def test_view_store_detail(self):
        """
        查看仓库详情
        :return:
        """
        admin_page.select_menu('仓库管理')
        store_manage_page.click_view_store_detail()
        assert store_manage_page.check_current_menu('仓库详情'), '显示仓库详情失败'

