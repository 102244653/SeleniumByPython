"""
型号管理
"""

import allure
import pytest

from src.pages.admin_page import AdminPage
from src.pages.business_manage.channel_resource_manage.basic_info_manage.model_manage_page import ModelManagePage

global model_manage_page, admin_page


@pytest.mark.usefixtures('user_login')
@pytest.mark.usefixtures('init_browser')
@allure.story("型号管理")
class TestModelManage:

    @pytest.fixture(scope='function')
    def set_up(self):
        """
        前置操作
        :return:
        """
        global model_manage_page, admin_page
        model_manage_page = ModelManagePage(self.driver)
        admin_page = AdminPage(self.driver)

        admin_page.into_subsystem('业务管理')
        admin_page.select_menu('首页/渠道资源管理/基本信息管理')

    @pytest.mark.modelmanage
    @pytest.mark.run(order=250)
    def test_query_model_manage(self, set_up):
        """
        型号管理查询
        :return:
        """
        admin_page.select_menu('型号管理')
        model_manage_page.simple_query_model_manage(_type='设备')
        assert model_manage_page.read_table_cell_value(1, 2), '型号管理查询失败'

    @pytest.mark.modelmanage
    @pytest.mark.run(order=251)
    def test_reset_query_model_manage(self):
        """
        重置查询
        :return:
        """
        admin_page.select_menu('型号管理')
        model_manage_page.click_reset_query_button()
        assert model_manage_page.read_query_type() == '', '重置查询失败'

    @pytest.mark.modelmanage
    @pytest.mark.run(order=252)
    def test_click_more_query(self):
        """
        显示更多查询
        :return:
        """
        admin_page.select_menu('型号管理')
        model_manage_page.click_more_query()
        assert model_manage_page.is_more_query(), '显示更多查询失败'

    @pytest.mark.modelmanage
    @pytest.mark.run(order=253)
    def test_click_create_model(self):
        """
        点击新增型号
        :return:
        """
        admin_page.select_menu('型号管理')
        model_manage_page.click_create_model()
        assert model_manage_page.check_current_menu('新增型号'), '点击新增型号失败'

    @pytest.mark.modelmanage
    @pytest.mark.run(order=254)
    def test_click_on_off_type(self):
        """
        点击新增型号启用开关
        :return:
        """
        admin_page.select_menu('型号管理')
        model_manage_page.click_on_off_btn()
        assert '状态修改成功' in model_manage_page.read_toast(), '点击新增型号启用开关失败'

    @pytest.mark.modelmanage
    @pytest.mark.run(order=255)
    def test_view_model_detail(self):
        """
        查看型号详情
        :return:
        """
        admin_page.select_menu('型号管理')
        model_manage_page.view_model_detail()
        assert model_manage_page.check_current_menu('设备详情'), '查看型号详情失败'