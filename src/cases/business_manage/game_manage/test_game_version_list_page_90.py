import allure
import pytest

from src.pages.admin_page import AdminPage
from src.pages.business_manage.game_manage.game_version_list_page import GameVersionPage

global game_version_page, admin_page


@pytest.mark.usefixtures('user_login')
@pytest.mark.usefixtures('init_browser')
@allure.story("版本配置列表")
class TestGameVersion:

    @pytest.fixture(scope='function')
    def set_up(self):
        """
        前置操作
        :return:
        """
        global game_version_page, admin_page
        game_version_page = GameVersionPage(self.driver)
        admin_page = AdminPage(self.driver)

        admin_page.into_subsystem('业务管理')
        admin_page.select_menu('首页/游戏储备管理')

    @pytest.mark.gameversion
    @pytest.mark.run(order=90)
    def test_query_game_version(self, set_up):
        """
        查询游戏版本
        """
        admin_page.select_menu('版本配置列表')
        game_version_page.simple_query_version(name='深海探秘')
        assert '深海探秘' in game_version_page.read_table_cell_value(1, 3), '游戏查询失败'

    @pytest.mark.gameversion
    @pytest.mark.run(order=91)
    def test_reset_query(self):
        """
        重置查询
        """
        game_version_page.reset_query()
        assert game_version_page.read_query_name() == '', '查询条件重置失败'

    @pytest.mark.gameversion
    @pytest.mark.run(order=92)
    def test_click_more_query(self):
        """
        展示更多查询条件
        """
        admin_page.select_menu('版本配置列表')
        game_version_page.click_more_query()
        assert game_version_page.is_more_query(), '展示更多查询条件失败'

    @pytest.fixture(scope='function')
    def close_open_menu(self):
        """
        打开新建的菜单
        """
        yield 1
        game_version_page.close_current_menu()

    @pytest.mark.gameversion
    @pytest.mark.run(order=93)
    def test_open_creat_config(self, close_open_menu):
        """
        新建游戏弹窗
        """
        admin_page.select_menu('版本配置列表')
        game_version_page.click_add_config()
        assert game_version_page.check_current_menu('新建游戏版本'), '点击游戏配置未打开新界面'

    @pytest.mark.gameversion
    @pytest.mark.run(order=94)
    def test_view_config_detail(self, close_open_menu):
        """
        查看游戏详情
        """
        admin_page.select_menu('版本配置列表')
        game_version_page.view_config()
        assert game_version_page.check_current_menu('游戏版本详情'), '点击查看未打开新界面'

    @pytest.fixture(scope='function')
    def close_small_version(self):
        """
        后置操作
        """
        yield 1
        game_version_page.edit_small_version()

    @pytest.mark.gamestore
    @pytest.mark.run(order=95)
    def test_edit_version_detail(self, close_small_version):
        """
        编辑游戏版本界面
        """
        admin_page.select_menu('版本配置列表')
        game_version_page.view_config_version()
        assert game_version_page.check_alert_is_exist('配置最小版本号'), '点击编辑游戏未打开新界面'
