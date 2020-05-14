#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

sys.path.append('.')
__author__ = '1084502012@qq.com'
__all__ = ['d']

import conf
from airtest.aircv import *
from airtest.core.api import *
from airtest.core.helper import *
from tools.logger import init_logging
from airtest.core.settings import Settings as ST
from airtest.core.android.android import Android
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
# exception
from poco.exceptions import *
from airtest.core.error import *


class AirPage(object):
    """
    Airtest和poco的方法集合
    """

    def __init__(self):
        """
        init初始化
        """
        # 设置全局日志目录
        set_logdir(conf.LOG_PATH)
        # 初始化日志
        init_logging()
        self.android = Android()
        self.poco = AndroidUiautomationPoco(force_restart=False)

    """
    AirTest-Method
    """

    @staticmethod
    def template(img_name):
        """CV识别主函数
        :param img_name: 图片名称
        :return:
        """
        temp = Template(repr(img_name), record_pos=(0.5, -0.5), resolution=screen())
        return temp

    def airtest_touch(self, name):
        """触摸函数"""
        touch(AirPage.template(name))

    def airtest_text(self, name):
        """输入函数"""
        text(name)

    def airtest_wait(self, name):
        """等待函数"""
        wait(AirPage.template(name))

    def airtest_exist(self, name):
        """判断函数"""
        return exists(AirPage.template(name))

    def starts_app(self, *args, **kwargs):
        """
        在设备上启动目标应用程序
            :param package: 要启动的包的名称，例如"com.netease.my"
            :param activity:开始的活动，默认为无，表示主要活动
        """
        start_app(self, *args, **kwargs)

    def stops_app(self, *args, **kwargs):
        """
        停止设备上的目标应用程序
            :param package 要停止的包的名称，另请参见start_app
        :return:
        """
        stop_app(*args, **kwargs)

    """
    poco-method
    """

    def wait_any(self):
        self.poco.wait_for_any()

    def poco_click(self, *args, **kwargs):
        """
        对由UI代理表示的UI元素执行click操作。如果这个UI代理代表一组
        UI元素，单击集合中的第一个元素，并将UI元素的定位点用作默认值
        一个。还可以通过提供“focus”参数单击另一个点偏移。
        :param args:
        :param kwargs: [text,name]
        """
        self.poco(*args, **kwargs).click()

    def poco_exists(self, *args, **kwargs):
        """
        测试UI元素是否在层次结构中
        :param args:
        :param kwargs: [text,name]
        """
        return self.poco(*args, **kwargs).exists()

    def poco_scroll(self, *args, **kwargs):
        """
        从整个屏幕的下部滚动到上部
        方向：滚动方向。垂直或“水平”
        百分比：根据
        持续时间：执行操作的时间间隔
        :param args:
        :param kwargs: direction='vertical', percent=0.6, duration=2.0
        """
        self.poco.scroll(*args, **kwargs)

    def poco_shot_base64(self, width=720):
        """
        获取屏幕截图
        :param width:
        :return:
                2-tuple:
                    - screen_shot (:obj:`str/bytes`): base64 encoded screenshot data
                    - format (:obj:`str`): output format 'png', 'jpg', etc.
        """
        base64, _ = self.poco.snapshot(width=width)
        return base64

    """
    aircv-method
    """

    def crop_image(self, img, rect):
        """局部截图
        :param img:
        :param rect:
        """
        crop_screen = crop_image(img, rect)  # 局部截图
        try_log_screen(crop_screen)  # 保存局部截图到logs文件夹中

    """
    设备相关
    """

    @property
    def device_id(self):
        """当前设备ID"""
        return self.android.uuid

    @property
    def screen(self):
        """获取屏幕宽高"""
        info = self.android.display_info
        return info.get('width'), info.get('height')

    @property
    def get_top_activity(self):
        """获取顶级活动"""
        return self.android.get_top_activity()


d = AirPage()
if __name__ == '__main__':
    pass
