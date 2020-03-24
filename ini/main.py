# -*- coding: utf-8 -*-
"""
# Author: lixiang
# Created Time : Sun 22 Mar 2020 08:53:23 PM CST
# File Name: main.py
# Description:
"""
from bq import *

#%% Test Codes
if __name__=='__main__':
    ini = Ini('./test.ini')
    print(ini)
    print(ini.keys)
    print(ini.exists('sec~ui'))
    print(ini.findBool('sec~hh'))
    print(ini.findBoolVec('first~vb'))
    print(ini.findInt('today'))
    print(ini.findFloat('a'))
    print(ini.findFloatVec('b'))
    ini.set('from~outside',[1,2.1])
    print(ini.findFloatVec('from~outside'))
