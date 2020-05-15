#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

sys.path.append('.')
__author__ = '1084502012@qq.com'

import pytest
import requests
from py._xmlgen import html
from basic.base import d
from common.readconfig import ini


@pytest.fixture(scope='session', autouse=True)
def set_session(request):
    """
    切换输入法
    """
    print("开始测试！")
    d.starts_app(ini.package_name)
    d.poco_click(text="发现")
    d.poco_click(text="小程序")
    d.poco_click(text="西安曲江池遗址公园")

    def fn():
        d.poco_click(desc="关闭")
        d.stops_app(ini.package_name)
        d.poco.ime.end()  # 返回至默认的键盘
        print("结束测试！")

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
        # 防止乱码


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


def _capture_screenshot():
    """
    截图保存为base64
    :return:
    """
    return d.poco_shot_base64()
