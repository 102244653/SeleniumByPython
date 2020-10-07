"""
入库管理
"""

import allure
import pytest

from src.pages.admin_page import AdminPage
from src.pages.business_manage.channel_resource_manage.out_put_manage.put_store_manage_page import PutStoreManagePage

global put_store_page, admin_page


@pytest.mark.usefixtures('user_login')
@pytest.mark.usefixtures('init_browser')
@allure.story("入库管理")
class TestDeviceList:

    @pytest.fixture(scope='function')
    def set_up(self):
        """
        前置操作
        :return:
        """
        global put_store_page, admin_page
        put_store_page = PutStoreManagePage(self.driver)
        admin_page = AdminPage(self.driver)

        admin_page.into_subsystem('业务管理')
        admin_page.select_menu('首页/渠道资源管理/出入库管理')

    @pytest.mark.putstore
    @pytest.mark.run(order=230)
    def test_query_put_store(self, set_up):
        """
        查寻上架列表
        1.输入类型名称：202007
        【check_point】第一条结果名称选项包含：202007
        :return:
        """
        admin_page.select_menu('入库管理')
        put_store_page.query_put_store(id='202007')
        assert '202007' in put_store_page.read_table_cell_value(1, 2), '查寻上架列表失败'

    @pytest.mark.putstore
    @pytest.mark.run(order=231)
    def test_reset_query_put_store(self):
        """
        重置查询
        :return:
        """
        admin_page.select_menu('入库管理')
        put_store_page.click_reset_query_button()
        assert put_store_page.read_query_id() == '', '重置查询失败'

    @pytest.mark.putstore
    @pytest.mark.run(order=232)
    def test_view_put_store_detail(self):
        """
        查看入库详情
        :return:
        """
        admin_page.select_menu('入库管理')
        put_store_page.switch_put_tab('已入库')
        put_store_page.click_view_put_store_detail()
        assert put_store_page.check_current_menu('已入库详情'), '查看已入库详情失败'

    @pytest.fixture(scope='function')
    def close_open_print(self):
        """
        关闭打印窗口
        :return:
        """
        yield 1
        put_store_page.close_print_view()

    @pytest.mark.putstore
    @pytest.mark.run(order=233)
    def test_print_put_store(self, close_open_print):
        """
        打印入库单
        :return:
        """
        admin_page.select_menu('入库管理')
        put_store_page.click_print_put_store()
        assert put_store_page.is_print_view(), '打印入库单 失败'