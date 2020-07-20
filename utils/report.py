#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
from core.aircore import ST
from utils.times import strftime
from config.conf import BASE_DIR, REPORT_PATH
from airtest.utils.compat import script_dir_name
from airtest.report.report import LogToHtml, HTML_TPL

__all__ = ['get_report']


def report_path():
    """报告目录"""
    report_paths = os.path.join(REPORT_PATH, "%s" % strftime())
    if not os.path.exists(report_paths):
        os.makedirs(report_paths)
    return report_paths


def get_report(script, log_root=ST.LOG_DIR, outfile='log.html', static_root="", lang="zh", record_list=None):
    """生成airtest_report"""
    path, name = script_dir_name(script)
    rpt = LogToHtml(path, log_root, static_root=static_root, export_dir=report_path(), script_name=name, lang=lang,
                    plugins=["poco.utils.airtest.report"])
    rpt.report(HTML_TPL, output_file=outfile, record_list=record_list)


script_file = os.path.join(BASE_DIR, 'TestCase', 'conftest.py')

if __name__ == '__main__':
    get_report(script_file)
