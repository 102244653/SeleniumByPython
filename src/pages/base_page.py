import time

import pyperclip
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
        alert = ('xpath', '//div[@aria-label="{}"]/div/div[3]/button[1]'.format(alter_name))
        if self.wait_exist(alert):
            self.click_element(alert)
        else:
            print('[{}]弹窗不存在'.format(alter_name))

    def alert_confirm(self, alter_name):
        """
        提示弹窗确认
        :return:
        """
        alert = ('xpath', '//div[@aria-label="{}"]/div/div[3]/button[1]'.format(alter_name))
        if self.wait_exist(alert):
            self.click_element(alert)
        else:
            print('[{}]弹窗不存在'.format(alter_name))

    def alert_close(self, alter_name):
        """
        提示弹窗的关闭按钮
        :return:
        """
        alert = ('xpath', '//div[@aria-label="{}"]//button[@aria-label="Close"]'.format(alter_name))
        if self.wait_exist(alert):
            self.click_element(alert)
        else:
            print('[{}]弹窗不存在'.format(alter_name))

    def alert_list_close(self, alert_name=[]):
        """
        多个弹窗关闭：比如某个页面有多种标题弹窗，可以使用这个函数做后置操作
        :param alert_name: 弹窗明list
        :return:
        """
        for alert in alert_name:
            self.alert_close(alert)

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
        :param is_center: 默认选择：中国福利彩票
        """
        self.click_element(locator)
        time.sleep(1)
        if is_center:
            # 中福彩
            self.click_element(('xpath', '//li[starts-with(@id,"cascader-menu")]/label/span/span'))
        else:
            self.click_element(('xpath', '//li[starts-with(@id,"cascader-menu")]/span'))
            # 北京
            self.click_element(('xpath', '//div[@class="el-cascader-panel"]/div[2]/div[1]/ul[1]/li[1]/label[1]'))
        time.sleep(1)
        self.click_element(locator)

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

    def select_pull_down_list(self, locator, value, is_down=True):
        """
        查询哪里的下拉列表选择
        :param value:
        :param locator:
        :param is_down: 是否直接按回车键
        :return:
        """
        ele = self.get_element(locator)
        self.clear_text(ele)
        ele.send_keys(value)
        time.sleep(1)
        if is_down:
            ele.send_keys(Keys.DOWN)
            time.sleep(1)
        ele.send_keys(Keys.ENTER)
        time.sleep(1)

    def swipe_page(self, desc):
        """
        页面滑动,一次到位
        :param desc: 滑动方向：up 上/down 下/center 居中/ rl 左右居中
        :return:
        """
        if desc == 'up':
            js = 'document.getElementsByClassName("main")[0].scrollTo(0,0)'
        elif desc == 'down':
            js = 'document.getElementsByClassName("main")[0].scrollTo(0,10000)'
        elif desc == 'center':
            js = 'scrollBy(0.0-document.body.scrollHeight * 1/2)'
        elif desc == 'rl':
            js = 'scrollBy(0.0-document.body.scrollWidht * 1/2)'
        self.driver.execute_script(js)

    def swipe_down_find_ele(self, locator):
        """
        下滑查找某个元素是否存在
        :param locator:
        :return:
        """
        js = 'document.getElementsByClassName("main")[0].scrollTo(0,150)'
        is_exist = False
        for i in range(10):
            if not self.wait_exist(locator):
                self.driver.execute_script(js)
            else:
                is_exist = True
                break
        return is_exist

    def click_button(self, btn_name):
        """
        点击按钮，传入按钮名称
        :param btn_name:
        :return:
        """
        btn = ('xpath', '//span[contains(.,"{}")]'.format(btn_name))
        if self.wait_exist(btn):
            self.click_element(btn)
            self.loading(2)
        else:
            print('未查找到{}按钮'.format(btn_name))

    def do_upload_window(self, astr='None'):
        """
        上传文件弹窗处理
        python的剪切板操作，先传入一个值写入剪切板然后进行粘贴,在点击确认按钮
        :param astr:
        :return:
        """
        time.sleep(2)
        pyperclip.copy(astr)
        pyperclip.paste()
        self.driver.send_keys(Keys.ENTER)
        self.loading()


    def get_search_count(self):
        """
            获取搜索记录数(通用)
        :return:
        """
        search_count = ('css', 'div[class="search-bar-comp"]>div>p>span>em')
        return self.get_element(search_count).text


    def click_button_contain_of_id(self, part_id="detail", postion=2, isload=False):
        """
            点击包含Id的按钮
        :param part_id: add,delete,edit,detail 等等按钮。 （注意是button类且包含id的按钮）
        :param postion: 默认出现二个同ID元素的比较多
        :param isload: 等待加载
        :return:
        """
        selector = f'(//button[contains(@id,"{part_id}")])[{postion}]'
        self.click_element(('xpath', selector))
        if isload:
            self.loading()
        else:
            time.sleep(2)
