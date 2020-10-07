"""
台账管理
"""

import allure
import pytest

from src.pages.admin_page import AdminPage
from src.pages.business_manage.channel_resource_manage.ledger_manage_page import LedgerManagePage

global ledger_manage_page, admin_page


@pytest.mark.usefixtures('user_login')
@pytest.mark.usefixtures('init_browser')
@allure.story("台账管理")
class TestStoreManage:

    @pytest.fixture(scope='function')
    def set_up(self):
        """
        前置操作
        :return:
        """
        global ledger_manage_page, admin_page
        ledger_manage_page = LedgerManagePage(self.driver)
        admin_page = AdminPage(self.driver)

        admin_page.into_subsystem('业务管理')
        admin_page.select_menu('首页/渠道资源管理')

    @pytest.mark.ledgermanage
    @pytest.mark.run(order=260)
    def test_query_ledger_manage(self, set_up):
        """
        查询台账管理列表
        :return:
        """
        admin_page.select_menu('台账管理')
        ledger_manage_page.simple_query_ledger(name='中福彩中心仓库')
        assert '中福彩中心仓库' in ledger_manage_page.read_table_cell_value(1, 2), '查询台账管理列表失败'

    @pytest.mark.ledgermanage
    @pytest.mark.run(order=261)
    def test_reset_query_ledger_manage(self):
        """
        重置查询台账管理列表
        :return:
        """
        admin_page.select_menu('台账管理')
        ledger_manage_page.click_reset_query_button()
        assert ledger_manage_page.read_query_name() == '', '重置查询台账管理列表失败'

    @pytest.mark.ledgermanage
    @pytest.mark.run(order=262)
    def test_more_query_ledger_manage(self):
        """
        显示更多查询
        :return:
        """
        admin_page.select_menu('台账管理')
        ledger_manage_page.click_more_query()
        assert ledger_manage_page.is_more_query(), '显示更多查询失败'

    @pytest.mark.ledgermanage
    @pytest.mark.run(order=263)
    def test_view_ledger_detail(self):
        """
        查看台账详情
        :return:
        """
        admin_page.select_menu('台账管理')
        ledger_manage_page.click_view_ledger_detail()
        assert ledger_manage_page.check_current_menu('台账明细'), '查看台账明细失败'

