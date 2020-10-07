import allure
import pytest

from src.pages.admin_page import AdminPage
from src.pages.business_manage.home_module.record_manage_page import RecordManagePage

global record_manage_page, admin_page


@pytest.mark.usefixtures('user_login')
@pytest.mark.usefixtures('init_browser')
@allure.story("档案管理")
class TestRecordManage:

    @pytest.fixture(scope='function')
    def set_up(self):
        """
        前置操作
        :return:
        """
        global record_manage_page, admin_page
        record_manage_page = RecordManagePage(self.driver)
        admin_page = AdminPage(self.driver)

        admin_page.into_subsystem('业务管理')

    @pytest.mark.record
    @pytest.mark.run(order=30)
    def test_query_record_manage(self, set_up):
        """
        查询
        1.输入查询标题：终端机维修申请
        【check_point】第一条结果标题为：终端机维修申请
        :return:
        """
        admin_page.select_menu('档案管理')
        record_manage_page.simple_query(title='终端机维修申请')
        assert '终端机维修申请' in record_manage_page.read_table_cell_value(1, 2), '档案管理标题查询失败'

    @pytest.mark.record
    @pytest.mark.run(order=31)
    def test_reset_query(self):
        """
        重置查询条件
        :return:
        """
        record_manage_page.reset_query()
        assert record_manage_page.read_query_title() == '', '重置查询条件失败'

    @pytest.mark.record
    @pytest.mark.run(order=32)
    def test_display_more_query(self):
        """
        显示更多查询条件
        :return:
        """
        admin_page.select_menu('档案管理')
        record_manage_page.click_more_query()
        assert record_manage_page.is_more_query(), '点击 展开 按钮未显示更多查询条件'

    @pytest.fixture(scope='function')
    def close_open_menu(self):
        """
        关闭当前菜单
        :return:
        """
        yield 1
        admin_page.close_current_menu()

    @pytest.mark.record
    @pytest.mark.run(order=33)
    def test_view_detail(self, close_open_menu):
        """
        查询业务详情
        :return:
        """
        admin_page.select_menu('档案管理')
        record_manage_page.simple_query('柜员机维修申请')
        record_manage_page.click_view_detail()
        assert record_manage_page.check_current_menu('审批详情'), '点击 查看 按钮未打开 审批详情'

    @pytest.mark.record
    @pytest.mark.run(order=34)
    def test_view_detail(self, close_open_menu):
        """
        查询业务详情
        :return:
        """
        admin_page.select_menu('档案管理')
        record_manage_page.simple_query('柜员机维修申请')
        record_manage_page.click_view_data()
        assert record_manage_page.check_current_menu('设备维护申请'), '点击 查看 按钮未打开 App设备维护申请'