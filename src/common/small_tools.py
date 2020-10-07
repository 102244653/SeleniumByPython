import os
import time
from datetime import datetime
from random import random
from src.common.log import Logger

log = Logger().get_logger()


class SmallTool:

    @staticmethod
    def sleep(timeout=10):
        time.sleep(timeout)

    @staticmethod
    def week_id():
        """
        获取当前的时间：周日-周六：0-6
        :return:
        """
        now_time = datetime.now()
        return int(now_time.strftime('%w'))

    @staticmethod
    def week_name():
        return datetime.now().strftime('%A')

    @staticmethod
    def week_simple_name():
        return datetime.now().strftime('%a')

    @staticmethod
    def create_mobile():
        return u'135' + str(int(time.time()))[2:]

    @staticmethod
    def create_identity_card():
        return str(int(time.time())) + str(random.randint(1000000, 9999999))

    @staticmethod
    @property
    def get_str(num=4):
        """
        获取随机字符串
        :param num:
        :return:
        """
        return ''.join(random.sample(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'z', 'y', 'x', 'w', 'v', 'u',
                                      't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e',
                                      'd', 'c', 'b', 'a'], num))

    @staticmethod
    def next_day():
        return (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def get_cell_xpath(locator, point):
        m, p = locator[1]
        p = p.format(point[0], point[1])
        return tuple(m, p)

    @staticmethod
    def kill_process(p_name):
        """
        检查并杀死未关闭的进程
        :return:
        """
        # 检查命令  tasklist |findstr "chromedriver"
        # 强制杀死命令  taskkill /f /t /im "chromedriver.exe"
        try:
            if os.popen('tasklist | findstr "{}"'.format(p_name)):
                t = os.popen('taskkill /f /t /im "{}"'.format(p_name))
                log.info(t.read())
        except:
            log.error('杀死{}进程失败'.format(p_name))
        time.sleep(2)

