#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

sys.path.append('.')
__author__ = '1084502012@qq.com'

import pytest
from py._xmlgen import html
from basic.base import *
from basic.android_dev import android_dev
from common.readconfig import ini


@pytest.fixture(scope='session', autouse=True)
def set_session(request):
    """
    切换输入法
    """
    log("开始测试！")
    log(d.device_id)
    air_api.wake()
    air_api.start_app(ini.package_name)
    d.poco_click(text="发现")
    d.poco_click(text="小程序")
    d.poco_click(text="西安曲江池遗址公园")

    def fn():
        d.poco_click(desc="关闭")
        air_api.stop_app(ini.package_name)
        android_dev.close_yosemite_ime(ini.default_ime)  # 返回至默认的键盘
        log("结束测试！")

    request.addfinalizer(fn)


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    当测试失败的时候，自动截图，展示到html报告中
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            screen_img = _capture_screenshot()
            if file_name:
                html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:300px;height:600px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % screen_img
                extra.append(pytest_html.extras.html(html))
        report.extra = extra
        report.description = str(item.function.__doc__)
        # report.nodeid = report.nodeid.encode("utf-8").decode("unicode_escape")
        # 防止参数化乱码


@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(1, html.th('Description'))
    cells.insert(2, html.th('Test_nodeid'))
    cells.pop(2)


@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(1, html.td(report.description))
    cells.insert(2, html.td(report.nodeid))
    cells.pop(2)


def pytest_html_results_table_html(report, data):
    if report.passed:
        del data[:]
        data.append(html.div('No log output captured.', class_='empty log'))


def _capture_screenshot():
    """
    截图保存为base64
    :return:
    """
    return d.poco_shot_base64()
