#!/usr/bin/python
# -*- coding: UTF-8 -*-
#coding:utf-8
import math


'''
模块
        import 语句
                import module1[, module2[,... moduleN]
        From…import 语句
                from modname import name1[, name2[, ... nameN]]
        From…import  *    语句
                from modname import *
        # global Money
        dir()函数
                dir() 函数一个排好序的字符串列表，内容是一个模块里定义过的名字。
        globals() 和 locals() 函数
                                    根据调用地方的不同，globals() 和 locals() 函数可被用来返回全局和局部命名空间里的名字。
                                    如果在函数内部调用 locals()，返回的是所有能在该函数里访问的命名。
                                    如果在函数内部调用 globals()，返回的是所有在该函数里能访问的全局名字。
                                    两个函数的返回类型都是字典。所以名字们能用 keys() 函数摘取。
        reload() 函数
                                    当一个模块被导入到一个脚本，模块顶层部分的代码只会被执行一次。
                                    想重新执行模块里顶层部分的代码，可以用 reload() 函数
               reload(module_name)
'''

content = dir(math);
print(content);
'''
以上实例输出结果：
['__doc__', '__file__', '__name__', 'acos', 'asin', 'atan', 
'atan2', 'ceil', 'cos', 'cosh', 'degrees', 'e', 'exp', 
'fabs', 'floor', 'fmod', 'frexp', 'hypot', 'ldexp', 'log',
'log10', 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 
'sqrt', 'tan', 'tanh']
在这里，特殊字符串变量__name__指向模块的名字，__file__指向该模块的导入文件名。
'''
