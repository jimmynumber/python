#!/usr/bin/python
# -*- coding: UTF-8 -*-
#coding:utf-8

#可写函数说明
def printme( str1 ):
    #"打印任何传入的字符串"
    print(str1);
    return;

#调用printme函数
printme(1);

#可写函数说明
def printme1( str1 ):
    "打印任何传入的字符串"
    print (str1);
    return;
 
#调用printme函数
printme1( str1 = "My string");
 

#可写函数说明
def printinfo( name, age ):
    "打印任何传入的字符串"
    print ("Name: ", name);
    print ("Age ", age);
    return;
 
#调用printinfo函数
printinfo( age=50, name="miki" );
 
#可写函数说明
def printinfo1( name, age = 35 ):
    #"打印任何传入的字符串"
    print ("Name: ", name);
    print ("Age ", age);
    return;
 
#调用printinfo函数
printinfo1( age=50, name="miki" );
printinfo1( name="miki" );

# 可写函数说明
def printinfo2( arg1, *vartuple ):
    "打印任何传入的参数"
    print ("输出: ");
    print (arg1);
    for var in vartuple:
        print(var)
    return;
 
# 调用printinfo2 函数
printinfo2( 10 );
printinfo2( 70, 60, 50 );
 
# 可写函数说明
sum1 = lambda arg1, arg2: arg1 + arg2;
 
# 调用sum函数
print("相加后的值为 : ", sum1( 10, 20 ))
print("相加后的值为 : ", sum1( 20, 20 ))

def outerFunc():
    print('Outer Funtion');
    def innerFunc():
        print('Inner Function');
    innerFunc();

outerFunc();

def FuncX(x):
    def FuncY(y):
        return x * y
    return FuncY

tempFunc = FuncX(3)
result = tempFunc(5)
print(result)  # 15

result = FuncX(3)(5)
print(result)  # 15

print("lambda函数的语法只包含一个语句： lambda [arg1 [,arg2,.....argn]]:expression ")

square = lambda x : x**2
print(square(3))  # 9

sum1 = lambda  x, y : x + y
print(sum1(2, 3))  # 5

reslut = filter(None, [1, 0, False, True])
print(list(reslut))  # [1, True]

def odd(num):
    return num % 2

reslut = filter(odd, range(10))
print(list(reslut))  # [1, 3, 5, 7, 9]

reslut = filter(lambda num: num % 2, range(10) )
print(list(reslut))  # [1, 3, 5, 7, 9]







