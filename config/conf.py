#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

sys.path.append('.')
__author__ = '1084502012@qq.com'

import os

# 项目目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 日志目录
LOG_PATH = os.path.join(BASE_DIR, 'log')

# 测试日志
TEST_LOG = os.path.join(BASE_DIR, 'TestCase', 'log')

# config.ini
INI_PATH = os.path.join(BASE_DIR, 'config', 'config.ini')

# 页面数据
YAML_PATH = os.path.join(BASE_DIR, 'page_element')

# airtest_img
AIR_IMG_PATH = os.path.join(BASE_DIR, 'airtest_img')

# 测试用例
TEST_CASE = os.path.join(BASE_DIR, 'TestCase')

# report_path
REPORT_PATH = os.path.join(BASE_DIR, "report")

# ALLURE_RAW_RESULTS
ALLURE_RESULTS = os.path.join(BASE_DIR, 'allure-results')

# ALLURE_DIR
ALLURE_REPORT = os.path.join(BASE_DIR, 'allure-report')

if __name__ == '__main__':
    print(BASE_DIR)
