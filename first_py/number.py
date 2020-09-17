#!/usr/bin/python
# -*- coding UTF-8 -*-
import math
import operator
import random


print(abs(-45) ,abs(100.12))
print(math.ceil(-45.17), math.ceil(100.12), math.ceil(100.72), math.ceil(119), math.ceil(math.pi))
print(math.floor(-45.17), math.floor(100.12), math.floor(100.72), math.floor(119), math.floor(math.pi))
print(operator.le(80, 100), operator.gt(180, 100), operator.eq(-80, 100), operator.ne(80, -100))
print ("math.fabs(-45.17) : ", math.fabs(-45.17))
print ("math.fabs(100.12) : ", math.fabs(100.12))
print ("math.fabs(100.72) : ", math.fabs(100.72))
print ("math.fabs(119) : ", math.fabs(119))
print ("math.fabs(math.pi) : ", math.fabs(math.pi))

print(min(1,2,3,4,5,6),max(1,2,3,4,5,6))

print ("math.modf(100.12) : ", math.modf(100.12))
print ("math.modf(100.72) : ", math.modf(100.72))
print ("math.modf(119) : ", math.modf(119))
print ("math.modf(math.pi) : ", math.modf(math.pi))

print ("pow(100, 2) : ", pow(100, 2))
print ("math.pow(100, -2) : ", math.pow(100, -2))
print ("math.pow(2, 4) : ", math.pow(2, 4))
print ("math.pow(3, 0) : ", math.pow(3, 0))

print ("round(100, 2) : ", round(100.123, 2))
print ("round(100, -2) : ", round(100.537, -2))
print ("round(2, 4) : ", round(2.56, 1))
print ("round(3, 0) : ", round(3.35, 1))

# sqrt(x) 返回数字x的平方根
print("math.sqrt(100) : ", math.sqrt(100))
print("math.sqrt(7) : ", math.sqrt(7))
print("math.sqrt(math.pi) : ", math.sqrt(math.pi))

# choice(seq)   从序列的元素中随机挑选一个元素，
# 比如random.choice(range(10))，从0到9中随机挑选一个整数。
print("choice([1, 2, 3, 5, 9]) : ", random.choice([1, 2, 3, 5, 9]))
print("choice('A String') : ", random.choice('A String'))

# randrange ([start,] stop [,step])    从指定范围内，按指定基数递增的集合中获取一个随机数，基数缺省值为1
# 输出 100 <= number < 1000 间的偶数
print("randrange(100, 1000, 2) : ", random.randrange(100, 1000, 2))
# 输出 100 <= number < 1000 间的其他数
print("randrange(100, 1000, 3) : ", random.randrange(100, 1000, 3))

# random()  随机生成下一个实数，它在[0,1)范围内。
# 生成第一个随机数
print ("random() : ", random.random())
# 生成第二个随机数
print ("random() : ", random.random())

random.seed( 10 )
print ("Random number with seed 10 : ", random.random())
# 生成同一个随机数
random.seed( 10 )
print ("Random number with seed 10 : ", random.random())
# 生成同一个随机数
random.seed(0)
print ("Random number with seed 10 : ", random.random())

# shuffle(lst)  将序列的所有元素随机排序
list1 = [20, 16, 10, 5];
random.shuffle(list1)
print ("随机排序列表 : ",  list1)

random.shuffle(list1)
print ("随机排序列表 : ",  list1)

# uniform(x, y) 随机生成下一个实数，它在[x,y]范围内。
print ("uniform(5, 10) 的随机数为 : ",  random.uniform(5, 10))

print ("uniform(7, 14) 的随机数为 : ",  random.uniform(7, 14))

'''
三角函数
    acos(x) 返回x的反余弦弧度值。
    asin(x) 返回x的反正弦弧度值。
    atan(x) 返回x的反正切弧度值。
    atan2(y, x) 返回给定的 X 及 Y 坐标值的反正切值。
    cos(x)  返回x的弧度的余弦值。
    hypot(x, y) 返回欧几里德范数 sqrt(x*x + y*y)。
    sin(x)  返回的x弧度的正弦值。
    tan(x)  返回x弧度的正切值。
    degrees(x)  将弧度转换为角度,如degrees(math.pi/2) ， 返回90.0
    radians(x)  将角度转换为弧度
'''
print("acos(0.64) : ",  math.acos(0.64))
print("acos(0) : ",  math.acos(0))
print("acos(-1) : ",  math.acos(-1))
print("acos(1) : ",  math.acos(1))

print("asin(0.64) : ",  math.asin(0.64))
print("asin(0) : ",  math.asin(0))
print("asin(-1) : ",  math.asin(-1))
print("asin(1) : ",  math.asin(1))

print("atan(0.64) : ",  math.atan(0.64))
print("atan(0) : ",  math.atan(0))
print("atan(10) : ",  math.atan(10))
print("atan(-1) : ",  math.atan(-1))
print("atan(1) : ",  math.atan(1))

print("atan2(-0.50,-0.50) : ",  math.atan2(-0.50,-0.50))
print("atan2(0.50,0.50) : ",  math.atan2(0.50,0.50))
print("atan2(5,5) : ",  math.atan2(5,5))
print("atan2(-10,10) : ",  math.atan2(-10,10))
print("atan2(10,20) : ",  math.atan2(10,20))

print("cos(3) : ",  math.cos(3))
print("cos(-3) : ",  math.cos(-3))
print("cos(0) : ",  math.cos(0))
print("cos(math.pi) : ",  math.cos(math.pi))
print("cos(2*math.pi) : ",  math.cos(2*math.pi))

print("hypot(3, 2) : ",  math.hypot(3, 2))
print("hypot(-3, 3) : ",  math.hypot(-3, 3))
print("hypot(0, 2) : ",  math.hypot(0, 2))

print("sin(3) : ",  math.sin(3))
print("sin(-3) : ",  math.sin(-3))
print("sin(0) : ",  math.sin(0))
print("sin(math.pi) : ",  math.sin(math.pi))
print("sin(math.pi/2) : ",  math.sin(math.pi/2))

print("tan(3) : ",  math.tan(3))
print("tan(-3) : ",  math.tan(-3))
print("tan(0) : ",  math.tan(0))
print("tan(math.pi) : ",  math.tan(math.pi))
print("tan(math.pi/2) : ",  math.tan(math.pi/2))
print("tan(math.pi/4) : ",  math.tan(math.pi/4))

print("degrees(3) : ",  math.degrees(3))
print("degrees(-3) : ",  math.degrees(-3))
print("degrees(0) : ",  math.degrees(0))
print("degrees(math.pi) : ",  math.degrees(math.pi))
print("degrees(math.pi/2) : ",  math.degrees(math.pi/2))
print("degrees(math.pi/4) : ",  math.degrees(math.pi/4))

print("radians(3) : ",  math.radians(3))
print("radians(-3) : ",  math.radians(-3))
print("radians(0) : ",  math.radians(0))
print("radians(math.pi) : ",  math.radians(math.pi))
print("radians(math.pi/2) : ",  math.radians(math.pi/2))
print("radians(math.pi/4) : ",  math.radians(math.pi/4))










