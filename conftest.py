#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

sys.path.append('.')
__author__ = '1084502012@qq.com'

import time
import pytest
import allure
from py._xmlgen import html
from basic.base import *
from basic.android_dev import android_dev
from common.readconfig import ini


@allure.epic("曲江池遗址公园")
@pytest.fixture(scope='session', autouse=True)
def set_session(request):
    """
    切换输入法
    """
    allure.step("开始测试！")
    log(android_dev.device_id)
    air_api.wake()
    air_api.start_app(ini.package_name)
    d.poco_click(text="发现")
    d.poco_click(text="小程序")
    d.poco_click(text="西安曲江池遗址公园")

    def fn():
        d.poco_click(desc="关闭")
        air_api.stop_app(ini.package_name)
        android_dev.close_yosemite_ime(ini.default_ime)  # 返回至默认的键盘
        allure.step("结束测试！")

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
            screen_img = d.capture_screenshot()
            if screen_img:
                html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:300px;height:600px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % screen_img
                extra.append(pytest_html.extras.html(html))
        report.extra = extra
        report.description = str(item.function.__doc__)


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
        data.append(html.div('passed.', class_='empty log'))


def pytest_html_report_title(report):
    report.title = "曲江池遗址公园小程序UI测试！"


@pytest.mark.optionalhook
def pytest_configure(config):
    config._metadata.clear()
    config._metadata['项目名称'] = "曲江池遗址公园小程序"


@pytest.mark.optionalhook
def pytest_html_results_summary(prefix):
    prefix.extend([html.p("所属部门: 云景测试")])
    prefix.extend([html.p("测试执行人: 侯伟轩")])


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    """收集测试结果"""
    result = {
        "total": terminalreporter._numcollected,
        'passed': len(terminalreporter.stats.get('passed', [])),
        'failed': len(terminalreporter.stats.get('failed', [])),
        'error': len(terminalreporter.stats.get('error', [])),
        'skipped': len(terminalreporter.stats.get('skipped', [])),
        'total times': time.time() - terminalreporter._sessionstarttime
    }
    print(result)
