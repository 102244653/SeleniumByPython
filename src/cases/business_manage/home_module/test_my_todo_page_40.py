import time

import allure
import pytest

from src.pages.admin_page import AdminPage
from src.pages.business_manage.home_module.my_todo_page import MyTodoPage

global my_todo_page, admin_page


@pytest.mark.usefixtures('user_login')
@pytest.mark.usefixtures('init_browser')
@allure.story("我的待办")
class TestMyTodo:

    @pytest.fixture(scope='function')
    def set_up(self):
        """
        前置操作
        :return:
        """
        global my_todo_page, admin_page
        my_todo_page = MyTodoPage(self.driver)
        admin_page = AdminPage(self.driver)

        admin_page.into_subsystem('业务管理')

    @pytest.mark.todo
    @pytest.mark.run(order=40)
    def test_query_my_todo(self, set_up):
        """
        简单查询
        :param set_up:
        :return:
        """
        admin_page.select_menu('我的待办')
        my_todo_page.simple_query(title='投注卡申请')
        assert '投注卡申请' in my_todo_page.read_table_cell_value(1, 2), '申请列表查询失败'

    @pytest.mark.todo
    @pytest.mark.run(order=41)
    def test_reset_query(self):
        """
        重置查询条件
        :return:
        """
        my_todo_page.reset_query()
        assert my_todo_page.read_query_title() == '', '重置查询条件失败'

    @pytest.mark.todo
    @pytest.mark.run(order=42)
    def test_display_more_query(self):
        """
        显示更多查询条件
        :return:
        """
        admin_page.select_menu('我的待办')
        my_todo_page.click_more_query()
        assert my_todo_page.is_more_query(), '点击 展开 按钮未显示更多查询条件'

    @pytest.fixture(scope='function')
    def close_print_window(self):
        """
        退出打印预览
        :return:
        """
        yield 1
        my_todo_page.close_print_view()

    @pytest.mark.todo
    @pytest.mark.run(order=43)
    def test_print_view(self, close_print_window):
        """
        打开打印预览
        :return:
        """
        admin_page.select_menu('我的待办')
        my_todo_page.click_print()
        time.sleep(2)
        assert my_todo_page.is_print_view(), '进入打印预览页面失败'

    @pytest.mark.todo
    @pytest.mark.run(order=44)
    def test_view_detail(self):
        """
        查询业务详情
        :return:
        """
        admin_page.select_menu('我的待办')
        my_todo_page.simple_query('投注卡申请')
        my_todo_page.click_view_detail()
        assert my_todo_page.check_current_menu('投注卡申请'), '点击 查看 按钮未打开 投注卡申请'
