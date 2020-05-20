#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

sys.path.append('.')
__author__ = '1084502012@qq.com'

from config import conf
from airtest.aircv import *
from airtest.core.api import *
from airtest.core.helper import *
from tools.logger import clear_log
from tools.logger import init_logging
from airtest.core.android.android import Android
from airtest.core.android.constant import YOSEMITE_IME_SERVICE
from poco.drivers.android.uiautomation import AndroidUiautomationPoco


class AirPoco(object):
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
        set_logdir(conf.TEST_CASE_LOG)
        # # 初始化日志
        init_logging()
        self.android = Android()
        self.poco = AndroidUiautomationPoco(force_restart=False)

    """
    AirTest-Method
    """

    @staticmethod
    def template(img_name: str, rgb: bool = True, record_pos: tuple = (0.5, -0.5)):
        """CV识别主函数
        :param rgb: 灰度识别还是色彩识别
        :param record_pos: 图片坐标
        :param img_name: 图片名称
        :return:
        """
        temp = Template(r"%s" % img_name, rgb=rgb, record_pos=record_pos, resolution=d.screen)
        return temp

    def airtest_touch(self, *args):
        """触摸函数"""
        touch(AirPoco.template(*args))

    def airtest_text(self, content):
        """输入函数"""
        text(content)

    def airtest_wait(self, *args):
        """等待函数"""
        wait(AirPoco.template(*args))

    def airtest_exist(self, *args):
        """判断函数"""
        return exists(AirPoco.template(*args))

    def assert_exists(self, *args, msg: str = None):
        """断言函数"""
        assert_exists(AirPoco.template(*args), msg)

    def starts_app(self, *args, **kwargs):
        """
        在设备上启动目标应用程序
            :param package: 要启动的包的名称，例如"com.netease.my"
            :param activity:开始的活动，默认为无，表示主要活动
        """
        start_app(*args, **kwargs)

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

    def poco_click(self, *args, **kwargs):
        """
        对由UI代理表示的UI元素执行click操作。如果这个UI代理代表一组
        UI元素，单击集合中的第一个元素，并将UI元素的定位点用作默认值
        一个。还可以通过提供“focus”参数单击另一个点偏移。
        :param args:
        :param kwargs: [text,name]
        """
        ele = self.poco(*args, **kwargs)
        ele.wait_for_appearance()  # 阻止并等待
        ele.click()

    def poco_get_text(self, *args, **kwargs):
        """
        获取 UI 元素的文本属性。如果没有此类属性，则返回"无"。
        :param args:
        :param kwargs:
        :return:
        """
        return self.poco(*args, **kwargs).get_text()

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
        self.poco(*args, **kwargs).attr(name)

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

    def yosemite_ime_end(self):
        """关闭airtest输入法"""
        self.android.adb.shell("ime disable %s" % YOSEMITE_IME_SERVICE)
        # self.android.adb.shell("ime set %s" % )


d = AirPoco()
if __name__ == '__main__':
    print(d.device_id)
    print(d.screen)
