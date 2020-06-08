#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

sys.path.append('.')
__author__ = '1084502012@qq.com'

import os
import yaml
from config import conf


class ReadYaml:
    def __init__(self, name):
        self.path = os.path.join(conf.YAML_PATH, "{}.yaml".format(name))
        with open(self.path, encoding='utf-8') as f:
            self.data = yaml.safe_load(f)

    def __getitem__(self, item):
        return self.data[item]


page_data = ReadYaml('page_data')

__all__ = ['page_data']

if __name__ == '__main__':
    from pprint import pprint

    pprint(page_data['景区介绍']['青年公园景观区'])
