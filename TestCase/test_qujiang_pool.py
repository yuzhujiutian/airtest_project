#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

sys.path.append('.')
__author__ = '1084502012@qq.com'
__title__ = "曲江池遗址公园小程序测试报告"
__desc__ = """
用例1: 测试头像是否与微信头像一致
用例2: 预约一个场地，然后取消预约
"""

import pytest
import functools
from basic.base import *
from tools.times import strftime
from common.readimg import ReadImg
from tools.reports import get_report

index_img = ReadImg('index')
my_img = ReadImg('my')


def back_home():
    """返回首页"""
    while not d.airtest_exists(index_img['运动打卡_参与排名']):
        try:
            d.poco(resourceId='com.tencent.mm:id/q0').click()
        except PocoNoSuchNodeException:
            d.poco_click(text="首页")


def case_name(func):
    """用例名称"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        log("##测试用例名称：{}##{}".format(func.__name__, func.__doc__))
        return func(*args, **kwargs)

    return wrapper


class TestQujiangPool:
    """曲江池遗址公园"""

    @pytest.fixture(scope='class', autouse=True)
    def generate_report(self, request):
        """生成报告"""

        def fn():
            get_report(__file__, 'log.html', log_root='./log')

        request.addfinalizer(fn)

    @pytest.fixture(scope='function', autouse=True)
    def applet_home(self, request):
        """回到小程序首页"""
        back_home()

        def fn():
            back_home()

        request.addfinalizer(fn)

    @case_name
    def test_001(self):
        """测试头像"""
        d.poco_click(text="我的")
        d.assert_exists(my_img['我的头像'])
        result = d.poco_get_text(textMatches="^客服：.*$")
        assert_equal(result, "客服：12083478349")

    @case_name
    def test_002(self):
        """场地预约"""
        d.poco_click(text="场地预约")
        d.poco_click(text="查看详情", index=0)
        d.poco_click(text="获取手机号")
        d.poco_click(text="允许")
        assert_equal(d.poco_exists(text="18092206143"), True)
        d.poco_click(text="选择入园时间")
        d.poco_click(text="确定")
        page_time = strftime("%Y-%m-%d")
        now_days = d.poco_exists(text=page_time)
        assert_equal(now_days, True)
        d.poco_click(text="确认预约")
        assert_not_equal(d.poco_exists(text="用户已预约场地"),
                         d.poco_exists(text='热力篮球预约成功'))
        back_home()
        d.poco_click(text="我的")
        d.poco_click(text="我的场地")
        assert_equal(d.poco_exists(text=page_time), d.poco_exists(text="预约成功"))
        d.poco_click(text=page_time)
        d.poco_exists(text="热力篮球预约成功")
        d.poco_click(text="取消预约")
        d.poco_click(text="确定")
        assert_equal(d.poco_exists(text="取消预约成功"), True)


if __name__ == '__main__':
    pytest.main(['test_qujiang_pool.py'])
