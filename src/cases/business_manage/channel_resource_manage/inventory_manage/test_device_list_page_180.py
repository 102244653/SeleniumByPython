""""
设备列表
"""

import allure
import pytest

from src.pages.admin_page import AdminPage
from src.pages.business_manage.channel_resource_manage.inventory_manage.device_list_page import DeviceListPage

global device_list_page, admin_page


@pytest.mark.usefixtures('user_login')
@pytest.mark.usefixtures('init_browser')
@allure.story("设备列表")
class TestDeviceList:

    @pytest.fixture(scope='function')
    def set_up(self):
        """
        前置操作
        :return:
        """
        global device_list_page, admin_page
        device_list_page = DeviceListPage(self.driver)
        admin_page = AdminPage(self.driver)

        admin_page.into_subsystem('业务管理')
        admin_page.select_menu('首页/渠道资源管理/库存管理')

    @pytest.mark.devicelist
    @pytest.mark.run(order=180)
    def test_query_device_list(self, set_up):
        """
        查寻设备类型
        1.输入类型名称：终端机
        【check_point】第一条结果名称选项包含：终端机
        :return:
        """
        admin_page.select_menu('S设备列表')
        device_list_page.query_device_list(name='终端机')
        assert '终端机' in device_list_page.read_table_cell_value(1, 2), '设备列表搜索失败'

    @pytest.mark.devicelist
    @pytest.mark.run(order=181)
    def test_reset_query_device_list(self):
        """
        清除查询
        :return:
        """
        admin_page.select_menu('S设备列表')
        device_list_page.click_reset_query_button()
        assert device_list_page.read_query_data('name') == '', '重置查询失败'

    @pytest.mark.devicelist
    @pytest.mark.run(order=182)
    def test_view_device_detail(self):
        """
        查看设备详情
        :return:
        """
        admin_page.select_menu('S设备列表')
        device_list_page.click_view_device_detail()
        assert device_list_page.check_current_menu('设备详情列表'), '查看设备详情失败'

    @pytest.fixture(scope='function')
    def close_open_print(self):
        """
        关闭打印界面
        :return:
        """
        yield 1
        device_list_page.close_print_view()

    @pytest.mark.devicelist
    @pytest.mark.run(order=183)
    def test_print_device_list(self, close_open_print):
        """
        打印设备清单
        :return:
        """
        admin_page.select_menu('S设备列表')
        device_list_page.click_print_button()
        assert device_list_page.is_print_view(), '打印设备清单失败'