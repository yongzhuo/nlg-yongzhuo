# -*- coding: UTF-8 -*-
# !/usr/bin/python
# @time     :2019/7/28 0:24
# @author   :Mo
# @function : base path of nlg-yongzhuo


import sys
import os


# base dir
path_root = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
projectdir = path_root.replace('\\', '/')
sys.path.append(projectdir)
print(projectdir)


