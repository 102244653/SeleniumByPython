import os
import sys

sys.path.append('../')


def get_path():
    # 获取根目录的绝对路径
    return os.path.split(os.path.realpath(__file__))[0]

