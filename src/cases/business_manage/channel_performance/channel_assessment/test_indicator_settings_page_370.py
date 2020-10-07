"""
指标列表
"""

import allure
import pytest

from src.pages.admin_page import AdminPage
from src.pages.business_manage.channel_performance.channel_assessment.indicator_settings_page import \
    IndicatorSettingsPage

global indicator_setting_page, admin_page


@pytest.mark.usefixtures('user_login')
@pytest.mark.usefixtures('init_browser')
@allure.story("指标列表")
class TestIndicatorSettings:

    @pytest.fixture(scope='function')
    def set_up(self):
        """
        前置操作
        :return:
        """
        global indicator_setting_page, admin_page
        indicator_setting_page = IndicatorSettingsPage(self.driver)
        admin_page = AdminPage(self.driver)

        admin_page.into_subsystem('业务管理')
        admin_page.select_menu('首页/渠道绩效管理/渠道考核')

    @pytest.mark.indicator
    @pytest.mark.run(order=370)
    def test_query_indicator_setting(self, set_up):
        """
        查询指标列表
        :return:
        """
        admin_page.select_menu('指标列表')
        indicator_setting_page.query_indicator_list(i_name='英语')
        assert '英语' in indicator_setting_page.read_table_cell_value(1, 2), '查询指标列表失败'

    @pytest.mark.indicator
    @pytest.mark.run(order=371)
    def test_reset_query_indicator_setting(self):
        """
        重置查询指标列表
        :param set_up:
        :return:
        """
        admin_page.select_menu('指标列表')
        indicator_setting_page.click_reset_query_button()
        assert indicator_setting_page.read_query_name() == '', '重置查询指标列表失败'

    @pytest.mark.indicator
    @pytest.mark.run(order=372)
    def test_click_more_query_indicator_setting(self):
        """
        展示更多查询条件
        :return:
        """
        admin_page.select_menu('指标列表')
        indicator_setting_page.click_more_query()
        assert indicator_setting_page.is_more_query(), '展示更多查询条件失败'

    @pytest.mark.indicator
    @pytest.mark.run(order=373)
    def test_click_create_indicator_setting(self):
        """
        点击新增指标
        :return:
        """
        admin_page.select_menu('指标列表')
        indicator_setting_page.click_create_indicator()
        assert indicator_setting_page.check_current_menu('新建指标'), '点击新增指标失败'

    @pytest.mark.indicator
    @pytest.mark.run(order=374)
    def test_click_view_indicator_detail(self):
        """
        查看指标详情
        :return:
        """
        admin_page.select_menu('指标列表')
        indicator_setting_page.click_view_indicator_detail()
        assert indicator_setting_page.check_current_menu('指标详情'), '查看指标详情失败'

    @pytest.mark.indicator
    @pytest.mark.run(order=375)
    def test_click_edit_indicator(self):
        """
        编辑指标
        :return:
        """
        admin_page.select_menu('指标列表')
        indicator_setting_page.click_edit_indicator_detail()
        assert indicator_setting_page.check_current_menu('编辑指标'), '编辑指标失败'

    @pytest.fixture(scope='function')
    def close_open_alert(self):
        """
        后置操作
        :return:
        """
        yield 1
        indicator_setting_page.alert_cancel('提示')

    @pytest.mark.indicator
    @pytest.mark.run(order=376)
    def test_click_delete_indicator(self, close_open_alert):
        """
        删除指标
        :return:
        """
        admin_page.select_menu('指标列表')
        indicator_setting_page.click_delete_indicator()
        assert indicator_setting_page.check_alert_is_exist('提示'), '删除指标失败'

