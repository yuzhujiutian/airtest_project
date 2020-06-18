#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

sys.path.append('.')
__author__ = '1084502012@qq.com'

from basic.base import *
from common.readimg import index_img


def back():
    """后退"""
    d.poco_click(name='com.tencent.mm:id/da')



def home_identify():
    """首页识别"""
    return d.exists(d.temp(index_img['运动打卡_参与排名']))


def back_home():
    """返回首页"""
    while not home_identify():
        try:
            back()
        except poco_error.PocoTargetTimeout:
            d.poco_click(text="首页")
            d.poco_scroll(percent=-0.6)
