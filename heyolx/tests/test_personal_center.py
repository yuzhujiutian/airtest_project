#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import pytest
import allure
from common.readimg import *


class TestPersonalCenter:
    """个人中心"""

    @allure.story("验证头像")
    @allure.description("验证微信头像与曲江池遗址公园的头像一致")
    def test_001(self, d):
        """验证头像"""
        d.poco_click(text="我的")
        d.assert_exists(d.temp(my_img['我的头像']))
        result = d.poco_text(textMatches="^客服：.*$")
        pytest.assume(result == "客服：12083478349")


if __name__ == '__main__':
    pytest.main(['test_personal_center.py'])
