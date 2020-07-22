#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from core.aircore import *
from common.readimg import index_img


def back(d):
    """后退"""
    d.poco_click(name='com.tencent.mm:id/da')


def home_identify(d):
    """首页识别"""
    return d.exists(d.temp(index_img['运动打卡_参与排名']))


def back_home(d):
    """返回首页"""
    while not home_identify(d):
        try:
            back(d)
        except poco_exception.PocoTargetTimeout:
            d.poco_click(text="首页")
            d.poco_scroll(percent=-0.6)
