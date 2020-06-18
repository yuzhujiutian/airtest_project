#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

sys.path.append('.')
__author__ = '1084502012@qq.com'

import os
import subprocess
from datetime import datetime
from config.conf import ALLURE_DIR

allure_test_dir = './report/allure'


def clear_allure():
    """清理日志"""
    ver = True
    if not os.path.exists(allure_test_dir):
        os.makedirs(allure_test_dir)
    for i in os.listdir(allure_test_dir):
        file = os.path.join(allure_test_dir, i)
        if os.path.isfile(file):
            os.remove(file)
            print("删除{}！".format(file))
            ver = False
    if ver:
        print("没有删除任何allure相关文件！")


def export_dir():
    """导出目录"""
    export = os.path.join(ALLURE_DIR, datetime.now().strftime("%Y%m%d%H%M%S"))
    if not os.path.exists(export):
        os.makedirs(export)
    return export


def main():
    """主函数"""
    clear_allure()
    export_dirname = export_dir()
    subprocess.call(['pytest', '--alluredir', allure_test_dir])
    subprocess.call(['allure', 'generate', allure_test_dir, '-o', export_dirname])
    subprocess.call(['allure', 'open', export_dirname])


if __name__ == '__main__':
    main()
