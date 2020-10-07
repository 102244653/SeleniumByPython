"""
全局参数管理
"""

import allure
import pytest

from src.pages.admin_page import AdminPage
from src.pages.business_manage.fund_clear_manage.fund_config_page import FundConfigPage

global fund_config_page, admin_page


@pytest.mark.usefixtures('user_login')
@pytest.mark.usefixtures('init_browser')
@allure.story("全局参数管理")
class TestFundConfig:

    @pytest.fixture(scope='function')
    def set_up(self):
        """
        前置操作
        :return:
        """
        global fund_config_page, admin_page
        fund_config_page = FundConfigPage(self.driver)
        admin_page = AdminPage(self.driver)

        admin_page.into_subsystem('业务管理')
        admin_page.select_menu('首页/资金结算管理')

    @pytest.mark.fundconfig
    @pytest.mark.run(order=450)
    def test_query_fund_config(self, set_up):
        """
        全局参数管理列表查询
        :return:
        """
        admin_page.select_menu('全局参数管理')
        fund_config_page.query_fund_config(name='兑奖提醒天数')
        assert '兑奖提醒天数' in fund_config_page.read_table_cell_value(1, 3), '全局参数管理列表查询失败'

    @pytest.fixture(scope='function')
    def close_open_alert(self):
        """
        关闭弹窗
        :return:
        """
        yield 1
        fund_config_page.alert_cancel('提示')

    @pytest.mark.fundconfig
    @pytest.mark.run(order=451)
    def test_click_on_off_fund_config(self, close_open_alert):
        """
        点击启用、关闭按钮
        :return:
        """
        admin_page.select_menu('全局参数管理')
        fund_config_page.click_on_off_fund()
        assert fund_config_page.check_alert_is_exist('提示'), '点击启用、关闭按钮失败'

    @pytest.mark.fundconfig
    @pytest.mark.run(order=452)
    def test_view_fund_config_detail(self):
        """
        查看全局参数管理
        :return:
        """
        admin_page.select_menu('全局参数管理')
        fund_config_page.click_view_fund_detail()
        assert fund_config_page.check_current_menu('全局参数详情'), '查看全局参数管理失败'

    @pytest.mark.fundconfig
    @pytest.mark.run(order=452)
    def test_edit_fund_config(self):
        """
        编辑全局参数管理
        :return:
        """
        admin_page.select_menu('全局参数管理')
        fund_config_page.click_edit_fund_config()
        assert fund_config_page.check_current_menu('编辑全局参数'), '编辑全局参数管理失败'