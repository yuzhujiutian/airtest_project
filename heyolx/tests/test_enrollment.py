#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import pytest
import allure
from config import elements
from common.readimg import *
from common.readyaml import ReadYaml

page_data = ReadYaml(elements['heyolx'], 'page_data')


@allure.feature("活动报名")
class TestEnrollment:
    """活动报名"""

    @allure.story("测试选择第一个活动进行报名")
    def test_004(self, d):
        """测试选择第一个活动进行报名"""
        d.poco_click(text="活动报名")
        pytest.assume(d.poco_wait_all([d.poco(text=x) for x in page_data['活动报名']]))
        d.poco_click(text='运动活动')
        d.poco_click(text='2020慢跑曲江池')
        if d.poco_exists(text='已报名'):
            d.poco_click(text='查看报名信息')
            d.touch(d.temp(act_img['关闭报名信息']))
        elif d.poco_exists(text="该活动已结束"):
            print("活动已结束")
        else:
            d.poco_click(text='立即报名')


if __name__ == '__main__':
    pytest.main(['test_enrollment.py'])
