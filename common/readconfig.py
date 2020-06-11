#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

sys.path.append('.')
__author__ = '1084502012@qq.com'
__all__ = ['ini']

import os
import configparser
from config.conf import INI_PATH

APP = "APP"
package = "package"
IME = "IME"
default_ime = "default_ime"


class ReadConfig(object):
    def __init__(self):
        if not os.path.exists(INI_PATH):
            raise FileNotFoundError("配置文件{}不存在！".format(INI_PATH))
        self.config = configparser.RawConfigParser()
        self.config.read(INI_PATH, encoding='utf-8')

    def _get(self, section, option):
        return self.config.get(section, option)

    @property
    def package_name(self):
        return self._get(APP, package)

    @property
    def default_ime(self):
        return self._get(IME, default_ime)


ini = ReadConfig()

if __name__ == '__main__':
    print(ini.package_name)
