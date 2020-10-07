"""
配件损耗报表
"""

import allure
import pytest

from src.pages.admin_page import AdminPage
from src.pages.business_manage.channel_device_manage.report_manage.parts_loss_page import PartsLossPage

global parts_loss_page, admin_page


@pytest.mark.usefixtures('user_login')
@pytest.mark.usefixtures('init_browser')
@allure.story("配件损耗报表")
class TestDeviceFailure:

    @pytest.fixture(scope='function')
    def set_up(self):
        """
        前置操作
        :return:
        """
        global parts_loss_page, admin_page
        parts_loss_page = PartsLossPage(self.driver)
        admin_page = AdminPage(self.driver)

        admin_page.into_subsystem('业务管理')
        admin_page.select_menu('首页/渠道终端管理/报表统计')

    @pytest.mark.partsloss
    @pytest.mark.run(order=340)
    def test_query_parts_loss(self, set_up):
        """
        查询配件故障报表
        """
        admin_page.select_menu('配件损耗报表')
        parts_loss_page.simple_query_parts_loss(name='柜员机')
        assert '柜员机' in parts_loss_page.read_table_cell_value(1, 2), '查询配件损耗报表失败'

    @pytest.mark.partsloss
    @pytest.mark.run(order=341)
    def test_reset_query_parts_loss(self):
        """
        重置配件损耗报表
        """
        admin_page.select_menu('配件损耗报表')
        parts_loss_page.click_reset_query_button()
        assert parts_loss_page.read_query_name() == '', '重置查询配件损耗报表失败'

    @pytest.mark.partsloss
    @pytest.mark.run(order=342)
    def test_click_more_query_parts_loss(self):
        """
        显示更多查询
        """
        admin_page.select_menu('配件损耗报表')
        parts_loss_page.click_more_query()
        assert parts_loss_page.is_more_query(), '配件损耗报表显示更多查询失败'

    @pytest.fixture(scope='function')
    def close_print_window(self):
        """
        关闭打印窗口
        :return:
        """
        yield 1
        parts_loss_page.close_print_view()

    @pytest.mark.partsloss
    @pytest.mark.run(order=343)
    def test_click_print_parts_loss(self, close_print_window):
        """
        打印配件损耗报表
        """
        admin_page.select_menu('配件损耗报表')
        parts_loss_page.click_print_parts_loss()
        assert parts_loss_page.is_print_view(), '打印配件损耗报表失败'