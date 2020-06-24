#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

sys.path.append('.')
__author__ = '1084502012@qq.com'
__all__ = ['d', 'log', 'airtest_api', 'air_error', 'poco_error']

import os
import allure
import base64
from config.conf import TEST_LOG
from tools.logger import clear_log
from tools.logger import init_logging

from airtest.core.cv import Template
from airtest.core import api as airtest_api
from airtest.core.settings import Settings as ST
from airtest.core.helper import G, set_logdir, log

from airtest.aircv import crop_image
from basic.android_dev import android_dev

from poco.proxy import UIObjectProxy
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
# exceptions
from airtest.core import error as air_error
from poco import exceptions as poco_error


class AirtestPoco(object):
    """
    Airtest和Poco的方法集合
    airtest-api
        airtest_api,methods
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
        set_logdir(TEST_LOG)
        log("设置全局日志目录：%s" % TEST_LOG)
        # # 初始化日志
        init_logging()
        self.poco = AndroidUiautomationPoco(
            use_airtest_input=True, screenshot_each_action=False)
        self.UIObj = UIObjectProxy(poco=self.poco)
        self.timeout = airtest_api.ST.FIND_TIMEOUT  # 等待显示时间

    """
    AirTest-Method
    封装的都是跟图片相关的
    """

    @classmethod
    def temp(cls, img_name: str, rgb: bool = True, record_pos: tuple = (0.5, -0.5)):
        """CV识别主函数
        :param rgb: 灰度识别还是色彩识别
        :param record_pos: 图片坐标
        :param img_name: 图片名称
        :return:
        """
        temp = airtest_api.Template(
            r"%s" % img_name, rgb=rgb, record_pos=record_pos, resolution=android_dev.screen)
        return temp

    def touch(self, v: Template, **kwargs):
        """
        在设备屏幕上执行触摸操作
        :param v: 要触摸的目标，可以是Template实例，也可以是绝对坐标（x，y）
        :param kwargs: [times  要执行多少次触摸]
        """
        airtest_api.touch(v, **kwargs)

    def text(self, text, enter=True, **kwargs):
        """
        目标设备上的输入文本。文本输入部件必须首先是活动的。
        :param text: 输入文本，支持unicode
        :param enter:输入' enter '键事件后文本输入，默认为真
        :param kwargs:
        :return:
        :platforms: Android, Windows, iOS
        """
        airtest_api.text(text, enter=enter, **kwargs)
        sleep()

    def double_click(self, v: Template):
        """双击"""
        airtest_api.double_click(v)

    def swipe(self, v1, v2=None, vector=None, **kwargs):
        """
        在设备屏幕上执行滑动操作。
        分配参数有两种方法
            swipe(v1, v2=Template(...)) ＃从v1滑动到v2
            swipe(v1, vector=(x, y)) ＃滑动从v1开始并沿向量移动。
        :param：v1 –滑动的起点，可以是Template实例，也可以是绝对坐标（x，y）
        :param：v2 –滑动的终点，可以是Template实例，也可以是绝对坐标（x，y）
        :param：vector - 向量 –滑动动作的向量坐标，可以是绝对坐标（x，y）或屏幕百分比，例如（0.5，0.5）
        :param：**kwargs – 平台特定的kwargs，请参考相应的文档
        :exception: 异常 –如果提供的参数不足以执行交换操作，则为一般异常
        平台：	Android，Windows，iOS
        :return: 原点位置和目标位置
        """
        if v1.endswith('.png'):
            v1 = self.temp(v1)
        if v2.endswith('.png'):
            v2 = self.temp(v2)
        return airtest_api.swipe(v1, v2, vector, **kwargs)

    def wait(self, v: Template, **kwargs):
        """
        等待与设备屏幕上的模板匹配
        :param v –等待的目标对象，模板实例
        :param 超时 –等待比赛的时间间隔，默认为无，即ST.FIND_TIMEOUT
        :param interval –尝试找到匹配项的时间间隔（以秒为单位）
        :param intervalfunc –在每次未成功尝试找到相应匹配项后调用
        """
        airtest_api.wait(v, **kwargs)

    def exists(self, v: Template):
        """
        检查设备屏幕上是否存在给定目标
        :param v –检查对象
        :return 如果找不到目标，则为False，否则返回目标的坐标
        """
        return airtest_api.exists(v)

    def assert_exists(self, v: Template, msg: str = None):
        """
        断言目标存在于设备屏幕上
        :param v –要检查的目标
        :param msg –断言的简短描述，它将记录在报告中
        """
        airtest_api.assert_exists(v, msg)

    def assert_not_exists(self, v: Template, msg: str = None):
        """
        断言目标在设备屏幕上不存在
        :param v –要检查的目标
        :param msg –断言的简短描述，它将记录在报告中
        """
        airtest_api.assert_not_exists(v, msg)

    def find_all(self, v: Template):
        """
        在设备屏幕上查找目标的所有位置并返回其坐标
        :param v:要查找的目标
        :return:坐标列表，[（x，y），（x1，y1），…]
        :平台：Android、Windows、iOS
        """
        return airtest_api.find_all(v)

    def capture_screenshot(self, bs64=True):
        """
        截图保存为base64
        :return:
        """
        filename = airtest_api.try_log_screen()['screen']
        filepath = os.path.join(TEST_LOG, filename)
        allure.attach.file(filepath, "异常截图..." + filename,
                           allure.attachment_type.JPG)
        if bs64:
            with open(filepath, 'rb') as f:
                imagebase64 = base64.b64encode(f.read())
            return imagebase64.decode()

    """
    poco-method
    """

    def poco_wait_any(self, objects):
        """
        等待，直到所有给定的一个 UI 代理在超时之前显示。将定期轮询所有 UI 代理。
        :param objects:
        :return: bool
        """
        try:
            return self.poco.wait_for_any(objects, timeout=self.timeout)
        except poco_error.PocoTargetTimeout:
            return False

    def poco_wait_all(self, objects):
        """
        等待，直到所有给定的所有 UI 代理在超时之前显示。将定期轮询所有 UI 代理。
        :param objects:
        :return:
        """
        try:
            self.poco.wait_for_all(objects, timeout=self.timeout)
            return True
        except poco_error.PocoTargetTimeout:
            return False

    def poco_obj(self, **kwargs):
        """poco实例"""
        if 'index' in kwargs:
            index = kwargs.pop('index')
            ele = self.poco(**kwargs)[index]
        else:
            ele = self.poco(**kwargs)
        ele.wait_for_appearance(timeout=self.timeout)
        return ele

    def poco_click(self, **kwargs):
        """
        对由UI代理表示的UI元素执行click操作。如果这个UI代理代表一组
        UI元素，单击集合中的第一个元素，并将UI元素的定位点用作默认值
        一个。还可以通过提供“focus”参数单击另一个点偏移。
        :param kwargs: [text, name]
        """
        log("点击元素：{}".format(kwargs))
        self.poco_obj(**kwargs).click()

    def poco_click_pos(self, pos):
        """
        在给定坐标下对目标设备执行单击(触摸，轻击等)操作。坐标(x, y)是一个2-列表或2-元组。
        x和y的坐标值必须在0 ~ 1之间，以表示屏幕的百分比。
        例如：
            坐标[0.5,0.5]表示屏幕的中心，坐标[0,0]表示左上角。
            有关坐标系统的详细信息，请参阅CoordinateSystem。
        实际案例：
            单击分辨率为（1920，1080）的屏幕的（100，100）点：
                poco.click([100.0 / 1920, 100.0 / 1080])
        :param pos: (list(float, float) / tuple(float, float)) – coordinates (x, y) in range of 0 to 1
        :return:
        """
        self.poco.click(pos)

    def poco_text(self, **kwargs):
        """
        获取 UI 元素的文本属性。如果没有此类属性，则返回"无"。
        :param kwargs:
        :return: txt
        """
        txt = self.poco_obj(**kwargs).get_text()
        log("获取元素{}文本：{}".format(kwargs, txt))
        return txt

    def poco_attr(self, name, **kwargs):
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
        self.poco_obj(**kwargs).attr(name)

    def poco_freeze(self, **kwargs):
        """冻结UI树并返回当前的UI结果树"""
        with self.poco.freeze() as freeze:
            return freeze(**kwargs)

    def poco_hierarchy_dict(self):
        """获取当前结构树的字典"""
        frozen_poco = self.poco.freeze()
        hierarchy_dict = frozen_poco.agent.hierarchy.dump()
        return hierarchy_dict

    def poco_exists(self, **kwargs):
        """
        测试UI元素是否在层次结构中
        :param kwargs: [text,name]
        """
        result = self.poco_freeze(**kwargs).exists()
        log("元素{}验证结果: {}".format(kwargs, result))
        return result

    def poco_scroll(self, direction='vertical', percent=0.5, duration=2.0):
        """
        从整个屏幕的下部滚动到上部
        默认的 direction='vertical', percent=0.6, duration=2.0
        :param direction: 方向：滚动方向。垂直(vertical)或“水平”(horizontal)
        :param duration: 百分比：根据
        :param percent: 持续时间：执行操作的时间间隔
        """
        self.poco.scroll(direction=direction,
                         percent=percent, duration=duration)

    def poco_swipe(self, p1, p2=None, direction=None, duration: float = 2.0):
        """
        在目标设备上通过起点和终点或方向向量指定的点到点执行滑动操作。必须至少提供端点或方向之一。
        点的坐标（x，y）定义与click事件的定义相同。方向矢量（x，y）的分量也以0到1的屏幕范围表示。
        请参阅CoordinateSystem以获取有关坐标系的更多详细信息。
        实际案例
            以下示例显示了如何在分辨率为1920x1080的屏幕上执行从（100，100）到（100，200）的滑动动作：
                poco.swipe([100.0 / 1920, 100.0 / 1080], [100.0 / 1920, 200.0 / 1080])
            或由特定方向而非终点给定：
                poco.swipe([100.0 / 1920, 100.0 / 1080], direction=[0, 100.0 / 1080])
        :param p1: 起点
        :param p2: 终点
        :param direction: 滑动方向
        :param duration: 持续时间（float）–执行滑动操作的时间间隔
        """
        self.poco.swipe(p1=p1, p2=p2, direction=direction, duration=duration)

    """
    aircv-method
    """

    @classmethod
    def crop_image(cls, rect):
        """局部截图
        :param rect = [x_min, y_min, x_max ,y_max].
        """
        img = airtest_api.G.DEVICE.snapshot()
        crop_screen = crop_image(img, rect)  # 局部截图
        airtest_api.try_log_screen(crop_screen)  # 保存局部截图到logs文件夹中


d = AirtestPoco()

if __name__ == '__main__':
    print(d)
