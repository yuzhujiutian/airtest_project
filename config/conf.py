#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os

# 项目目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 日志目录
LOG_PATH = os.path.join(BASE_DIR, 'log')

# 测试日志
AIRTEST_LOG = os.path.join(BASE_DIR, 'log', 'airtest')

# config.ini
INI_PATH = os.path.join(BASE_DIR, 'config', 'config.ini')

# 页面数据
YAML_PATH = os.path.join(BASE_DIR, 'page_element')

# airtest_img
PAGE_IMG = os.path.join(BASE_DIR, 'page_images')

# report_path
REPORT_PATH = os.path.join(BASE_DIR, "report")

if __name__ == '__main__':
    print(BASE_DIR)
