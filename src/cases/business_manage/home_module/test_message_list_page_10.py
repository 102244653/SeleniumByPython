import allure
import pytest

from src.pages.admin_page import AdminPage
from src.pages.business_manage.home_module.message_list_page import MessageListPage

global message_list_page, admin_page


@pytest.mark.usefixtures('user_login')
@pytest.mark.usefixtures('init_browser')
@allure.story("站内信")
class TestMessageList:

    @pytest.fixture(scope='function')
    def set_up(self):
        """
        前置操作
        :return:
        """
        global message_list_page, admin_page
        message_list_page = MessageListPage(self.driver)
        admin_page = AdminPage(self.driver)

        admin_page.into_subsystem('业务管理')

    @pytest.mark.msg
    @pytest.mark.run(order=10)
    def test_query_msg(self, set_up):
        """
        查询消息
        1.输入标题：这是个坏消息
        【check_point】消息总数不为0
        :return:
        """
        admin_page.select_menu('站内信', True)
        message_list_page.query_msg(title='这是一个坏消息')
        assert message_list_page.read_table_cell_value(1, 2) == '这是一个坏消息', '消息查询失败'

    @pytest.mark.msg
    @pytest.mark.run(order=11)
    def test_reset_query(self):
        """
        重置查询条件
        :return:
        """
        message_list_page.reset_query()
        assert message_list_page.read_query_title() == '', '重置查询条件失败'

    @pytest.fixture(scope='function')
    def close_msg_window(self):
        """
        关闭消息窗口
        :return:
        """
        yield 1
        message_list_page.close_msg_window()

    @pytest.mark.msg
    @pytest.mark.run(order=12)
    def test_open_msg_window(self, close_msg_window):
        """
        检查打开发布消息弹窗
        :return:
        """
        admin_page.select_menu('站内信', True)
        message_list_page.write_new_msg()
        assert message_list_page.is_msg_window(), '打开消息弹窗失败'

    @pytest.mark.msg
    @pytest.mark.run(order=13)
    def test_view_msg(self):
        """
        点击查看消息按钮
        :return
        """
        admin_page.select_menu('站内信', True)
        message_list_page.click_view_msg()
        assert message_list_page.check_current_menu('消息详情'), '点击 查看 按钮未打开详情页面'
