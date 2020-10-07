import allure
import pytest

from src.pages.admin_page import AdminPage
from src.pages.business_manage.game_manage.game_store_list_page import GameStorePage

global game_store_page, admin_page


@pytest.mark.usefixtures('user_login')
@pytest.mark.usefixtures('init_browser')
@allure.story("游戏储备列表")
class TestGameStore:

    @pytest.fixture(scope='function')
    def set_up(self):
        """
        前置操作
        :return:
        """
        global game_store_page, admin_page
        game_store_page = GameStorePage(self.driver)
        admin_page = AdminPage(self.driver)

        admin_page.into_subsystem('业务管理')
        admin_page.select_menu('首页/游戏储备管理')

    @pytest.mark.gamestore
    @pytest.mark.run(order=80)
    def test_query_store(self, set_up):
        """
        游戏查询
        1.输入游戏名称： 深海探秘
        【check_point】第一条数据的结果为：深海探秘
        """
        admin_page.select_menu('游戏储备列表')
        game_store_page.simple_query_store(name='深海探秘')
        assert '深海探秘' in game_store_page.read_table_cell_value(1, 3), '游戏查询失败'

    @pytest.mark.gamestore
    @pytest.mark.run(order=81)
    def test_reset_query(self):
        """
        重置查询
        """
        game_store_page.reset_query()
        assert game_store_page.read_query_name() == '', '查询条件重置失败'

    @pytest.mark.gamestore
    @pytest.mark.run(order=82)
    def test_click_more_query(self):
        """
        展示更多查询条件
        """
        admin_page.select_menu('游戏储备列表')
        game_store_page.click_more_query()
        assert game_store_page.is_more_query(), '展示更多查询条件失败'

    @pytest.fixture(scope='function')
    def close_open_menu(self):
        """
        打开新建的菜单
        """
        yield 1
        game_store_page.close_current_menu()

    @pytest.mark.gamestore
    @pytest.mark.run(order=83)
    def test_open_creat_new_game(self, close_open_menu):
        """
        新建游戏弹窗
        """
        admin_page.select_menu('游戏储备列表')
        game_store_page.click_creat_game()
        assert game_store_page.check_current_menu('新建游戏'), '点击创建游戏未打开新界面'

    @pytest.mark.gamestore
    @pytest.mark.run(order=84)
    def test_view_game_detail(self, close_open_menu):
        """
        查看游戏详情
        """
        admin_page.select_menu('游戏储备列表')
        game_store_page.click_view_game()
        assert game_store_page.check_current_menu('游戏详情'), '点击创建游戏未打开新界面'

    @pytest.mark.gamestore
    @pytest.mark.run(order=85)
    def test_edit_game_detail(self, close_open_menu):
        """
        编辑游戏界面
        """
        admin_page.select_menu('游戏储备列表')
        game_store_page.click_edit_btn()
        assert game_store_page.check_current_menu('编辑游戏'), '点击编辑游戏未打开新界面'