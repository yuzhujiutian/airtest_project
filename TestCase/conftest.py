#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

sys.path.append('.')
__author__ = '1084502012@qq.com'
__title__ = "曲江池遗址公园小程序测试报告"

import allure
import pytest
from tools.reports import get_report
from pages.homepage import back_home


@allure.story("生成airtest报告")
@pytest.fixture(scope='class')
def generate_report(request):
    """生成报告"""

    def fn():
        get_report(__file__, 'log.html', log_root='./log')

    request.addfinalizer(fn)


@pytest.fixture(scope='function', autouse=True)
def applet_home(request):
    """回到小程序首页"""
    back_home()

    def fn():
        back_home()

    request.addfinalizer(fn)
