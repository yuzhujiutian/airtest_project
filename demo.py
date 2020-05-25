#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

sys.path.append('.')
__author__ = '1084502012@qq.com'


def aaa():
    """你好"""
    print(1)


print(aaa.__doc__)
print(aaa.__name__)


print(repr("/user/bin/python3"))