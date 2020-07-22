#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
from common.readconfig import ReadConfig

# 项目目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 日志目录
LOG_PATH = os.path.join(BASE_DIR, 'log')

# 测试日志
AIRTEST_LOG = os.path.join(BASE_DIR, 'log', 'airtest')

# report_path
REPORT_PATH = os.path.join(BASE_DIR, "report")

apps = {
    'heyolx': os.path.join(BASE_DIR, 'heyolx')
}

# config.ini
ini = {
    'heyolx': ReadConfig(os.path.join(apps['heyolx'], 'config.ini'))
}

# 页面数据
elements = {
    'heyolx': os.path.join(BASE_DIR, 'heyolx', 'element')
}

# airtest_img
airImg = {
    'heyolx': os.path.join(BASE_DIR, 'heyolx', 'images')
}

if __name__ == '__main__':
    print(ini['heyolx'].package_name)
