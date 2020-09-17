#!/usr/bin/python
# -*- coding: UTF-8 -*-
#coding:utf-8

fo = open("D:\\文件\\temp\\myfile.txt",'r',encoding='utf-8')
print("文件名： ", fo.name)

fd = fo.fileno()
print("文件描述符为： ", fd)

isa = fo.isatty()
print("检测文件是否连接到一个终端设备，如果是返回 True，否则返回 False： ", isa)


line = fo.readline()
print("读取第一行:  %s" % (line))

line = fo.readline(3)
print("读取字符串为： %s" % (line))

'''
for index in range(1,4):
    line = next(fo)
    print("第 %d 行 ： %s"  % (index, line))
'''    
    
line = fo.read(2)
print("读取的字符串： %s" % (line))

line = fo.readlines()
print("读取的数据为:  %s" % (line))

#重新设置文件读取指针到开头
fo.seek(0, 0)
line = fo.readline()
print("读取的数据为： %s" % (line))

#从当前位置指针开始
fo.seek(0, 1)
line = fo.readline()
print("读取的数据为： %s" % (line))

#从文件末尾开始
fo.seek(0, 2)
line = fo.readline()
print("读取的数据为： %s" % (line))

#获取当前文件指针位置
path = fo.tell()
print("当前指针位置： %d" % (path))

# truncate()方法用于截断文件，如果指定了可选参数size，
# 则表示截断文件为size个字符。如果没有指定size，则重置到当前位置。（换行符’\n‘也会被计算）
#fo.truncate(10)


#刷新缓冲区
fo.flush()

#关闭文件
fo.close()

print('------------------------------------------------------')
fo = open("D:\\文件\\temp\\myfile.txt",'r+',encoding='utf-8')

fo.seek(0, 2)
line = fo.write('\n123456789')

#回到文件开头，读取文件所有内容
fo.seek(0, 0)
for index in range(1,6):
    line = next(fo)
    print('第 %d 行 -- %s' % (index, line))

#在文件末尾写入
fo.seek(0, 2)
seq = ['\n添加第五行内容', '\n添加第六行内容']
line = fo.writelines(seq)

#回到文件开头，读取文件所有内容
fo.seek(0, 0)
line = fo.read()
print(line)

#关闭文件
fo.close()
