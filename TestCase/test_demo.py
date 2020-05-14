#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

sys.path.append('.')
__author__ = '1084502012@qq.com'

import pytest
from basic.base import d


class TestDemo:
    def test_001(self):
        """测试"""
        print(d.device_id())


if __name__ == '__main__':
    pytest.main()
