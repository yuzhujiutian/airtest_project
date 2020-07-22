#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import yaml


class ReadYaml:
    def __init__(self, route, name):
        self.path = os.path.join(route, "{}.yaml".format(name))
        with open(self.path, encoding='utf-8') as f:
            self.data = yaml.safe_load(f)

    def __getitem__(self, item):
        return self.data[item]


if __name__ == '__main__':
    pass
