#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

sys.path.append('.')
__author__ = '1084502012@qq.com'

import os

sogou = ""

# 项目目录
BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# 日志目录
LOG_PATH = os.path.join(BASE_DIR, 'log')

# config.ini
INI_PATH = os.path.join(BASE_DIR, 'config', 'config.ini')

# airtest_img
AIR_IMG_PATH = os.path.join(BASE_DIR, 'airtest_img')

# report_path
REPORT_PATH = os.path.join(BASE_DIR, "report")

# testcase
TEST_CASE_LOG = os.path.join(BASE_DIR, 'TestCase', 'log')

if __name__ == '__main__':
    print(BASE_DIR)
