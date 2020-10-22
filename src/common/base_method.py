import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from src.common.log import Logger

log = Logger().get_logger()


class BaseMethod:
    """
    111
    """
    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(driver)

    def get_text_locator(self, text, class_name=None):
        """
        返回locator
        :param text:
        :param class_name:
        :return:
        """
        if class_name is None:
            loc = ('xpath', '//*[@text="{}"]'.format(class_name, text))
        else:
            loc = ('xpath', '//{}[@text="{}"]'.format(class_name, text))
        return loc

    def get_element(self, locator, index=0):
        """
        获取控件
        :param locator:
        :param index:
        :return:
        """
        method = locator[0]
        values = locator[1]
        if index == 0:
            ele = self.get_element_by_type(method, values)
        else:
            ele = self.get_elements_by_type(method, values)[index]
        return ele

    def get_elements(self, locator):
        """
        获取满足条件的所有控件
        :param locator:
        :return:
        """
        method = locator[0]
        values = locator[1]
        if type(values) is str:
            return self.get_elements_by_type(method, values)
        elif type(values) is list:
            for value in values:
                try:
                    return self.get_elements_by_type(method, value)
                except NoSuchElementException as e:
                    print(e)
                    pass
            raise NoSuchElementException

    def get_text(self, locator):
        '''
        获取字符串
        :param locator:
        :return:
        '''
        if isinstance(locator, tuple):
            el = self.get_element(locator)
        else:
            el = locator
        return el.text

    def wait(self, timeout=10):
        '''
        等待
        :param ec:
        :param timeout:
        :return:
        '''
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.ID, 'no element')))
        except:
            pass

    def wait_exist(self, locator, timeout=8):
        '''
        等待控件出现
        :param locator:
        :param timeout:
        :return:
        '''
        try:
            ele = WebDriverWait(self.driver, timeout, 1).until(EC.visibility_of_element_located(locator))
        except Exception as e:
            print(e)
            return False
        if ele:
            return True
        else:
            return False

    def wait_not_exist(self, locator, timeout=10):
        '''
        等待存在的控件消失
        :param locator:
        :param timeout:
        :return:
        '''
        try:
            if WebDriverWait(self.driver, timeout, 0.5).until(EC.invisibility_of_element_located(locator)):
                flag = True
        except Exception as e:
            print(e)
            flag = False
        return flag

    def is_clickable(self, locator):
        """
        元素是否可以点击
        """
        if isinstance(locator, tuple):
            el = self.get_element(locator)
        else:
            el = locator
        if el.get_attribute('disable'):
            return True
        else:
            return False

    # def wait_clickable(self, locator, timeout=10):
    #     '''
    #     等待控件可点击
    #     :param locator:
    #     :param timeout:
    #     :return:
    #     '''
    #     if isinstance(locator, tuple):
    #         el = self.get_element(locator)
    #     else:
    #         el = locator
    #
    #     end = time.time() + timeout
    #     while time.time() < end:
    #         if el.get_attribute('clickable') == 'true':
    #             return True
    #         time.sleep(1)
    #     return False

    def clear_text(self, locator):
        """
        send_keys(Keys.BACK_SPACE)：删除键(BackSpace)
        send_keys(Keys.SPACE)：空格键(Space)
        send_keys(Keys.TAB)：制表键(TAB)
        send_keys(Keys.ESCAPE)：回退键(ESCAPE)
        send_keys(Keys.ENTER)：回车键(ENTER)
        send_keys(Keys.CONTROL,'a')：全选(Ctrl+A)
        send_keys(Keys.CONTROL,'c')：复制(Ctrl+C)
        send_keys(Keys.CONTROL,'x')：剪切(Ctrl+X)
        send_keys(Keys.CONTROL,'v')：粘贴(Ctrl+V)
        send_keys(Keys.F1)：键盘F1
        .....
        send_keys(Keys.F12)：键盘F12
        """
        if isinstance(locator, tuple):
            el = self.get_element(locator)
        else:
            el = locator
        el.click()
        el.send_keys(Keys.CONTROL, 'a')
        el.send_keys(Keys.BACK_SPACE)

    def send_keys(self, locator, text):
        '''
        带检查的文本输入，保证输入的字符串无误
        :param locator:
        :param text:
        :param times:
        :return:
        '''
        if isinstance(locator, tuple):
            el = self.get_element(locator)
        else:
            el = locator
        try:
            self.clear_text(el)
        except:
            pass
        el.send_keys(text)

    def get_ele_attr(self, locator, attr_name):
        '''
        获取元素指定属性
        :param locator: 元素定位方式
        :param attr_name:属性名
        :return:
        '''
        if isinstance(locator, tuple):
            ele = self.get_element(locator)
        else:
            ele = locator
        return ele.get_attribute(attr_name)

    def get_element_by_type(self, method, value):
        msg = 'selenium.common.exceptions.FindElementTimeoutException:' \
              ' ("{}", "{}") could not be located on the page using the given search parameters.'.format(method, value)

        if method == 'id':
            locator = (By.ID, value)
        elif method == 'class':
            locator = (By.CLASS_NAME, value)
        elif method == 'css':
            locator = (By.CSS_SELECTOR, value)
        elif method == 'link_text':
            locator = (By.LINK_TEXT, value)
        elif method == 'tag':
            locator = (By.TAG_NAME, value)
        elif method == 'xpath':
            locator = (By.XPATH, value)
        elif method == 'name':
            locator = (By.NAME, value)
        else:
            raise Exception('Invalid locator method.')
        # return self.driver.find_element(locator[0], locator[1])
        # 每次查找元素最多等待10s，每隔0.5s查找一次
        return WebDriverWait(self.driver, 20, 0.5).until(EC.visibility_of_element_located(locator), msg.format(value))

    def get_elements_by_type(self, method, value):
        """

        :param method:
        :param value:
        :return:
        """
        if method == 'id':
            locator = (By.ID, value)
        elif method == 'class':
            locator = (By.CLASS_NAME, value)
        elif method == 'css':
            locator = (By.CSS_SELECTOR, value)
        elif method == 'tag':
            locator = (By.TAG_NAME, value)
        elif method == 'xpath':
            locator = (By.XPATH, value)
        elif method == 'link_text':
            locator = (By.LINK_TEXT, value)
        elif method == 'name':
            locator = (By.NAME, value)
        else:
            raise Exception('Invalid locator method.')
        return self.driver.find_elements(locator[0], locator[1])

    def get_size(self):
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']
        return width, height

    def page_source(self):
        '''
        获取当前页面所有控件信息
        :return:
        '''
        return self.driver.page_source

    def execute_command(self, command, desc):
        self.driver.execute_script(command, desc)

    def screen_shot(self, path):
        """
        截取屏幕
        :return:
        """
        self.driver.get_screenshot_as_file(path)

    def find_toast(self, message=None):
        """
        查找toast元素
        :param message:
        :return:
        """
        if message:
            toast_element = (By.XPATH, '//p[starts-with(@text,"{}")]'.format(message))
        else:
            toast_element = (By.XPATH, '//div[@role="alert"]/p')
        try:
            toast = WebDriverWait(self.driver, 10, 0.1).until(EC.visibility_of_element_located(toast_element))
        except Exception as e:
            print(e)
            toast = None
        return toast

    def move_to_element(self, locator):
        """
        将鼠标移动到控件
        :param locator:
        :param index:
        :return:
        """
        if isinstance(locator, tuple):
            el = self.get_element(locator)
        else:
            el = locator
        self.action.move_to_element(el).perform()
        time.sleep(5)

    def click_element(self, locator):
        """
        点击元素
        :param locator:
        :return:
        """
        if isinstance(locator, tuple):
            el = self.get_element(locator)
        else:
            el = locator
        el.click()

    def select_value(self, locator, value):
        """
        下拉框选项
        :param locator:
        :param value: value=value/text=text,index=1
        :return:
        """
        if isinstance(locator, tuple):
            el = self.get_element(locator)
        else:
            el = locator
        select = Select(el)
        _s = value.split('=')[0].strip().lower()
        _v = value.split('=')[1].strip().lower()

        if _s == 'value':
            select.deselect_by_value(_v)
        elif _s == 'text':
            select.deselect_by_visible_text(_v)
        elif _s == 'index':
            select.deselect_by_index(_v)

    def clear_select(self, locator):
        """
        取消选择的下拉框
        :param locator:
        :return:
        """
        if isinstance(locator, tuple):
            el = self.get_element(locator)
        else:
            el = locator
        select = Select(el)
        select.deselect_all()

    def all_select(self, locator):
        """
        全选
        :param locator:
        :return:
        """
        if isinstance(locator, tuple):
            el = self.get_element(locator)
        else:
            el = locator
        select = Select(el)
        select.all_selected.options
        return select.options

    def drag_to_element(self, start_ele, end_ele):
        """
        拖动元素
        :param start_ele:
        :param end_ele:
        :return:
        """
        if isinstance(start_ele, tuple):
            el1 = self.get_element(start_ele)
        else:
            el1 = start_ele
        if isinstance(end_ele, tuple):
            el2 = self.get_element(end_ele)
        else:
            el2 = end_ele

        self.action.drag_and_drop(el1, el2).perform()

    def switch_to_window(self, windowName):
        """
        切换浏览器窗口
        :param handle:
        :return:
        """
        for handle in self.driver.window_handles:
            if handle in windowName:
                self.driver.switch_to_window(handle)
        raise Exception('切换窗口[%s]失败')

    def switch_to_iframe(self, iframe):
        """
        切换iframe
        :param iframe:
        :return:
        """
        if isinstance(iframe, tuple):
            el1 = self.get_element(iframe)
        else:
            el1 = iframe
        self.driver.switch_to_frame(el1)

    def out_to_iframe(self):
        """
        退出iframe
        :return:
        """
        self.driver.switch_to_default_content()

    def focus_on_element(self, locator):
        """
        焦点移动到某个元素上
        :param locator:
        :return:
        """
        if isinstance(locator, tuple):
            ele = self.get_element(locator)
        else:
            ele = locator
        self.driver.execute_script("arguments[0].focus();", ele)

    def change_element_attr(self, locator, attr=()):
        """
        修改元素属性
        :param locator:
        :param attr:
        :return:
        """
        if isinstance(locator, tuple):
            ele = self.get_element(locator)
        else:
            ele = locator
        self.driver.execute_script("arguments[0].setAttribute(arguments[1],arguments[2])", ele, attr[1], attr[2])

    def delete_element_attr(self, locator, attr):
        """
        移除元素属性
        :param locator:
        :param attr:
        :return:
        """
        if isinstance(locator, tuple):
            ele = self.get_element(locator)
        else:
            ele = locator
        self.driver.execute_script("arguments[0].removeAttribute(arguments[1])", ele, attr)

    # 向一个认证的对话框发送用户名和密码，会自动点击确认
    # driver.switch_to.alert.authenticate('cheese','secretGouda')


