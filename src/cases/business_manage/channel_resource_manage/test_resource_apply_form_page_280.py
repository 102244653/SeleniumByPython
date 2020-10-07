"""
资源申请管理
"""


import allure
import pytest

from src.pages.admin_page import AdminPage
from src.pages.business_manage.channel_resource_manage.resource_apply_form_page import ResourceApplyFormPage

global resource_apply_page, admin_page


@pytest.mark.usefixtures('user_login')
@pytest.mark.usefixtures('init_browser')
@allure.story("资源申请单")
class TestStoreManage:

    @pytest.fixture(scope='function')
    def set_up(self):
        """
        前置操作
        :return:
        """
        global resource_apply_page, admin_page
        resource_apply_page = ResourceApplyFormPage(self.driver)
        admin_page = AdminPage(self.driver)

        admin_page.into_subsystem('业务管理')
        admin_page.select_menu('首页/渠道资源管理')

    @pytest.mark.ledgermanage
    @pytest.mark.run(order=280)
    def test_query_resource_apply(self, set_up):
        """
        查询资源申请列表
        :return:
        """
        admin_page.select_menu('资源申请单')
        resource_apply_page.simple_query_resource(name='四川')
        assert '四川' in resource_apply_page.read_table_cell_value(1, 4), '查询资源申请列表失败'

    @pytest.mark.ledgermanage
    @pytest.mark.run(order=281)
    def test_reset_query_resource_apply(self):
        """
        重置查询资源申请
        :return:
        """
        admin_page.select_menu('资源申请单')
        resource_apply_page.click_reset_query_button()
        assert resource_apply_page.read_query_name() == '', '查询资源申请失败'

    @pytest.mark.ledgermanage
    @pytest.mark.run(order=282)
    def test_more_query_resource_apply(self):
        """
        显示更多查询
        :return:
        """
        admin_page.select_menu('资源申请单')
        resource_apply_page.click_more_query()
        assert resource_apply_page.is_more_query(), '显示更多查询失败'


