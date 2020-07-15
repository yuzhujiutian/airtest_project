#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import shutil
from config.conf import REPORT_PATH


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
    clear_airtest_report()
