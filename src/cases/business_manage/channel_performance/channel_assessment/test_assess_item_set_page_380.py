"""
考核项列表
"""


import allure
import pytest

from src.pages.admin_page import AdminPage
from src.pages.business_manage.channel_performance.channel_assessment.assess_item_set_page import AssessItemSetPage

global assess_item_page, admin_page


@pytest.mark.usefixtures('user_login')
@pytest.mark.usefixtures('init_browser')
@allure.story("考核项列表")
class TestAssessItemSet:

    @pytest.fixture(scope='function')
    def set_up(self):
        """
        前置操作
        :return:
        """
        global assess_item_page, admin_page
        assess_item_page = AssessItemSetPage(self.driver)
        admin_page = AdminPage(self.driver)

        admin_page.into_subsystem('业务管理')
        admin_page.select_menu('首页/渠道绩效管理/渠道考核')

    @pytest.mark.indicator
    @pytest.mark.run(order=380)
    def test_query_assess_item(self, set_up):
        """
        查询考核项列表
        :return:
        """
        admin_page.select_menu('考核项列表')
        assess_item_page.query_assess_item(name='测试数据')
        assert '测试数据' in assess_item_page.read_table_cell_value(1, 2), '查询考核项列表失败'

    @pytest.mark.indicator
    @pytest.mark.run(order=381)
    def test_reset_query_assess_item(self):
        """
        重置查询考核项列表
        :param set_up:
        :return:
        """
        admin_page.select_menu('考核项列表')
        # assess_item_page.click_reset_query_button()
        assert assess_item_page.read_query_name() == '', '重置查询考核项列表失败'

    @pytest.mark.indicator
    @pytest.mark.run(order=383)
    def test_click_create_assess_item(self):
        """
        点击新增考核项
        :return:
        """
        admin_page.select_menu('考核项列表')
        assess_item_page.click_create_assess_item()
        assert assess_item_page.check_current_menu('新增考核项'), '点击新增考核项失败'

    @pytest.mark.indicator
    @pytest.mark.run(order=384)
    def test_click_view_assess_item(self):
        """
        查看考核项详情
        :return:
        """
        admin_page.select_menu('考核项列表')
        assess_item_page.click_view_assess_item()
        assert assess_item_page.check_current_menu('考核项详情'), '查看考核项详情失败'

    @pytest.mark.indicator
    @pytest.mark.run(order=385)
    def test_click_edit_assess_item(self):
        """
        编辑考核项
        :return:
        """
        admin_page.select_menu('考核项列表')
        assess_item_page.click_edit_assess_item()
        assert assess_item_page.check_current_menu('编辑考核项'), '编辑考核项失败'

    @pytest.fixture(scope='function')
    def close_open_alert(self):
        """
        后置操作
        :return:
        """
        yield 1
        assess_item_page.alert_cancel('提示')

    @pytest.mark.indicator
    @pytest.mark.run(order=386)
    def test_click_delete_assess_item(self, close_open_alert):
        """
        删除考核项
        :return:
        """
        admin_page.select_menu('考核项列表')
        assess_item_page.click_delete_assess_item()
        assert assess_item_page.check_alert_is_exist('提示'), '删除考核项失败'

