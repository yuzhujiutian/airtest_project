#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

sys.path.append('.')
__author__ = '1084502012@qq.com'

import allure
import pytest
from pytest import assume
from basic.base import *
from common.readimg import *
from pages.homepage import back
from common.readyaml import page_data


@allure.feature("导览地图ICON")
class TestMap:
    """导览地图"""

    @allure.title("测试景点icon在地图中的显示")
    def test_001(self):
        """测试景点icon在地图中的显示"""
        d.poco_click(text='导览')
        d.wait(d.temp(index_img['导览首页'], record_pos=(0.398, 0.261)))
        results = []
        for i in page_data['导览列表']:
            if page_data['导览列表'].index(i) == 0:
                continue
            else:
                d.poco_click_pos([0.9111111111111111, 0.1388888888888889])
                d.poco_click(text=i)
            result = d.find_all(d.temp(icon_img['%sicon' % i]))
            log(str(result))
            results.append(result)
        with assume:
            assert all(results), "icon查找有报错:%s" % results

    def test_002(self):
        """测试景点列表的滑动"""
        pass


if __name__ == '__main__':
    pytest.main(['test_map.py'])
