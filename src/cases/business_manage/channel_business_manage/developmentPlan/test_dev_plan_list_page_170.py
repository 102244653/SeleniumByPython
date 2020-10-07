import allure
import pytest

from src.pages.admin_page import AdminPage
from src.pages.business_manage.channel_business_manage.developmentPlan.dev_plan_list_page import DevPlanListPage

global dev_plan_list_page, admin_page


@pytest.mark.usefixtures('user_login')
@pytest.mark.usefixtures('init_browser')
@allure.story("计划列表")
class TestDevPlanList:

    @pytest.fixture(scope='function')
    def set_up(self):
        """
        前置操作
        :return:
        """
        global dev_plan_list_page, admin_page
        dev_plan_list_page = DevPlanListPage(self.driver)
        admin_page = AdminPage(self.driver)

        admin_page.into_subsystem('业务管理')
        admin_page.select_menu('首页/渠道业务管理/年度发展计划')

    @pytest.mark.devplan
    @pytest.mark.run(order=170)
    def test_query_dev_plan(self, set_up):
        """
        年度计划查询
        :return:
        """
        admin_page.select_menu('计划列表')
        dev_plan_list_page.query_by_year(_year='2020')
        assert '2020' in dev_plan_list_page.read_table_cell_value(1, 3), '年度计划查询失败'

    @pytest.mark.devplan
    @pytest.mark.run(order=171)
    def test_reset_dev_plan_query(self):
        """
        重置年度计划查询
        :return:
        """
        admin_page.select_menu('计划列表')
        dev_plan_list_page.reset_query()
        assert dev_plan_list_page.read_query_year() == '', '重置年度计划查询条件失败'

    @pytest.mark.devplan
    @pytest.mark.run(order=172)
    def test_click_create_dev_plan(self):
        """
        查看市级计划
        :return:
        """
        admin_page.select_menu('计划列表')
        dev_plan_list_page.click_create_dev_plan()
        assert dev_plan_list_page.check_current_menu('新建年度发展计划'), '点击新建年度发展计划失败'

    @pytest.mark.devplan
    @pytest.mark.run(order=173)
    def test_view_shi_plan_list(self):
        """
        查看市级计划
        :return:
        """
        admin_page.select_menu('计划列表')
        dev_plan_list_page.click_shi_plan_btn()
        assert dev_plan_list_page.check_current_menu('市级计划列表'), '点击查看渠道管市级计划列表详情失败'

    @pytest.mark.devplan
    @pytest.mark.run(order=174)
    def test_view_shi_plan_detail(self):
        """
        查看市级计划
        :return:
        """
        admin_page.select_menu('计划列表')
        dev_plan_list_page.click_view_plan_btn()
        assert dev_plan_list_page.check_current_menu('年度发展计划详情'), '点击查看年度发展计划详情失败'

