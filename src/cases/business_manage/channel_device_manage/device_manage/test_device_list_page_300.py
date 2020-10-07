"""
设备列表
"""
import allure
import pytest

from src.pages.admin_page import AdminPage
from src.pages.business_manage.channel_device_manage.device_manage.device_list_page import DeviceListPage

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
        admin_page.select_menu('首页/渠道终端管理/设备管理')

    @pytest.mark.devicelist2
    @pytest.mark.run(order=300)
    def test_query_device_list(self, set_up):
        """
        查询设备列表
        """
        admin_page.select_menu('T设备列表')
        device_list_page.simple_query_device(store='房山区')
        assert '房山区' in device_list_page.read_table_cell_value(1, 3), '查询设备列表失败'

    @pytest.mark.devicelist2
    @pytest.mark.run(order=301)
    def test_reset_query_device_list(self):
        """
        重置查询设备列表
        """
        admin_page.select_menu('T设备列表')
        device_list_page.click_reset_query_button()
        assert device_list_page.read_query_store() == '', '重置查询设备列表失败'

    @pytest.mark.devicelist2
    @pytest.mark.run(order=302)
    def test_click_more_query_device_list(self):
        """
        显示更多查询
        """
        admin_page.select_menu('T设备列表')
        device_list_page.click_more_query()
        assert device_list_page.is_more_query(), '显示更多查询失败'

    @pytest.mark.devicelist2
    @pytest.mark.run(order=303)
    def test_view_device_record(self):
        """
        设备履历
        """
        admin_page.select_menu('T设备列表')
        device_list_page.click_view_device_record()
        assert device_list_page.check_current_menu('设备履历'), '查看设备履历失败'

    @pytest.mark.devicelist2
    @pytest.mark.run(order=304)
    def test_view_device_detail(self):
        """
        查看设备详情
        :return:
        """
        admin_page.select_menu('T设备列表')
        device_list_page.click_view_device_detail()
        assert device_list_page.check_current_menu('设备详情'), '查看设备详情失败'
