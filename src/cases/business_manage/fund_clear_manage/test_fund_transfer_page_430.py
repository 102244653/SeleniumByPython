"""
资金划拨管理
"""

import allure
import pytest

from src.pages.admin_page import AdminPage
from src.pages.business_manage.fund_clear_manage.fund_transfer_page import FundTransferPage

global fund_transfer_page, admin_page


@pytest.mark.usefixtures('user_login')
@pytest.mark.usefixtures('init_browser')
@allure.story("资金划拨管理")
class TestFundTransfer:

    @pytest.fixture(scope='function')
    def set_up(self):
        """
        前置操作
        :return:
        """
        global fund_transfer_page, admin_page
        fund_transfer_page = FundTransferPage(self.driver)
        admin_page = AdminPage(self.driver)

        admin_page.into_subsystem('业务管理')
        admin_page.select_menu('首页/资金结算管理')

    @pytest.mark.fundtransfer
    @pytest.mark.run(order=430)
    def test_click_create_fund_transfer(self, set_up):
        """
        新增资金划拨管理
        :return:
        """
        admin_page.select_menu('资金划拨管理')
        fund_transfer_page.click_create_btn()
        assert fund_transfer_page.check_current_menu('新增游戏资金划拨'), '新增资金划拨管理失败'

    @pytest.mark.fundtransfer
    @pytest.mark.run(order=431)
    def test_view_fund_transfer_detail(self):
        """
        查看游戏资金划拨详情
        :return:
        """
        admin_page.select_menu('资金划拨管理')
        fund_transfer_page.click_view_btn()
        assert fund_transfer_page.check_current_menu('资金划拨管理'), '查看游戏资金划拨详情失败'

    @pytest.fixture(scope='function')
    def close_open_alert(self):
        """
        关闭弹窗
        :return:
        """
        fund_transfer_page.alert_cancel('自动划拨')

    @pytest.mark.fundtransfer
    @pytest.mark.run(order=432)
    def test_click_on_off_fund_transfer(self, close_open_alert):
        """
        点击启用、关闭按钮
        :return:
        """
        admin_page.select_menu('资金划拨管理')
        fund_transfer_page.click_on_off_btn()
        assert fund_transfer_page.check_alert_is_exist('自动划拨'), '点击启用、关闭按钮失败'