"""
类型管理
"""


import allure
import pytest

from src.pages.admin_page import AdminPage
from src.pages.business_manage.channel_resource_manage.basic_info_manage.type_manage_page import TypeManagePage

global type_manage_page, admin_page


@pytest.mark.usefixtures('user_login')
@pytest.mark.usefixtures('init_browser')
@allure.story("类型管理")
class TestTypeManage:

    @pytest.fixture(scope='function')
    def set_up(self):
        """
        前置操作
        :return:
        """
        global type_manage_page, admin_page
        type_manage_page = TypeManagePage(self.driver)
        admin_page = AdminPage(self.driver)

        admin_page.into_subsystem('业务管理')
        admin_page.select_menu('首页/渠道资源管理/基本信息管理')

    @pytest.mark.typemanage
    @pytest.mark.run(order=240)
    def test_query_type_manage(self, set_up):
        """
        类型管理查询
        :return:
        """
        admin_page.select_menu('类型管理')
        type_manage_page.simple_query_type(_type='设备')
        assert type_manage_page.read_table_cell_value(1, 2), '类型管理查询失败'

    @pytest.mark.typemanage
    @pytest.mark.run(order=241)
    def test_reset_query_type_manage(self):
        """
        重置查询
        :return:
        """
        admin_page.select_menu('类型管理')
        type_manage_page.click_reset_query_button()
        assert type_manage_page.read_query_type() == '', '重置查询失败'

    @pytest.mark.typemanage
    @pytest.mark.run(order=242)
    def test_click_more_query(self):
        """
        显示更多查询
        :return:
        """
        admin_page.select_menu('类型管理')
        type_manage_page.click_more_query()
        assert type_manage_page.is_more_query(), '显示更多查询失败'

    @pytest.mark.typemanage
    @pytest.mark.run(order=243)
    def test_click_create_type(self):
        """
        点击新增类型
        :return:
        """
        admin_page.select_menu('类型管理')
        type_manage_page.click_create_type()
        assert type_manage_page.check_current_menu('新增类型'), '点击新增类型失败'

    @pytest.mark.typemanage
    @pytest.mark.run(order=244)
    def test_click_on_off_type(self):
        """
        点击新增类型启用开关
        :return:
        """
        admin_page.select_menu('类型管理')
        type_manage_page.click_on_off_btn()
        assert '状态修改成功' in type_manage_page.read_toast(), '点击新增类型启用开关失败'

    @pytest.mark.typemanage
    @pytest.mark.run(order=245)
    def test_view_type_detail(self):
        """
        查看类型详情
        :return:
        """
        admin_page.select_menu('类型管理')
        type_manage_page.view_type_detail()
        assert type_manage_page.check_current_menu('设备详情'), '查看类型详情失败'
