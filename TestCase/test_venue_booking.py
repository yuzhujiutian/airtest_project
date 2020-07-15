#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import pytest
import allure
from pytest import assume
from core.aircore import *
from utils.times import strftime
from pages.homepage import back_home


@allure.feature("场地预约")
class TestVenueBooking:
    """测试活动场地"""

    @allure.story("测试预约热力篮球场地！")
    def test_001(self):
        """场地预约"""
        d.poco_click(text="场地预约")
        d.poco_click(text="查看详情", index=0)
        d.poco_click(text="获取手机号")
        d.poco_click(text="允许")
        with assume: assert d.poco_exists(text="18092206143")
        d.poco_click(text="选择入园时间")
        d.poco_click(text="确定")
        page_time = strftime("%Y-%m-%d")
        now_days = d.poco_exists(text=page_time)
        with assume: assert now_days
        d.poco_click(text="确认预约")
        with assume: assert d.poco_exists(text="用户已预约场地") != d.poco_exists(text='热力篮球预约成功')
        back_home()
        d.poco_click(text="我的")
        d.poco_click(text="我的场地")
        with assume: assert d.poco_exists(text=page_time)
        with assume: assert d.poco_exists(text="预约成功")
        d.poco_click(text=page_time)
        d.poco_exists(text="热力篮球预约成功")
        d.poco_click(text="取消预约")
        d.poco_click(text="确定")
        with assume: assert d.poco_exists(text="取消预约成功")


if __name__ == '__main__':
    pytest.main([''])
