#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

sys.path.append('.')
__author__ = '1084502012@qq.com'

from config import conf
from airtest.core.api import *
from tools.logger import clear_log
from tools.logger import init_logging
from airtest.aircv import crop_image
from airtest.core.helper import set_logdir, log
from airtest.core.android.android import Android
from airtest.core.android.constant import YOSEMITE_IME_SERVICE
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
# exceptions
from airtest.core.error import *
from poco.exceptions import *


class AirtestPoco(object):
    """
    Airtest和poco的方法集合
     poco-Selector
        text, textMatches
    """

    def __init__(self):
        """
        init初始化
        """
        # 删除旧日志
        clear_log()
        # 设置全局日志目录
        set_logdir(conf.TEST_LOG)
        log("设置全局日志目录：%s" % conf.TEST_LOG)
        # # 初始化日志
        init_logging()
        self.android = Android()
        self.poco = AndroidUiautomationPoco(force_restart=False)
        self.timeout = ST.FIND_TIMEOUT  # 等待显示时间

    """
    AirTest-Method
    封装的都是跟图片相关的
    """

    @classmethod
    def template(cls, img_name: str, rgb: bool = True, record_pos: tuple = (0.5, -0.5)):
        """CV识别主函数
        :param rgb: 灰度识别还是色彩识别
        :param record_pos: 图片坐标
        :param img_name: 图片名称
        :return:
        """
        temp = Template(r"%s" % img_name, rgb=rgb, record_pos=record_pos, resolution=d.screen)
        return temp

    def airtest_touch(self, v: str, *args, **kwargs):
        """触摸函数"""
        touch(self.template(v), *args, **kwargs)

    def airtest_double_click(self, v):
        """双击"""
        double_click(self.template(v))

    def airtest_swipe(self, v1, v2=None, vector=None, **kwargs):
        """
        在设备屏幕上执行滑动操作。
        分配参数有两种方法
            swipe(v1, v2=Template(...)) ＃从v1滑动到v2
            swipe(v1, vector=(x, y)) ＃滑动从v1开始并沿向量移动。
        参数：
            v1 –滑动的起点，可以是Template实例，也可以是绝对坐标（x，y）
            v2 –滑动的终点，可以是Template实例，也可以是绝对坐标（x，y）
            向量 –滑动动作的向量坐标，可以是绝对坐标（x，y）或屏幕百分比，例如（0.5，0.5）
            **矮人 –
            平台特定的kwargs，请参考相应的文档
        引发：	异常 –如果提供的参数不足以执行交换操作，则为一般异常
        平台：	Android，Windows，iOS
        :return: 原点位置和目标位置
        """
        if v1.endswith('.png'):
            v1 = self.template(v1)
        if v2.endswith('.png'):
            v2 = self.template(v2)
        return swipe(v1, v2, vector, **kwargs)

    def airtest_wait(self, v, *args, **kwargs):
        """等待函数"""
        wait(self.template(v), *args, **kwargs)

    def airtest_exists(self, v):
        """判断函数"""
        return exists(self.template(v))

    def assert_exists(self, v, msg: str = None):
        """断言函数"""
        assert_exists(self.template(v), msg)

    def assert_not_exists(self, v, msg: str = None):
        """断言函数"""
        assert_not_exists(self.template(v), msg)

    def find_all(self, v):
        """
        在设备屏幕上查找目标的所有位置并返回其坐标
        :param v:要查找的目标
        :return:坐标列表，[（x，y），（x1，y1），…]
        :平台：Android、Windows、iOS
        """
        return find_all(self.template(v))

    """
    poco-method
    """

    def wait_any(self, *args, **kwargs):
        """
        等待，直到所有给定的 UI 代理在超时之前显示。将定期轮询所有 UI 代理。
        :param args:
        :param kwargs:
        :return:
        """
        return self.poco.wait_for_any(*args, **kwargs)

    def wait_all(self, *args, **kwargs):
        """
        等待，直到所有给定的 UI 代理在超时之前显示。将定期轮询所有 UI 代理。
        :param args:
        :param kwargs:
        :return:
        """
        return self.poco.wait_for_all(*args, **kwargs)

    def poco_obj(self, *args, **kwargs):
        """poco实例"""
        if 'index' in kwargs:
            index = kwargs.pop('index')
            ele = self.poco(*args, **kwargs)[index]
            ele.wait_for_appearance(timeout=self.timeout)
            return ele
        ele = self.poco(*args, **kwargs)
        ele.wait_for_appearance(timeout=self.timeout)
        return ele

    def poco_click(self, *args, **kwargs):
        """
        对由UI代理表示的UI元素执行click操作。如果这个UI代理代表一组
        UI元素，单击集合中的第一个元素，并将UI元素的定位点用作默认值
        一个。还可以通过提供“focus”参数单击另一个点偏移。
        :param args:
        :param kwargs: [text, name]
        """
        log("点击元素：{}".format(kwargs))
        self.poco_obj(*args, **kwargs).click()

    def poco_get_text(self, *args, **kwargs):
        """
        获取 UI 元素的文本属性。如果没有此类属性，则返回"无"。
        :param args:
        :param kwargs:
        :return:
        """
        txt = self.poco_obj(*args, **kwargs).get_text()
        log("获取元素{}文本：{}".format(kwargs, txt))
        return txt

    def poco_attr(self, name, *args, **kwargs):
        """
        按给定属性名称检索 UI 元素的属性。如果属性不存在，则返回"无"。
        visible：用户是否可见
        text：UI 元素的字符串值
        type：远程运行时的 UI 元素的类型名称
        pos：UI 元素的位置
        size：根据屏幕，0+1 范围内的百分比大小 [宽度、高度]
        name：UI 元素的名称
        ...： other sdk 实现的属性
        :return:
        """
        self.poco_obj(*args, **kwargs).attr(name)

    def poco_exists(self, *args, **kwargs):
        """
        测试UI元素是否在层次结构中
        :param args:
        :param kwargs: [text,name]
        """
        result = self.poco(*args, **kwargs).exists()
        log("元素{}验证结果: {}".format(kwargs, result))
        return result

    def poco_scroll(self, *args, **kwargs):
        """
        从整个屏幕的下部滚动到上部
        方向：滚动方向。垂直或“水平”
        百分比：根据
        持续时间：执行操作的时间间隔
        :param args:
        :param kwargs: direction="vertical" or "horizontal", percent=0.6, duration=2.0
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

    def crop_image(self, rect):
        """局部截图
        :param rect = [x_min, y_min, x_max ,y_max].
        """
        img = G.DEVICE.snapshot()
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

    def yosemite_ime_end(self, ime):
        """关闭airtest输入法"""
        self.android.adb.shell("ime disable %s" % YOSEMITE_IME_SERVICE)
        self.android.adb.shell("ime set %s" % ime)


d = AirtestPoco()
if __name__ == '__main__':
    print(d.get_top_activity)
    print(d.screen)
