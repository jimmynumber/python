#!/usr/bin/python
# -*- coding: UTF-8 -*-
# coding:utf-8 
from MyError import MyError


try:
    raise MyError(2*2)
except MyError as e:
    print('My exception occurred, value:', e.value)
