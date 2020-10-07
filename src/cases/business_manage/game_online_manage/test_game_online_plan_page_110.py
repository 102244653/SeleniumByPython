import allure
import pytest

from src.pages.admin_page import AdminPage
from src.pages.business_manage.game_online_manage.game_online_plan_page import GameOnlinePlanPage

global game_online_plan_page, admin_page


@pytest.mark.usefixtures('user_login')
@pytest.mark.usefixtures('init_browser')
@allure.story("游戏上市计划")
class TestGameOnlinePlan:

    @pytest.fixture(scope='function')
    def set_up(self):
        """
        前置操作
        :return:
        """
        global game_online_plan_page, admin_page
        game_online_plan_page = GameOnlinePlanPage(self.driver)
        admin_page = AdminPage(self.driver)

        admin_page.into_subsystem('业务管理')
        admin_page.select_menu('首页/游戏发行管理')

    @pytest.mark.onlineplan
    @pytest.mark.run(order=110)
    def test_query_online_plan(self, set_up):
        """
        查询上市计划
        """
        admin_page.select_menu('游戏上市计划')
        game_online_plan_page.simple_query_play_plan(game_name='深海探秘')
        assert '深海探秘' in game_online_plan_page.read_table_cell_value(1, 3), '查询退市计划失败'

    @pytest.mark.onlineplan
    @pytest.mark.run(order=111)
    def test_reset_online_query(self):
        """
        重置试玩计划
        """
        admin_page.select_menu('游戏上市计划')
        game_online_plan_page.reset_query()
        assert game_online_plan_page.read_query_game_name() == '', '重置查询失败'

    @pytest.mark.onlineplan
    @pytest.mark.run(order=112)
    def test_more_online_query(self):
        """
        更多查询条件
        """
        admin_page.select_menu('游戏上市计划')
        game_online_plan_page.click_more_query()
        assert game_online_plan_page.is_more_query(), '点击 展开 显示更多查询条件失败'

    @pytest.fixture(scope='function')
    def close_open_menu(self):
        """
        关闭打开的菜单
        """
        yield 1
        game_online_plan_page.close_current_menu()

    @pytest.mark.onlineplan
    @pytest.mark.run(order=113)
    def test_click_creat_online_plan(self, close_open_menu):
        """
        点击新增上市计划
        """
        admin_page.select_menu('游戏上市计划')
        game_online_plan_page.click_creat_online_plan()
        assert game_online_plan_page.check_current_menu('新建上市计划'), '打开新建上市计划页面失败'

    @pytest.mark.onlineplan
    @pytest.mark.run(order=114)
    def test_view_online_plan(self):
        """
        查看上市计划
        """
        admin_page.select_menu('游戏上市计划')
        game_online_plan_page.view_online_plan()
        assert game_online_plan_page.check_current_menu('上市计划详情'), '查看上市计划详情失败'