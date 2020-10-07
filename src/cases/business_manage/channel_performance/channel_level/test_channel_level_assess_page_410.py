"""
渠道等级考核
"""


import allure
import pytest

from src.pages.admin_page import AdminPage
from src.pages.business_manage.channel_performance.channel_level.channel_level_assess_page import LevelAssessPage

global level_assess_page, admin_page


@pytest.mark.usefixtures('user_login')
@pytest.mark.usefixtures('init_browser')
@allure.story("等级考核")
class TestLevelAssess:

    @pytest.fixture(scope='function')
    def set_up(self):
        """
        前置操作
        :return:
        """
        global level_assess_page, admin_page
        level_assess_page = LevelAssessPage(self.driver)
        admin_page = AdminPage(self.driver)

        admin_page.into_subsystem('业务管理')
        admin_page.select_menu('首页/渠道绩效管理/渠道等级')

    @pytest.mark.levelassess
    @pytest.mark.run(order=410)
    def test_query_level_assess(self, set_up):
        """
        查询等级考核
        :return:
        """
        admin_page.select_menu('等级考核')
        level_assess_page.query_level_assess(id='830000')
        assert '830000' in level_assess_page.read_table_cell_value(1, 2), '查询等级考核失败'

    @pytest.mark.levelassess
    @pytest.mark.run(order=411)
    def test_click_more_query_level_assess(self):
        """
        展示更多查询条件
        :return:
        """
        admin_page.select_menu('等级考核')
        level_assess_page.click_more_query()
        assert level_assess_page.is_more_query(), '展示更多查询条件失败'

    @pytest.mark.levelassess
    @pytest.mark.run(order=412)
    def test_click_view_level_detail(self):
        """
        查看等级考核
        :return:
        """
        admin_page.select_menu('等级考核')
        level_assess_page.click_view_level_assess_detail()
        assert level_assess_page.check_current_menu('渠道等级考核详情'), '查看等级考核详情失败'