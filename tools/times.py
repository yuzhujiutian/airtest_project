#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

sys.path.append('.')
__author__ = '1084502012@qq.com'

import time
import datetime
from airtest.report.report import timefmt
from airtest.core.api import sleep


def timestamp():
    """时间戳"""
    return time.time()


def strftime(fmt="%Y%m%d%H%M%S"):
    """格式化时间"""
    return time.strftime(fmt, time.localtime())


def now_time():
    """现在时间"""
    return datetime.datetime.now()


def timefmts():
    """格式化时间"""
    return timefmt(timestamp())


if __name__ == '__main__':
    print(strftime())
