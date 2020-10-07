"""
考核列表
"""
import allure
import pytest

from src.pages.admin_page import AdminPage
from src.pages.business_manage.channel_performance.channel_assessment.assessment_list_page import AssessmentListPage

global assessment_list_page, admin_page


@pytest.mark.usefixtures('user_login')
@pytest.mark.usefixtures('init_browser')
@allure.story("考核列表")
class TestAssessmentList:

    @pytest.fixture(scope='function')
    def set_up(self):
        """
        前置操作
        :return:
        """
        global assessment_list_page, admin_page
        assessment_list_page = AssessmentListPage(self.driver)
        admin_page = AdminPage(self.driver)

        admin_page.into_subsystem('业务管理')
        admin_page.select_menu('首页/渠道绩效管理/渠道考核')

    @pytest.mark.assessment
    @pytest.mark.run(order=400)
    def test_query_assessment_list(self, set_up):
        """
        查询考核列表
        :return:
        """
        admin_page.select_menu('考核列表')
        assessment_list_page.query_assessment_list(id='460300')
        assert '460300' in assessment_list_page.read_table_cell_value(1, 2), '查询考核列表失败'

    @pytest.mark.assessment
    @pytest.mark.run(order=401)
    def test_reset_query_assessment_list(self):
        """
        重置查询考核列表
        :param set_up:
        :return:
        """
        admin_page.select_menu('考核列表')
        assessment_list_page.click_reset_query_button()
        assert assessment_list_page.read_query_id() == '', '重置查询考核列表失败'

    @pytest.mark.assessment
    @pytest.mark.run(order=402)
    def test_click_more_query_assessment_list(self):
        """
        展示更多查询条件
        :return:
        """
        admin_page.select_menu('考核列表')
        assessment_list_page.click_more_query()
        assert assessment_list_page.is_more_query(), '展示更多查询条件失败'

    @pytest.mark.assessment
    @pytest.mark.run(order=404)
    def test_click_view_assessment_detail(self):
        """
        查看考核详情
        :return:
        """
        admin_page.select_menu('考核列表')
        assessment_list_page.click_view_assessment_detail()
        assert assessment_list_page.check_current_menu('考核详情'), '查看考核详情失败'

    @pytest.fixture(scope='function')
    def close_open_alert(self):
        """
        关闭弹窗
        :return:
        """
        yield 1
        assessment_list_page.alert_close('定性考核-人工干预')

    @pytest.mark.assessment
    @pytest.mark.run(order=405)
    def test_click_manual_assessment(self, close_open_alert):
        """
        人工干预申诉详情
        :return:
        """
        admin_page.select_menu('考核列表')
        assessment_list_page.click_manual_assessment()
        assert assessment_list_page.check_alert_is_exist('定性考核-人工干预'), '人工干预申诉详情失败'