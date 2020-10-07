import allure
import pytest

from src.pages.admin_page import AdminPage
from src.pages.business_manage.channel_business_manage.channel_manage_page import ChannelManagePage

global channel_manage_page, admin_page


@pytest.mark.usefixtures('user_login')
@pytest.mark.usefixtures('init_browser')
@allure.story("渠道管理")
class TestChannelManage:

    @pytest.fixture(scope='function')
    def set_up(self):
        """
        前置操作
        :return:
        """
        global channel_manage_page, admin_page
        channel_manage_page = ChannelManagePage(self.driver)
        admin_page = AdminPage(self.driver)

        admin_page.into_subsystem('业务管理')
        admin_page.select_menu('首页/渠道业务管理')

    @pytest.mark.channelmanage
    @pytest.mark.run(order=160)
    def test_query_channel_manage(self, set_up):
        """
        渠道机构查询
        :return:
        """
        admin_page.select_menu('渠道管理')
        channel_manage_page.query_channel_name(name='北京')
        assert '北京' in channel_manage_page.read_table_cell_value(1, 5), '渠道管理查询失败'

    @pytest.mark.channelmanage
    @pytest.mark.run(order=161)
    def test_reset_channel_manage_query(self):
        """
        重置渠道列表查询
        :return:
        """
        admin_page.select_menu('渠道管理')
        channel_manage_page.reset_query()
        assert channel_manage_page.read_query_name() == '', '重置渠道管理查询条件失败'

    @pytest.mark.channelmanage
    @pytest.mark.run(order=162)
    def test_click_more_channel_manage_query(self):
        """
        展示更多的查询条件
        :return:
        """
        admin_page.select_menu('渠道管理')
        channel_manage_page.click_more_query()
        assert channel_manage_page.is_more_query(), '展示更多的查询条件失败'

    @pytest.mark.channelmanage
    @pytest.mark.run(order=163)
    def test_view_channel_organization_detail(self):
        """
        查看渠道详情
        :return:
        """
        admin_page.select_menu('渠道管理')
        channel_manage_page.click_view_organization()
        assert channel_manage_page.check_current_menu('渠道管理详情'), '点击查看渠道管理详情失败'

    @pytest.fixture(scope='function')
    def close_open_alert(self):
        """
        关闭弹窗
        :return:
        """
        yield 1
        channel_manage_page.cancel_fee()

    @pytest.mark.channelmanage
    @pytest.mark.run(order=164)
    def test_edit_channel_organization_detail(self, close_open_alert):
        """
        编辑渠道详情
        :return:
        """
        admin_page.select_menu('渠道管理')
        channel_manage_page.click_edit_organization()
        assert channel_manage_page.check_alert_is_exist('编辑渠道费用'), '点击查看渠道管理详情失败'