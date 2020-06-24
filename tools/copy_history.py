#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

sys.path.append('.')
__author__ = '1084502012@qq.com'

import os
import shutil
from config.conf import ALLURE_REPORT, ALLURE_RESULTS


def copy_history():
    start_path = os.path.join(ALLURE_REPORT, 'history')
    end_path = os.path.join(ALLURE_RESULTS, 'history')
    if os.path.exists(end_path):
        shutil.rmtree(end_path)
    try:
        shutil.copytree(start_path, end_path)
    except FileNotFoundError:
        print("allure-results上一次历史数据不存在！")


if __name__ == '__main__':
    copy_history()
