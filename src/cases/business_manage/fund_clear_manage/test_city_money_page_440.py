"""
城市资金参数
"""
import allure
import pytest

from src.pages.admin_page import AdminPage
from src.pages.business_manage.fund_clear_manage.city_money_page import CityMoneyPage

global city_money_page, admin_page


@pytest.mark.usefixtures('user_login')
@pytest.mark.usefixtures('init_browser')
@allure.story("城市资金参数")
class TestCityMoney:

    @pytest.fixture(scope='function')
    def set_up(self):
        """
        前置操作
        :return:
        """
        global city_money_page, admin_page
        city_money_page = CityMoneyPage(self.driver)
        admin_page = AdminPage(self.driver)

        admin_page.into_subsystem('业务管理')
        admin_page.select_menu('首页/资金结算管理')

    @pytest.mark.citymoey
    @pytest.mark.run(order=440)
    def test_query_city_money_list(self, set_up):
        """
        城市资金参数列表查询
        :return:
        """
        admin_page.select_menu('城市资金参数')
        city_money_page.query_city_money(name='深海探秘')
        assert '深海探秘' in city_money_page.read_table_cell_value(1, 3), '城市资金参数列表查询失败'

    @pytest.fixture(scope='function')
    def close_open_alert(self):
        """
        关闭弹窗
        :return:
        """
        yield 1
        city_money_page.alert_close('编辑发行费比例')

    @pytest.mark.citymoey
    @pytest.mark.run(order=441)
    def test_click_select_edit(self, close_open_alert):
        """
        城市资金参数批量编辑
        :return:
        """
        admin_page.select_menu('城市资金参数')
        city_money_page.click_selcet_edit_btn([1, 2])
        assert city_money_page.check_alert_is_exist('编辑发行费比例'), '城市资金参数批量编辑失败'

    @pytest.mark.citymoey
    @pytest.mark.run(order=442)
    def test_click_all_edit(self, close_open_alert):
        """
        城市资金参数全部编辑
        :return:
        """
        admin_page.select_menu('城市资金参数')
        city_money_page.click_all_edit_btn()
        assert city_money_page.check_alert_is_exist('编辑发行费比例'), '城市资金参数全部编辑失败'

    @pytest.mark.citymoey
    @pytest.mark.run(order=443)
    def test_click_single_edit(self, close_open_alert):
        """
        城市资金参数全部编辑
        :return:
        """
        admin_page.select_menu('城市资金参数')
        city_money_page.click_edit_detail_btn()
        assert city_money_page.check_alert_is_exist('编辑发行费比例'), '城市资金参数单个编辑失败'

