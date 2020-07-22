#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import configparser

APP = "APP"
package = "package"
IME = "IME"
default_ime = "default_ime"


class ReadConfig(object):
    def __init__(self, path):
        self.path = path
        if not os.path.exists(self.path):
            raise FileNotFoundError("配置文件{}不存在！".format(self.path))
        self.config = configparser.RawConfigParser()
        self.config.read(self.path, encoding='utf-8')

    def _get(self, section, option):
        return self.config.get(section, option)

    @property
    def package_name(self):
        return self._get(APP, package)

    @property
    def default_ime(self):
        return self._get(IME, default_ime)


if __name__ == '__main__':
    pass
