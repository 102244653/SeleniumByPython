"""
出库管理
"""


import allure
import pytest

from src.pages.admin_page import AdminPage
from src.pages.business_manage.channel_resource_manage.out_put_manage.out_store_manage_page import OutStoreManagePage

global out_store_page, admin_page


@pytest.mark.usefixtures('user_login')
@pytest.mark.usefixtures('init_browser')
@allure.story("出库管理")
class TestDeviceList:

    @pytest.fixture(scope='function')
    def set_up(self):
        """
        前置操作
        :return:
        """
        global out_store_page, admin_page
        out_store_page = OutStoreManagePage(self.driver)
        admin_page = AdminPage(self.driver)

        admin_page.into_subsystem('业务管理')
        admin_page.select_menu('首页/渠道资源管理/出入库管理')

    @pytest.mark.outstore
    @pytest.mark.run(order=220)
    def test_query_out_store(self, set_up):
        """
        查寻出库列表
        1.输入类型名称：终端机
        【check_point】第一条结果名称选项包含：终端机
        :return:
        """
        admin_page.select_menu('出库管理')
        out_store_page.query_out_store(title='资源申请')
        assert '资源申请' in out_store_page.read_table_cell_value(1, 3), '查寻出库列表失败'

    @pytest.mark.outstore
    @pytest.mark.run(order=221)
    def test_reset_query_out_store(self):
        """
        重置查询
        :return:
        """
        admin_page.select_menu('出库管理')
        out_store_page.click_reset_query_button()
        assert out_store_page.read_query_title() == '', '重置查询失败'

    @pytest.mark.outstore
    @pytest.mark.run(order=222)
    def test_view_out_store_detail(self):
        """
        查看入库详情
        :return:
        """
        admin_page.select_menu('出库管理')
        out_store_page.switch_out_tab('已出库')
        out_store_page.click_view_out_store_detail()
        assert out_store_page.check_current_menu('已出库详情'), '查看已出库详情失败'

    @pytest.fixture(scope='function')
    def close_open_print(self):
        """
        关闭打印窗口
        :return:
        """
        yield 1
        out_store_page.close_print_view()

    @pytest.mark.outstore
    @pytest.mark.run(order=223)
    def test_print_out_store(self, close_open_print):
        """
        打印入库单
        :return:
        """
        admin_page.select_menu('出库管理')
        out_store_page.click_print_out_store()
        assert out_store_page.is_print_view(), '打印出库单失败'