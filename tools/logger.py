#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

sys.path.append('.')
__author__ = '1084502012@qq.com'

import os
from config import conf
import logging
import datetime


def log_file():
    """日志目录"""
    file_name = "{}.log".format(datetime.datetime.now().strftime("%Y%m"))
    if not os.path.exists(conf.LOG_PATH):
        os.makedirs(conf.LOG_PATH)
    return os.path.join(conf.LOG_PATH, file_name)


def init_logging():
    # logger = logging.root
    # use 'airtest' as root logger name to prevent changing other modules' logger
    logger = logging.getLogger("airtest")
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(log_file(), encoding='utf-8')
    formatter = logging.Formatter(
        fmt='[%(asctime)s][%(levelname)s]<%(name)s> %(message)s',
        datefmt='%I:%M:%S'
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)


if __name__ == '__main__':
    print(log_file())
