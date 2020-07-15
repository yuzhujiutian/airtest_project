#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import allure
import pytest
from pytest import assume
from core.aircore import *
from common.readimg import *
from pages.homepage import back
from common.readyaml import page_data


@allure.feature("各类活动和景点介绍")
class TestIntroduce:
    """各类活动和景点介绍"""

    @allure.story("测试景区介绍")
    def test_001(self):
        """景区介绍"""
        for i in page_data['景区介绍']:
            if not d.poco_exists(text=i):
                d.poco_scroll()
            d.poco_click(text=i)
            d.poco_exists(text=page_data['景区介绍'][i])
            d.poco_click(text='商业服务')
            back()

    @allure.story("测试各类活动")
    def test_003(self):
        """各类活动"""
        d.poco_click(text="各类活动")
        for i in page_data['各类活动']:
            d.poco_click(text=i)
            if i == "传统文化活动":
                with assume: assert d.poco_wait_all([d.poco(text=x) for x in page_data['各类活动'][i]])
        else:
            d.assert_exists(d.temp(act_img['金缘阁喜饼']))


if __name__ == '__main__':
    pytest.main(['test_introduce.py'])
