"""
设备损耗报表
"""

import allure
import pytest

from src.pages.admin_page import AdminPage
from src.pages.business_manage.channel_device_manage.report_manage.device_loss_page import DeviceLossPage

global device_loss_page, admin_page


@pytest.mark.usefixtures('user_login')
@pytest.mark.usefixtures('init_browser')
@allure.story("设备损耗报表")
class TestDeviceLoss:

    @pytest.fixture(scope='function')
    def set_up(self):
        """
        前置操作
        :return:
        """
        global device_loss_page, admin_page
        device_loss_page = DeviceLossPage(self.driver)
        admin_page = AdminPage(self.driver)

        admin_page.into_subsystem('业务管理')
        admin_page.select_menu('首页/渠道终端管理/报表统计')

    @pytest.mark.deviceloss
    @pytest.mark.run(order=320)
    def test_query_device_loss(self, set_up):
        """
        查询设备损耗报表
        """
        admin_page.select_menu('设备损耗报表')
        device_loss_page.simple_query_device_loss(name='柜员机')
        assert '柜员机' in device_loss_page.read_table_cell_value(1, 2), '查询设备损耗报表失败'

    @pytest.mark.deviceloss
    @pytest.mark.run(order=321)
    def test_reset_query_device_loss(self):
        """
        重置设备损耗报表
        """
        admin_page.select_menu('设备损耗报表')
        device_loss_page.click_reset_query_button()
        assert device_loss_page.read_query_name() == '', '重置查询设备损耗报表失败'

    @pytest.mark.deviceloss
    @pytest.mark.run(order=322)
    def test_click_more_query_device_loss(self):
        """
        显示更多查询
        """
        admin_page.select_menu('设备损耗报表')
        device_loss_page.click_more_query()
        assert device_loss_page.is_more_query(), '设备损耗报表显示更多查询失败'

    @pytest.fixture(scope='function')
    def close_print_window(self):
        """
        关闭打印窗口
        :return:
        """
        yield 1
        device_loss_page.close_print_view()

    @pytest.mark.deviceloss
    @pytest.mark.run(order=323)
    def test_click_print_device_loss(self, close_print_window):
        """
        打印设备损耗报表
        """
        admin_page.select_menu('设备损耗报表')
        device_loss_page.click_print_device_loss()
        assert device_loss_page.is_print_view(), '打印设备损耗报表失败'