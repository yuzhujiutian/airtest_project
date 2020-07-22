#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import shutil
import logging
import datetime
from config import LOG_PATH


def log_file():
    """日志目录"""
    file_name = "{}.log".format(datetime.datetime.now().strftime("%Y%m"))
    if not os.path.exists(LOG_PATH):
        os.makedirs(LOG_PATH)
    return os.path.join(LOG_PATH, file_name)


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


def clear_log(path):
    """清除上一次的日志记录"""
    try:
        shutil.rmtree(path)
        print("删除：{}".format(path))
    except FileNotFoundError:
        pass


if __name__ == '__main__':
    clear_log('123')
