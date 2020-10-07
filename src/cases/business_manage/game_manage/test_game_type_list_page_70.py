import allure
import pytest

from src.pages.admin_page import AdminPage
from src.pages.business_manage.game_manage.game_type_list_page import GameTypePage

global game_type_page, admin_page


@pytest.mark.usefixtures('user_login')
@pytest.mark.usefixtures('init_browser')
@allure.story("游戏类型列表")
class TestGameType:

    @pytest.fixture(scope='function')
    def set_up(self):
        """
        前置操作
        :return:
        """
        global game_type_page, admin_page
        game_type_page = GameTypePage(self.driver)
        admin_page = AdminPage(self.driver)

        admin_page.into_subsystem('业务管理')
        admin_page.select_menu('首页/游戏储备管理')

    @pytest.mark.gametype
    @pytest.mark.run(order=70)
    def test_query_game_type(self, set_up):
        """
        查询游戏类型
        1.输入类型名称：局游戏
        【check_point】第一条结果名称选项包含：局游戏
        :return:
        """
        admin_page.select_menu('游戏类型列表')
        game_type_page.query_game_type(name='局游戏')
        assert '局游戏' in game_type_page.read_table_cell_value(1, 3), '游戏类型搜索失败'

    @pytest.mark.gametype
    @pytest.mark.run(order=71)
    def test_reset_query(self):
        """
        清除查询
        :return:
        """
        admin_page.select_menu('游戏类型列表')
        game_type_page.reset_query()
        assert game_type_page.read_query_name() == '', '重置查询失败'

    @pytest.mark.gametype
    @pytest.mark.run(order=72)
    def test_open_add_window(self):
        """
        测试打开添加弹窗
        :return:
        """
        admin_page.select_menu('游戏类型列表')
        game_type_page.click_add_type()
        assert game_type_page.check_alert_is_exist('新增类型'), '打开新增游戏类型窗口失败'

    @pytest.fixture(scope='function')
    def close_alter_window(self):
        """
        点击取消按钮关闭弹窗
        :return:
        """
        yield 1
        game_type_page.cancel_alter()

    @pytest.mark.gametype
    @pytest.mark.run(order=73)
    def test_click_status_button(self, close_alter_window):
        """
        1.点击 状态按钮
        【check_point】检查是否有确认弹窗
        后置：关闭弹窗
        :param set_up:
        :return:
        """
        admin_page.select_menu('游戏类型列表')
        game_type_page.click_type_status_btn()
        assert game_type_page.check_alert_is_exist('提示'), '点击状态按钮未显示提示弹窗'

    @pytest.mark.gametype
    @pytest.mark.run(order=74)
    def test_click_edit_button(self, close_alter_window):
        """
        打开编辑界面
        :param set_up:
        :param close_alter_window:
        :return:
        """
        admin_page.select_menu('游戏类型列表')
        game_type_page.click_edit_btn()
        assert game_type_page.check_alert_is_exist('编辑类型'), "点击 编辑 按钮未打开编辑弹窗"