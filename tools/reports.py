#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

sys.path.append('.')
__author__ = '1084502012@qq.com'
__all__ = ['get_report']

import os
from config import conf
from tools.times import strftime
from airtest.utils.compat import script_dir_name
from airtest.report.report import LogToHtml, HTML_TPL


def report_path():
    """报告目录"""
    report_paths = os.path.join(conf.REPORT_PATH, "%s" % strftime())
    if not os.path.exists(report_paths):
        os.makedirs(report_paths)
    return report_paths


def get_report(script, outfile, log_root, static_root="", lang="zh", record_list=None):
    """生成airtest_report"""
    path, name = script_dir_name(script)
    rpt = LogToHtml(path, log_root, static_root=static_root, export_dir=report_path(), script_name=name, lang=lang,
                    plugins=["poco.utils.airtest.report"])
    rpt.report(HTML_TPL, output_file=outfile, record_list=record_list)


if __name__ == '__main__':
    for i in ["poco.utils.airtest.report"]:
        print(i)
