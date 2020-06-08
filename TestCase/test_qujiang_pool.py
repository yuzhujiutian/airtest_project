#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

sys.path.append('.')
__author__ = '1084502012@qq.com'
__title__ = "曲江池遗址公园小程序测试报告"
__desc__ = """
用例1: 测试头像是否与微信头像一致
用例2: 预约一个场地，然后取消预约
用例3：查看各类活动
用例4：测试活动报名
用例5：测试导览中的景点在地图中的显示
"""

import pytest
from basic.base import *
from common.readimg import *
from common.readyaml import page_data
from tools.times import strftime
from tools.reports import get_report
from pages.homepage import back_home, case_name, back


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
        air_api.assert_equal(result, "客服：12083478349")

    @case_name
    def test_002(self):
        """场地预约"""
        d.poco_click(text="场地预约")
        d.poco_click(text="查看详情", index=0)
        d.poco_click(text="获取手机号")
        d.poco_click(text="允许")
        air_api.assert_equal(d.poco_exists(text="18092206143"), True)
        d.poco_click(text="选择入园时间")
        d.poco_click(text="确定")
        page_time = strftime("%Y-%m-%d")
        now_days = d.poco_exists(text=page_time)
        air_api.assert_equal(now_days, True)
        d.poco_click(text="确认预约")
        air_api.assert_not_equal(d.poco_exists(text="用户已预约场地"),
                                 d.poco_exists(text='热力篮球预约成功'))
        back_home()
        d.poco_click(text="我的")
        d.poco_click(text="我的场地")
        air_api.assert_equal(d.poco_exists(text=page_time),
                             d.poco_exists(text="预约成功"))
        d.poco_click(text=page_time)
        d.poco_exists(text="热力篮球预约成功")
        d.poco_click(text="取消预约")
        d.poco_click(text="确定")
        air_api.assert_equal(d.poco_exists(text="取消预约成功"), True)

    @case_name
    def test_003(self):
        """各类活动"""
        d.poco_click(text="各类活动")
        for i in page_data['各类活动']:
            d.poco_click(text=i)
            if i == "传统文化活动":
                assert d.poco_wait_all([d.poco(text=x) for x in page_data['各类活动'][i]])
        else:
            d.assert_exists(act_img['金缘阁喜饼'])

    def test_004(self):
        """活动报名"""
        d.poco_click(text="活动报名")
        assert d.poco_wait_all([d.poco(text=x) for x in page_data['活动报名']])
        d.poco_click(text='运动活动')
        d.poco_click(text='2020慢跑曲江池')
        if d.poco_exists(text='已报名'):
            d.poco_click(text='查看报名信息')
            d.airtest_touch(act_img['关闭报名信息'])
        else:
            d.poco_click(text='立即报名')

    def test_005(self):
        """测试景点icon在地图中的显示"""
        d.poco_click(text='导览')
        d.wait(index_img['导览首页'])
        results = []
        for i in page_data['导览列表']:
            if page_data['导览列表'].index(i) == 0:
                continue
            else:
                d.poco_click_pos([0.9111111111111111, 0.1388888888888889])
                d.poco_click(text=i)
            result = d.find_all(icon_img['%sicon' % i])
            log(str(result))
            results.append(result)
        assert all(results), "icon查找有报错:%s" % results

    def test_006(self):
        """景区介绍"""
        for i in page_data['景区介绍']:
            if not d.poco_exists(text=i):
                d.poco_scroll()
            d.poco_click(text=i)
            d.poco_exists(text=page_data['景区介绍'][i])
            d.poco_click(text='商业服务')
            back()


if __name__ == '__main__':
    pytest.main(['test_qujiang_pool.py'])
