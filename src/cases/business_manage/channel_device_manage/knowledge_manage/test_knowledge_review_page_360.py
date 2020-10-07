"""
知识库审核
"""


import allure
import pytest

from src.pages.admin_page import AdminPage
from src.pages.business_manage.channel_device_manage.knowledge_manage.knowledge_review_page import KnowledgeReviewPage

global knowledge_review_page, admin_page


@pytest.mark.usefixtures('user_login')
@pytest.mark.usefixtures('init_browser')
@allure.story("知识库审核")
class TestKnowledgeReview:

    @pytest.fixture(scope='function')
    def set_up(self):
        """
        前置操作
        :return:
        """
        global knowledge_review_page, admin_page
        knowledge_review_page = KnowledgeReviewPage(self.driver)
        admin_page = AdminPage(self.driver)

        admin_page.into_subsystem('业务管理')
        admin_page.select_menu('首页/渠道终端管理/维护知识库')

    @pytest.mark.review
    @pytest.mark.run(order=360)
    def test_query_knowledge_review(self, set_up):
        """
        知识库审核查询
        :return:
        """
        admin_page.select_menu('知识库审核')
        knowledge_review_page.query_knowledge_review(device='设备')
        assert '设备' in knowledge_review_page.read_table_cell_value(1, 2), '知识库审核查询失败'

    @pytest.mark.review
    @pytest.mark.run(order=361)
    def test_reset_query_knowledge_review(self):
        """
        重置查询
        :return:
        """
        admin_page.select_menu('知识库审核')
        knowledge_review_page.click_reset_query_button()
        assert knowledge_review_page.read_query_device_type() == '', '知识库审核重置查询失败'

    @pytest.mark.review
    @pytest.mark.run(order=362)
    def test_view_knowledge_review(self):
        """
        查看知识库审核详情
        :return:
        """
        admin_page.select_menu('知识库审核')
        knowledge_review_page.click_view_review_detail()
        assert knowledge_review_page.check_current_menu('知识库审核详情'), '查看知识库审核详情失败'

    @pytest.fixture(scope='function')
    def close_alert_window(self):
        """
        关闭弹窗
        :return:
        """
        yield 1
        knowledge_review_page.review_confirm(False)

    @pytest.mark.review
    @pytest.mark.run(order=363)
    def test_click_knowledge_review(self, close_alert_window):
        """
        点击知识库审核
        :return:
        """
        admin_page.select_menu('知识库审核')
        knowledge_review_page.click_knowledge_review()
        assert knowledge_review_page.check_alert_is_exist('审核知识库'), '点击知识库审核失败'

    @pytest.fixture(scope='function')
    def close_open_alert(self):
        yield 1
        knowledge_review_page.alert_cancel('提示')

    @pytest.mark.review
    @pytest.mark.run(order=364)
    def test_click_delete_knowledge_review(self, close_open_alert):
        """
        点击删除
        :return:
        """
        admin_page.select_menu('知识库审核')
        knowledge_review_page.click_delete_knowledge()
        assert knowledge_review_page.check_alert_is_exist('提示'), '点击删除'
