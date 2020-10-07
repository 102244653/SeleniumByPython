import allure
import pytest

from src.pages.admin_page import AdminPage
from src.pages.business_manage.channel_business_manage.channel_summary_page import ChannelSummaryPage

global channel_summary_page, admin_page


@pytest.mark.usefixtures('user_login')
@pytest.mark.usefixtures('init_browser')
@allure.story("渠道汇总")
class TestChannelSummary:

    @pytest.fixture(scope='function')
    def set_up(self):
        """
        前置操作
        :return:
        """
        global channel_summary_page, admin_page
        channel_summary_page = ChannelSummaryPage(self.driver)
        admin_page = AdminPage(self.driver)

        admin_page.into_subsystem('业务管理')
        admin_page.select_menu('首页/渠道业务管理')

    @pytest.mark.channelorganization
    @pytest.mark.run(order=150)
    def test_query_channel_organization(self, set_up):
        """
        渠道机构查询
        :return:
        """
        admin_page.select_menu('渠道汇总')
        channel_summary_page.query_channel()
        assert '北京市' in channel_summary_page.read_table_cell_value(1, 2), '渠道机构查询失败'

    @pytest.mark.channelorganization
    @pytest.mark.run(order=151)
    def test_view_channel_next_organization(self):
        """
        查看下级渠道机构
        :return:
        """
        admin_page.select_menu('渠道汇总')
        channel_summary_page.view_next_organization()
        assert channel_summary_page.check_current_menu('渠道地市汇总'), '点击查看渠道下级机构失败'