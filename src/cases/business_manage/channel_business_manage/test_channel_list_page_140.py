import allure
import pytest

from src.pages.admin_page import AdminPage
from src.pages.business_manage.channel_business_manage.channel_list_page import ChannelListPage

global channel_list_page, admin_page


@pytest.mark.usefixtures('user_login')
@pytest.mark.usefixtures('init_browser')
@allure.story("渠道列表")
class TestChannelList:

    @pytest.fixture(scope='function')
    def set_up(self):
        """
        前置操作
        :return:
        """
        global channel_list_page, admin_page
        channel_list_page = ChannelListPage(self.driver)
        admin_page = AdminPage(self.driver)

        admin_page.into_subsystem('业务管理')
        admin_page.select_menu('首页/渠道业务管理')

    @pytest.mark.channellist
    @pytest.mark.run(order=140)
    def test_query_channel(self, set_up):
        """
        渠道查询
        :return:
        """
        admin_page.select_menu('渠道列表')
        channel_list_page.simple_query_channel(channel_name='三沙市')
        assert '三沙市' in channel_list_page.read_table_cell_value(1, 2), '渠道列表查询失败'

    @pytest.mark.channellist
    @pytest.mark.run(order=141)
    def test_reset_channel_query(self):
        """
        重置渠道列表查询
        :return:
        """
        admin_page.select_menu('渠道列表')
        channel_list_page.reset_query()
        assert channel_list_page.read_query_name() == '', '重置渠道列表查询条件失败'

    @pytest.mark.channellist
    @pytest.mark.run(order=142)
    def test_click_more_channel_query(self):
        """
        展示更多的查询条件
        :return:
        """
        admin_page.select_menu('渠道列表')
        channel_list_page.click_more_query()
        assert channel_list_page.is_more_query(), '展示更多的查询条件失败'

    @pytest.mark.channellist
    @pytest.mark.run(order=143)
    def test_view_channel_detail(self):
        """
        查看渠道详情
        :return:
        """
        admin_page.select_menu('渠道列表')
        channel_list_page.view_channel_detail()
        assert channel_list_page.check_current_menu('渠道详情'), '点击查看渠道详情失败'