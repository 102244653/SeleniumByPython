"""
配件列表
"""

import allure
import pytest

from src.pages.admin_page import AdminPage
from src.pages.business_manage.channel_resource_manage.inventory_manage.parts_list_page import PartsListPage

global parts_list_page, admin_page


@pytest.mark.usefixtures('user_login')
@pytest.mark.usefixtures('init_browser')
@allure.story("配件列表")
class TestDeviceList:

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
        admin_page.select_menu('首页/渠道资源管理/库存管理')

    @pytest.mark.partslist
    @pytest.mark.run(order=190)
    def test_query_parts_list(self, set_up):
        """
        查寻配件列表
        1.输入类型名称：终端机
        【check_point】第一条结果名称选项包含：终端机
        :return:
        """
        admin_page.select_menu('配件列表')
        parts_list_page.query_parts_list(name='密码键盘')
        assert '密码键盘' in parts_list_page.read_table_cell_value(1, 2), '配件列表搜索失败'

    @pytest.mark.partslist
    @pytest.mark.run(order=191)
    def test_reset_query_device_list(self):
        """
        清除查询
        :return:
        """
        admin_page.select_menu('配件列表')
        parts_list_page.click_reset_query_button()
        assert parts_list_page.read_query_data('name') == '', '重置查询失败'

    @pytest.mark.partslist
    @pytest.mark.run(order=192)
    def test_view_device_detail(self):
        """
        查看设备详情
        :return:
        """
        admin_page.select_menu('配件列表')
        parts_list_page.click_view_parts_detail()
        assert parts_list_page.check_current_menu('配件详情列表'), '查看设备详情失败'

    @pytest.fixture(scope='function')
    def close_open_print(self):
        """
        关闭打印界面
        :return:
        """
        yield 1
        parts_list_page.close_print_view()

    @pytest.mark.partslist
    @pytest.mark.run(order=193)
    def test_print_device_list(self, close_open_print):
        """
        打印设备清单
        :return:
        """
        admin_page.select_menu('配件列表')
        parts_list_page.click_print_button()
        assert parts_list_page.is_print_view(), '打印设备清单失败'