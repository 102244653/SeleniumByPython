"""
等级配置
"""

import allure
import pytest

from src.pages.admin_page import AdminPage
from src.pages.business_manage.channel_performance.channel_level.channel_level_config_page import LevelConfigPage

global level_config_page, admin_page


@pytest.mark.usefixtures('user_login')
@pytest.mark.usefixtures('init_browser')
@allure.story("等级配置")
class TestLevelConfig:

    @pytest.fixture(scope='function')
    def set_up(self):
        """
        前置操作
        :return:
        """
        global level_config_page, admin_page
        level_config_page = LevelConfigPage(self.driver)
        admin_page = AdminPage(self.driver)

        admin_page.into_subsystem('业务管理')
        admin_page.select_menu('首页/渠道绩效管理/渠道等级')

    @pytest.mark.levelconfig
    @pytest.mark.run(order=420)
    def test_query_level_config(self, set_up):
        """
        查询等级配置
        :return:
        """
        admin_page.select_menu('等级配置')
        level_config_page.query_level_config(name='自动化测试')
        assert '自动化测试' in level_config_page.read_table_cell_value(1, 2), '查询等级配置失败'

    @pytest.mark.levelconfig
    @pytest.mark.run(order=421)
    def test_click_more_query_level_config(self):
        """
        展示更多查询条件
        :return:
        """
        admin_page.select_menu('等级配置')
        level_config_page.click_more_query()
        assert level_config_page.is_more_query(), '展示更多查询条件失败'

    @pytest.mark.levelconfig
    @pytest.mark.run(order=422)
    def test_click_view_level_detail(self):
        """
        查看等级配置
        :return:
        """
        admin_page.select_menu('等级配置')
        level_config_page.click_view_level_detail()
        assert level_config_page.check_current_menu('等级配置详情'), '查看等级配置详情失败'
    
    @pytest.mark.levelconfig
    @pytest.mark.run(order=423)
    def test_click_edit_level(self):
        """
        编辑等级配置
        :return:
        """
        admin_page.select_menu('等级配置')
        level_config_page.click_edit_level()
        assert level_config_page.check_current_menu('编辑等级配置'), '查看等级配置详情失败'

    @pytest.fixture(scope='function')
    def close_open_alert(self):
        """
        关闭弹窗
        :return:
        """
        yield 1
        level_config_page.alert_cancel('提示')

    @pytest.mark.levelconfig
    @pytest.mark.run(order=424)
    def test_click_delete_level(self, close_open_alert):
        """
        删除等级配置
        :return:
        """
        admin_page.select_menu('等级配置')
        level_config_page.click_delete_level()
        assert level_config_page.check_alert_is_exist('提示'), '删除等级配置失败'