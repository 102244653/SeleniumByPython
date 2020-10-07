import configparser
import os

import vlt_path


class ReadConfig(object):

    def __init__(self, path=None):
        if path:
            config_path = path
        else:
            root_dir = vlt_path.get_path()
            config_path = os.path.join(root_dir, 'src/config/config.ini')
        self.cf = configparser.ConfigParser()
        self.cf.read(config_path)

    def get_env(self, param):
        """
        读取测试url
        :param param:
        :return:
        """
        return self.cf.get('env', param)

    def get_account(self, param):
        """
        读取测试账号信息
        :param param:
        :return:
        """
        res = self.cf.get('account', param).split('|')
        return res[0], res[1]

    def get_driver_path(self, dr, param):
        """
        读取浏览器驱动地址
        :param dr:
        :param param:
        :return:
        """
        return self.cf.get(dr, param)


data = ReadConfig()

if __name__ == '__main__':
    d = data.get_driver_path('local', 'firefox')
    print(d)