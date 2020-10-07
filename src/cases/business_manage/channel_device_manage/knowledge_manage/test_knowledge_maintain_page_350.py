"""
维护知识库
"""

import allure
import pytest

from src.pages.admin_page import AdminPage
from src.pages.business_manage.channel_device_manage.knowledge_manage.knowledge_maintain_page import \
    KnowledgeMaintainPage

global knowledge_maintain_page, admin_page


@pytest.mark.usefixtures('user_login')
@pytest.mark.usefixtures('init_browser')
@allure.story("维护知识库")
class TestKnowledgeMaintain:

    @pytest.fixture(scope='function')
    def set_up(self):
        """
        前置操作
        :return:
        """
        global knowledge_maintain_page, admin_page
        knowledge_maintain_page = KnowledgeMaintainPage(self.driver)
        admin_page = AdminPage(self.driver)

        admin_page.into_subsystem('业务管理')
        admin_page.select_menu('首页/渠道终端管理/维护知识库')

    @pytest.mark.maintain
    @pytest.mark.run(order=350)
    def test_query_knowledge_maintain(self, set_up):
        """
        知识库维护查询
        :return:
        """
        admin_page.select_menu('T维护知识库')
        knowledge_maintain_page.query_knowledge_maintain(device='设备')
        assert '设备' in knowledge_maintain_page.read_table_cell_value(1, 2), '知识库维护查询失败'

    @pytest.mark.maintain
    @pytest.mark.run(order=351)
    def test_reset_query_knowledge_maintain(self):
        """
        重置查询
        :return:
        """
        admin_page.select_menu('T维护知识库')
        knowledge_maintain_page.click_reset_query_button()
        assert knowledge_maintain_page.read_query_device_type() == '', '知识库维护重置查询失败'

    @pytest.mark.maintain
    @pytest.mark.run(order=352)
    def test_view_knowledge_maintain(self):
        """
        查看知识库详情
        :return:
        """
        admin_page.select_menu('T维护知识库')
        knowledge_maintain_page.click_view_knowledge_detail()
        assert knowledge_maintain_page.check_current_menu('知识库审核'), '查看知识库详情失败'