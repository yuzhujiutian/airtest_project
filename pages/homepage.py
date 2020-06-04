#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

sys.path.append('.')
__author__ = '1084502012@qq.com'
import functools
from basic.base import *
from common.readimg import ReadImg

index_img = ReadImg('index')


def case_name(func):
    """用例名称"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        log("##测试用例名称：{}##{}".format(func.__name__, func.__doc__))
        return func(*args, **kwargs)

    return wrapper


def back_home():
    """返回首页"""
    while not d.airtest_exists(index_img['运动打卡_参与排名']):
        try:
            d.poco(resourceId='com.tencent.mm:id/q0').click()
        except poco_error.PocoNoSuchNodeException:
            d.poco_click(text="首页")
