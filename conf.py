#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

sys.path.append('.')
__author__ = '1084502012@qq.com'

import os

# 项目目录
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# 日志目录
LOG_PATH = os.path.join(BASE_DIR, 'logs')

if __name__ == '__main__':
    print(BASE_DIR)
