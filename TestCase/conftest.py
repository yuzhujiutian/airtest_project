#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = '1084502012@qq.com'
__title__ = "曲江池遗址公园小程序测试报告"

import pytest
from pages.homepage import back_home


@pytest.fixture(scope='function', autouse=True)
def applet_home(request):
    """回到小程序首页"""
    back_home()

    def fn():
        back_home()

    request.addfinalizer(fn)
