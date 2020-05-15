#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

sys.path.append('.')
__author__ = '1084502012@qq.com'

import pytest
from basic.base import d
from common.readimg import ReadImg

index_img = ReadImg('index')
my_img = ReadImg('my')


class TestQujiangPool:
    """曲江池遗址公园"""

    def test_001(self):
        """测试头像"""
        print(d.device_id)
        d.airtest_wait(index_img['运动打卡_参与排名'])
        d.poco_click(text="我的")
        d.assert_exist(my_img['我的头像'])
        result = d.poco_get_text(textMatches="^客服：.*$")
        print(result)


if __name__ == '__main__':
    pytest.main()
