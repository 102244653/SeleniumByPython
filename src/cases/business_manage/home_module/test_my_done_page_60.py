
import allure
import pytest

from src.pages.admin_page import AdminPage
from src.pages.business_manage.home_module.my_done_page import MyDonePage

global my_done_page, admin_page


@pytest.mark.usefixtures('user_login')
@pytest.mark.usefixtures('init_browser')
@allure.story("我的已办")
class TestMyApplication:

    @pytest.fixture(scope='function')
    def set_up(self):
        """
        前置操作
        :return:
        """
        global my_done_page, admin_page
        my_done_page = MyDonePage(self.driver)
        admin_page = AdminPage(self.driver)

        admin_page.into_subsystem('业务管理')

    @pytest.mark.done
    @pytest.mark.run(order=60)
    def test_query_my_done(self, set_up):
        """
        简单查询
        :param set_up:
        :return:
        """
        admin_page.select_menu('我的已办')
        my_done_page.simple_query(title='投注卡申请')
        assert '投注卡申请' in my_done_page.read_table_cell_value(1, 2), '申请列表查询失败'

    @pytest.mark.done
    @pytest.mark.run(order=61)
    def test_reset_query(self):
        """
        重置查询条件
        :return:
        """
        my_done_page.reset_query()
        assert my_done_page.read_query_title() == '', '重置查询条件失败'

    @pytest.mark.done
    @pytest.mark.run(order=62)
    def test_display_more_query(self):
        """
        显示更多查询条件
        :return:
        """
        admin_page.select_menu('我的已办')
        my_done_page.click_more_query()
        assert my_done_page.is_more_query(), '点击 展开 按钮未显示更多查询条件'