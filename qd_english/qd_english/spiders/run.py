#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@author: jmz
@file: run.py.py
@time: 2020/9/23 15:48
@desc:
"""

from scrapy import cmdline

cmdline.execute("scrapy crawl english".split())