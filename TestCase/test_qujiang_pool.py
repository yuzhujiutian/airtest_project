#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

sys.path.append('.')
__author__ = '1084502012@qq.com'
__title__ = "曲江池遗址公园小程序测试报告"
__desc__ = """
用例1： 测试头像是否与微信头像一致

"""

import pytest
from basic.base import d
import config.conf as cfg
from common.readimg import ReadImg
from tools.reports import get_report, report_path

index_img = ReadImg('index')
my_img = ReadImg('my')


@pytest.fixture(scope='module', autouse=True)
def generate_report(request):
    """生成报告"""

    def fn():
        get_report(__file__, 'log.html', log_root='./log', export=report_path())

    request.addfinalizer(fn)


class TestQujiangPool:
    """曲江池遗址公园"""

    def test_001(self):
        """测试头像"""
        print(d.device_id)
        d.airtest_wait(index_img['运动打卡_参与排名'])
        d.poco_click(text="我的")
        d.assert_exists(my_img['我的头像'])
        result = d.poco_get_text(textMatches="^客服：.*$")
        print(result)


if __name__ == '__main__':
    pytest.main()
