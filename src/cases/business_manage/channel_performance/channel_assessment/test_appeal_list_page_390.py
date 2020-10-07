"""
申诉列表
"""


import allure
import pytest

from src.pages.admin_page import AdminPage
from src.pages.business_manage.channel_performance.channel_assessment.appeal_list_page import AppealListPage

global appeal_list_page, admin_page


@pytest.mark.usefixtures('user_login')
@pytest.mark.usefixtures('init_browser')
@allure.story("申诉列表")
class TestappealList:

    @pytest.fixture(scope='function')
    def set_up(self):
        """
        前置操作
        :return:
        """
        global appeal_list_page, admin_page
        appeal_list_page = AppealListPage(self.driver)
        admin_page = AdminPage(self.driver)

        admin_page.into_subsystem('业务管理')
        admin_page.select_menu('首页/渠道绩效管理/渠道考核')

    @pytest.mark.appeal
    @pytest.mark.run(order=390)
    def test_query_appeal_list_(self, set_up):
        """
        查询申诉列表
        :return:
        """
        admin_page.select_menu('申诉列表')
        appeal_list_page.query_appeal_list(phone='13511111111')
        assert '13511111111' in appeal_list_page.read_table_cell_value(1, 3), '查询申诉列表失败'

    @pytest.mark.appeal
    @pytest.mark.run(order=391)
    def test_reset_query_appeal_list_(self):
        """
        重置查询申诉列表
        :param set_up:
        :return:
        """
        admin_page.select_menu('申诉列表')
        appeal_list_page.click_reset_query_button()
        assert appeal_list_page.read_query_phone() == '', '重置查询申诉列表失败'

    @pytest.mark.appeal
    @pytest.mark.run(order=392)
    def test_click_more_query_appeal_list_(self):
        """
        展示更多查询条件
        :return:
        """
        admin_page.select_menu('申诉列表')
        appeal_list_page.click_more_query()
        assert appeal_list_page.is_more_query(), '展示更多查询条件失败'

    @pytest.mark.appeal
    @pytest.mark.run(order=394)
    def test_click_view_appeal_detail(self):
        """
        查看申诉详情
        :return:
        """
        admin_page.select_menu('申诉列表')
        appeal_list_page.click_view_appeal_list()
        assert appeal_list_page.check_current_menu('申诉详情'), '查看申诉详情失败'


