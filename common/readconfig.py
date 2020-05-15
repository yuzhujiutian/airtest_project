#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

sys.path.append('.')
__author__ = '1084502012@qq.com'
__all__ = ['ini']

import os
import configparser
import config.conf as cfg

APP = "APP"
package = "package"


class ReadConfig(object):
    def __init__(self):
        self.path = cfg.INI_PATH
        if not os.path.exists(self.path):
            raise FileNotFoundError("配置文件{}不存在！".format(self.path))
        self.config = configparser.RawConfigParser()
        self.config.read(self.path, encoding='utf-8')

    def _get(self, section, option):
        return self.config.get(section, option)

    @property
    def package_name(self):
        return self._get(APP, package)


ini = ReadConfig()

if __name__ == '__main__':
    print(ini.package_name)
