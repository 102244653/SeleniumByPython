import time

from selenium.webdriver.common.keys import Keys

from vlt_path import get_path
from src.common.base_method import BaseMethod
from src.common.log import Logger

log = Logger().get_logger()
path = get_path()


class BasePage(BaseMethod):
    """
    公共方法
    """

    @property
    def confirm(self):
        alter = self.driver.switch_to_alert()
        alter.accept()

    @property
    def cancel(self):
        alter = self.driver.switch_to_alert()
        alter.dismiss()

    @property
    def alert_text(self):
        alter = self.driver.switch_to_alert()
        return alter.text

    def loading(self, num=10):
        loading = ('xpath', '/html/body/div[14]')
        for i in range(num):
            if self.wait_exist(loading):
                time.sleep(2)
            else:
                return

    def check_current_menu(self, menu):
        """
        检查当前窗口的菜单与预期是否一致
        :param menu:
        :return:
        """
        time.sleep(2.5)
        menu_title = ('css', 'span.el-tag.el-tag--light.current')
        menu_name = self.get_text(menu_title)
        if menu in menu_name:
            log.info('当前活动菜单['+menu_name+']')
            return True
        else:
            return False

    def close_current_menu(self):
        """
        关闭当前的菜单窗口
        :return:
        """
        menu_list = ('xpath', '//div[@class="tags-list"]/span')
        if len(self.get_elements(menu_list)) > 1:
            self.click_element(('css', '.current > .el-tag__close'))
            time.sleep(2)

    def select_date(self, start, end):
        """
        选择开始/结束时间
        :param start:
        :param end:
        :return:
        """
        start_input = ('xpath', '//input[@placeholder="开始日期"]')
        end_input = ('xpath', '//input[@placeholder="结束日期"]')
        self.send_keys(start_input, start)
        self.send_keys(end_input, end)

    def is_print_view(self):
        """
        检查是否打开打印预览
        :return:
        """
        return self.wait_exist(('xpath', '//div[@aria-label="打印预览"]'))

    def close_print_view(self):
        """
        关闭打印预览
        :return:
        """
        self.click_element(('css', '.el-button--medium:nth-child(2) > span'))

    def read_toast(self, msg=None):
        """
        读取toast提示
        :return:
        """
        ele = self.find_toast(msg)
        if ele:
            t = ele.text
            log.info('已读取到Toast=[{}]'.format(t))
            return t
        else:
            return ''

    def check_alert_is_exist(self, alter_name):
        """
        检查是否显示了某个弹窗：需要输入弹窗名称
        :param alter_name:
        :return:
        """
        alter_ele = ('xpath', '//div[@aria-label="{}" and @role="dialog"]'.format(alter_name))
        return self.wait_exist(alter_ele)

    def alert_cancel(self, alter_name):
        """
        提示弹窗取消
        :return:
        """
        self.click_element(('xpath', '//div[@aria-label="{}"]/div/div[3]/button[1]'.format(alter_name)))

    def alert_confirm(self, alter_name):
        """
        提示弹窗确认
        :return:
        """
        self.click_element(('xpath', '//div[@aria-label="{}"]/div/div[3]/button[1]'.format(alter_name)))

    def alert_close(self, alter_name):
        """
        提示弹窗的关闭按钮
        :return:
        """
        self.click_element(('xpath', '//div[@aria-label="{}"]//button[@aria-label="Close"]'.format(alter_name)))

    def read_table_cell_value(self, row=1, line=2):
        """
        读取单元格的text
        :return:
        """
        title_cell = ('xpath', '//tbody/tr[{}]/td[{}]/div'.format(row, line))
        if self.wait_exist(title_cell):
            return self.get_text(title_cell)
        else:
            return ' '

    def select_beijing(self, locator, is_center=False):
        """
        选择机构
        ****穿的值最好为默认显示的，没有滑动操作
        :param locator:定位元素
        :param is_center: 默认不选择：中国福利彩票
        """
        if isinstance(locator, tuple):
            el = self.get_element(locator)
        else:
            el = locator
        self.click_element(el)
        time.sleep(1)
        if is_center:
            self.click_element(('xpath', '//li[starts-with(@id,"cascader-menu")]/label/span/span'))
        self.click_element(('xpath', '/html/body/div[2]/div[1]/div[2]/div[1]/ul/li[1]/label/span[1]/span'))
        time.sleep(1)
        self.click_element(el)

    def click_search_button(self, isload=False):
        """
        点击页面查询按钮
        :return:
        """
        self.click_element(('css', '.el-form-item__content > .el-button--primary'))
        if isload:
            self.loading()
        else:
            time.sleep(2)

    def click_reset_query_button(self):
        """
        重置查询条件
        :return:
        """
        self.click_element(('css', '.el-form-item__content > .el-button--default'))
        time.sleep(2)

    def click_show_more_query(self):
        """
        点击展开/收起按钮
        :return:
        """
        self.click_element(('css', '.el-button:nth-child(3) > span'))
        time.sleep(2)

    def select_pull_down_list(self, locator, value):
        """
        查询哪里的下拉列表选择
        :param value:
        :param locator:
        :return:
        """
        ele = self.get_element(locator)
        ele.send_keys(value)
        time.sleep(1)
        ele.send_keys(Keys.DOWN)
        time.sleep(1)
        ele.send_keys(Keys.ENTER)

