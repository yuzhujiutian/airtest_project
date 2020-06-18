#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

sys.path.append('.')
__author__ = '1084502012@qq.com'

import pytest
import allure
from pytest import assume
from basic.base import *
from common.readimg import *
from common.readyaml import page_data


@allure.feature("活动报名")
class TestEnrollment:
    """活动报名"""

    @allure.story("测试选择第一个活动进行报名")
    def test_004(self):
        """测试选择第一个活动进行报名"""
        d.poco_click(text="活动报名")
        with assume:
            assert d.poco_wait_all([d.poco(text=x) for x in page_data['活动报名']])
        d.poco_click(text='运动活动')
        d.poco_click(text='2020慢跑曲江池')
        if d.poco_exists(text='已报名'):
            d.poco_click(text='查看报名信息')
            d.touch(d.temp(act_img['关闭报名信息']))
        else:
            d.poco_click(text='立即报名')


if __name__ == '__main__':
    pytest.main(['test_enrollment.py'])
