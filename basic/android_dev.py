#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

sys.path.append('.')
__author__ = '1084502012@qq.com'

from airtest.core.android.android import Android
from airtest.core.android.constant import YOSEMITE_IME_SERVICE


class AndroidDev:
    """
    安卓相关获取的命令
    """

    def __init__(self):
        self.android = Android()
        self.adb = self.android.adb

    @property
    def screen(self):
        """获取屏幕宽高"""
        info = self.android.display_info
        return info.get('width'), info.get('height')

    @property
    def device_id(self):
        """当前设备ID"""
        return self.android.uuid

    @property
    def get_top_activity(self):
        """获取顶级活动"""
        return self.android.get_top_activity()

    @property
    def get_default_ime(self):
        """获取默认的输入法"""
        return self.adb.shell("settings get secure default_input_method").strip()

    @property
    def get_ipv4(self):
        """[summary]
        获取手机的IP地址
        """
        return self.android.get_ip_address()

    def close_yosemite_ime(self, ime):
        """关闭airtest输入法"""
        self.adb.shell("ime disable %s" % YOSEMITE_IME_SERVICE)
        self.adb.shell("ime set %s" % ime)


android_dev = AndroidDev()
__all__ = ['android_dev']

if __name__ == '__main__':
    print(android_dev.close_yosemite_ime("com.sohu.inputmethod.sogou/.SogouIME"))
