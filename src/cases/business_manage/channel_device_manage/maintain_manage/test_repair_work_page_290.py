"""
维修工单
"""
import allure
import pytest

from src.pages.admin_page import AdminPage
from src.pages.business_manage.channel_device_manage.maintain_manage.repair_work_page import RepairWorkPage

global repair_work_page, admin_page


@pytest.mark.usefixtures('user_login')
@pytest.mark.usefixtures('init_browser')
@allure.story("维修工单")
class TestRepairWork:

    @pytest.fixture(scope='function')
    def set_up(self):
        """
        前置操作
        :return:
        """
        global repair_work_page, admin_page
        repair_work_page = RepairWorkPage(self.driver)
        admin_page = AdminPage(self.driver)

        admin_page.into_subsystem('业务管理')
        admin_page.select_menu('首页/渠道终端管理/维修管理')

    @pytest.mark.repairwork
    @pytest.mark.run(order=290)
    def test_click_more_query_repair(self, set_up):
        """
        显示更多查询
        """
        admin_page.select_menu('维修工单', 4)
        repair_work_page.click_more_query()
        assert repair_work_page.is_more_query(), '显示更多查询失败'

    @pytest.mark.repairwork
    @pytest.mark.run(order=291)
    def test_query_repair_work(self):
        """
        查询维修工单
        """
        admin_page.select_menu('维修工单', 4)
        repair_work_page.simple_query_repair(device='终端机')
        assert '终端机' in repair_work_page.read_table_cell_value(1, 3), '查询维修工单失败'

    @pytest.mark.repairwork
    @pytest.mark.run(order=292)
    def test_reset_query_repair(self):
        """
        重置维修查询
        """
        admin_page.select_menu('维修工单', 4)
        repair_work_page.click_reset_query_button()
        assert repair_work_page.read_query_device_name() == '', '重置维修查询失败'

    @pytest.mark.repairwork
    @pytest.mark.run(order=293)
    def test_click_all_remind(self):
        """
        一键提醒
        """
        admin_page.select_menu('维修工单', 4)
        repair_work_page.click_all_remind()
        assert '提醒成功' in repair_work_page.read_toast(), '一键提醒失败'

    @pytest.mark.repairwork
    @pytest.mark.run(order=294)
    def test_view_repair_detail(self):
        """
        查看维修工单详情
        :return:
        """
        admin_page.select_menu('维修工单', 4)
        repair_work_page.click_view_repair_detail()
        assert repair_work_page.check_current_menu('维修工单详情'), '查看维修工单详情失败'

    @pytest.mark.repairwork
    @pytest.mark.run(order=295)
    def test_click_repair_remind(self):
        """
        工单提醒
        :return:
        """
        admin_page.select_menu('维修工单', 4)
        repair_work_page.simple_query_repair('待处理')
        repair_work_page.click_remind_btn()
        assert '提醒成功' in repair_work_page.read_toast(), '工单提醒失败'
