
import allure
import pytest

from src.pages.admin_page import AdminPage
from src.pages.business_manage.home_module.my_knowledge_page import MyKnowledgePage

global my_knowledge_page, admin_page


@pytest.mark.usefixtures('user_login')
@pytest.mark.usefixtures('init_browser')
@allure.story("我的知会")
class TestMyKnowledge:

    @pytest.fixture(scope='function')
    def set_up(self):
        """
        前置操作
        :return:
        """
        global my_knowledge_page, admin_page
        my_knowledge_page = MyKnowledgePage(self.driver)
        admin_page = AdminPage(self.driver)

        admin_page.into_subsystem('业务管理')

    @pytest.mark.knowledge
    @pytest.mark.run(order=51)
    def test_query_my_knowledge(self, set_up):
        """
        简单查询
        :param set_up:
        :return:
        """
        admin_page.select_menu('我的知会')
        my_knowledge_page.simple_query(title='渠道开设申报')
        assert '渠道开设申报' in my_knowledge_page.read_table_cell_value(1, 2), '知会列表查询失败'

    @pytest.mark.knowledge
    @pytest.mark.run(order=52)
    def test_reset_query(self):
        """
        重置查询条件
        :return:
        """
        admin_page.select_menu('我的知会')
        my_knowledge_page.reset_query()
        assert my_knowledge_page.read_query_title() == '', '重置查询条件失败'

    @pytest.mark.knowledge
    @pytest.mark.run(order=53)
    def test_display_more_query(self):
        """
        显示更多查询条件
        :return:
        """
        admin_page.select_menu('我的知会')
        my_knowledge_page.click_more_query()
        assert my_knowledge_page.is_more_query(), '点击 展开 按钮未显示更多查询条件'

    @pytest.fixture(autouse=True, scope='function')
    def close_open_menu(self):
        """
        后置操作，关闭当前菜单
        :return:
        """
        yield 1
        admin_page.close_current_menu()

    @pytest.mark.knowledge
    @pytest.mark.run(order=54)
    def test_view_approval_detail(self, close_open_menu):
        """
        查询申报详情
        :return:
        """
        admin_page.select_menu('我的知会')
        my_knowledge_page.simple_query('渠道开设申报')
        my_knowledge_page.click_approval_detail()
        assert my_knowledge_page.check_current_menu('审批详情'), '点击 查看 按钮未打开 审批详情'

    @pytest.mark.knowledge
    @pytest.mark.run(order=55)
    def test_view_detail(self, close_open_menu):
        """
        查询申报详情
        :return:
        """
        admin_page.select_menu('我的知会')
        my_knowledge_page.simple_query('渠道开设申报')
        my_knowledge_page.click_view_detail()
        assert my_knowledge_page.check_current_menu('渠道开设申报'), '点击 查看 按钮未打开 渠道开设申报'