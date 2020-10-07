import allure
import pytest

from src.pages.admin_page import AdminPage
from src.pages.business_manage.home_module.over_view_page import OverViewPage

global over_view_page, admin_page


@pytest.mark.usefixtures('user_login')
@pytest.mark.usefixtures('init_browser')
@allure.story("概况")
class TestOverView:

    @pytest.fixture(scope='function')
    def set_up(self):
        """
        前置操作
        :return:
        """
        global over_view_page, admin_page
        over_view_page = OverViewPage(self.driver)
        admin_page = AdminPage(self.driver)

        admin_page.into_subsystem('业务管理')

    @pytest.fixture(autouse=True, scope='function')
    def close_open_menu(self):
        """
        后置操作，关闭当前菜单
        :return:
        """
        yield 1
        admin_page.close_current_menu()

    @pytest.mark.home
    @pytest.mark.run(order=1)
    def test_check_wait_confirm(self, set_up):
        """
        检查待审核：
        1.点击 待审核 图标
        【check_point】当前菜单窗口标题==我的待办
        :return:
        """
        admin_page.select_menu('概况')
        over_view_page.click_wait_confirm()
        assert over_view_page.check_current_menu('我的待办'), "点击 【待审核】 未跳转至 我的待办"
        toast = over_view_page.read_toast()
        assert toast == '', '检查到错误提示信息：'+toast

    @pytest.mark.home
    @pytest.mark.run(order=2)
    def test_check_have_confirm(self):
        """
        1.检查 已审核 图标
        【check_point】当前菜单窗口标题==我的已办
        :return:
        """
        admin_page.select_menu('概况')
        over_view_page.click_have_confirm()
        assert over_view_page.check_current_menu('我的已办'), "点击 【已审核】 未跳转至 我的已办"
        toast = over_view_page.read_toast()
        assert toast == '', '检查到错误提示信息：'+toast

    @pytest.mark.home
    @pytest.mark.run(order=3)
    def test_check_have_apply(self):
        """
        1.检查 已申请 图标
        【check_point】当前菜单窗口标题==我的申请
        :return:我的申请
        """
        admin_page.select_menu('概况')
        over_view_page.click_have_confirm()
        assert over_view_page.check_current_menu(''), "点击 【已申请】 未跳转至 我的申请"
        toast = over_view_page.read_toast()
        assert toast == '', '检查到错误提示信息：'+toast

    @pytest.mark.home
    @pytest.mark.run(order=4)
    def test_check_have_notified(self):
        """
        1.检查 已知会 图标
        【check_point】当前菜单窗口标题==我的知会
        :return:
        """
        admin_page.select_menu('概况')
        over_view_page.click_have_notified()
        assert over_view_page.check_current_menu('我的知会'), "点击 【已知会】 未跳转至 我的知会"
        toast = over_view_page.read_toast()
        assert toast == '', '检查到错误提示信息：'+toast

    @pytest.mark.home
    @pytest.mark.run(order=5)
    def test_check_more_message(self):
        """
        1.检查 已审核 图标
        【check_point】当前菜单窗口标题==我的已办
        :return:
        """
        admin_page.select_menu('概况')
        over_view_page.click_more_message()
        over_view_page.loading()
        assert over_view_page.check_current_menu('站内信'), "点击 【更多消息】 未跳转至 站内信"
        toast = over_view_page.read_toast()
        assert toast == '', '检查到错误提示信息：'+toast
