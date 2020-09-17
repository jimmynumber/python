#!/usr/bin/python
# -*- coding: UTF-8 -*-
# coding:utf-8
import sys

class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
try:
    raise MyError(2*2)
except MyError as e:
    print('My exception occurred, value:', e.value)



'''
x = 10
if x > 5:
    raise Exception('x 不能大于 5。x 的值为: {}'.format(x))   
'''

'''
while True:
    try:
        x = int(input("请输入一个数字: "))
        print("您输入的数字",x);
        #break
    except ValueError:
        print("您输入的不是数字，请再次尝试输入！")
        break
try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
'''
def this_fails():
    print(0/1)
   
try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)

try:
    print(0/1)
except AssertionError as error:
    print(error+"11111111")
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error+"222222")
finally:
    print('这句话，无论异常是否发生都会执行。')    
    

def temp_convert(var):
    try:
        return int(var)
    except (ValueError) as Argument:
        print ("参数没有包含数字\n", Argument)

# 调用函数
temp_convert("xyz");

def model_exception(x,y):
  try:
    b = name
    a =x/y
  except(ZeroDivisionError,NameError,TypeError):
    print('one of ZeroDivisionError or NameError or TypeError happend')

#调用函数结果
model_exception(2,0)

def test1():
    print('test1-1')
    print(num)
    print('test2-2')
def test2():
    print('test2-1')
    test1()
    print('test2-2')
def test3():
    try:
        print('test3-1')
        test1()
        print('test3-2')
    except Exception as result:
        print('检测出异常{}'.format(result))
    print('test3-2')
test3()
print('-------------')
test2()

with open('test_text.txt', 'r') as f:
    print(f.read())
 
    
    
    