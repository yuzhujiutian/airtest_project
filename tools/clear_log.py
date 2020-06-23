#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

sys.path.append('.')
__author__ = '1084502012@qq.com'

import os
import shutil
from config.conf import ALLURE_RESULTS, ALLURE_REPORT, REPORT_PATH


def copy_history():
    start_path = os.path.join(ALLURE_REPORT, 'history')
    end_path = os.path.join(ALLURE_RESULTS, 'history')
    if os.path.exists(end_path):
        shutil.rmtree(end_path)
    try:
        shutil.copytree(start_path, end_path)
    except FileNotFoundError:
        print("allure-results上一次历史数据不存在！")


def clear_allure():
    """清理日志"""
    ver = True
    if not os.path.exists(ALLURE_RESULTS):
        os.makedirs(ALLURE_RESULTS)
    for i in os.listdir(ALLURE_RESULTS):
        file = os.path.join(ALLURE_RESULTS, i)
        if os.path.isfile(file):
            os.remove(file)
            print("删除{}！".format(file))
            ver = False
    if ver:
        print("没有删除任何allure相关文件！")


def clear_airtest_report():
    var = True
    for i in os.listdir(REPORT_PATH):
        new_path = os.path.join(REPORT_PATH, i)
        if os.path.isdir(new_path):
            shutil.rmtree(new_path)
            print("删除{}成功！".format(new_path))
            var = False
    if var:
        print("没有删除任何allure相关文件！")


if __name__ == '__main__':
    clear_allure()
    copy_history()
