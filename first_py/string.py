#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re
import sys


#coding:utf-8
print('--------------转义字符---------------------------')
print('反斜杠符号',end='\\')
print('---------------------',end='\n\r')
print('单引号',end='\'')
print('---------------------',end='\n\r')
print('双引号',end='\"')
print('---------------------',end='\n\r')
print('响铃',end='\a')
print('---------------------',end='\n\r')
print('退格(Backspace)',end='\b')
print('---------------------',end='\n\r')
print('转义',end='\e')
print('---------------------',end='\n\r')
print('空',end='\000')
print('---------------------',end='\n\r')
print('换行',end='\n')
print('---------------------',end='\n\r')
print('纵向制表符',end='\v')
print('---------------------',end='\n\r')
print('横向制表符',end='\t')
print('---------------------',end='\n\r')
print('回车',end='\r')
print('---------------------',end='\n\r')
print('换页',end='\f')
print('---------------------',end='\n\r')
print('八进制数，yy代表的字符，例如：\o12代表换行',end='\o12')
print('---------------------',end='\n\r')
print('十六进制数，yy代表的字符，例如：\x0a代表换行',end='\x0a')
print('---------------------',end='\n\r')
print('其它的字符以普通格式输出',end='\other')
print('---------------------',end='\n\r')

print('--------------字符串运算符---------------------------')
a = "Hello"
b = "Python"
print ("a + b 输出结果：", a + b )
print ("a * 2 输出结果：", a * 2 )
print ("a[1] 输出结果：", a[1] )
print ("a[1:] 输出结果：", a[1:] )
print ("a[1:4] 输出结果：", a[1:4] )

if( "H" in a) :
    print ("H 在变量 a 中" )
else :
    print ("H 不在变量 a 中" )

if( "M" not in a) :
    print ("M 不在变量 a 中" )
else :
    print ("M 在变量 a 中")

print (r'\n')
print (R'\n')
'''
字符串格式化
符   号   描述
  %c      格式化字符及其ASCII码
  %s      格式化字符串
  %d      格式化整数
  %u      格式化无符号整型
  %o      格式化无符号八进制数
  %x      格式化无符号十六进制数
  %X      格式化无符号十六进制数（大写）
  %f      格式化浮点数字，可指定小数点后的精度
  %e      用科学计数法格式化浮点数
  %E      作用同%e，用科学计数法格式化浮点数
  %g      %f和%e的简写
  %G      %f 和 %E 的简写
  %p      用十六进制数格式化变量的地址
'''
print ("My name is %s and weight is %d kg!" % ('Zara', 21) )

'''
格式化操作符辅助指令:
符号            功能
*       定义宽度或者小数点精度
-       用做左对齐
+       在正数前面显示加号( + )
<sp>    在正数前面显示空格
#       在八进制数前面显示零('0')，在十六进制前面显示'0x'或者'0X'(取决于用的是'x'还是'X')
0       显示的数字前面填充'0'而不是默认的空格
%       '%%'输出一个单一的'%'
(var)   映射变量(字典参数)
m.n.    m 是显示的最小总宽度,n 是小数点后的位数(如果可用的话)
'''
print('--------------字符串内建函数---------------------------')
str1 = "this is\tstring example....wow!!!";
print ("Original string: " + str1)
print ("Defualt exapanded tab: " + str1.expandtabs())
print ("Double exapanded tab: " + str1.expandtabs(16))
'''
    string.center(width)   原字符串居中,使用空格填充至长度 width
    string.islower()       如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False
    string.isupper()       如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False
    string.isalnum()       如果 string 至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False
    string.isalpha()       如果 string 至少有一个字符并且所有字符都是字母则返回 True,否则返回 False
    string.isdigit()       如果 string 只包含数字则返回 True 否则返回 False.
    string.isdecimal()     如果 string 只包含十进制数字则返回 True 否则返回 False.
    string.isnumeric()     如果 string 中只包含数字字符，则返回 True，否则返回 False
    string.isspace()       如果 string 中只包含空格，则返回 True，否则返回 False.
    string.istitle()       如果 string 是标题化的(见 title())则返回 True，否则返回 False
'''
print("{} {}".format("hello", "world")  )  # 不设置指定位置，按默认顺序
print("{0} {1}".format("hello", "world"))  # 设置指定位置
print("{1} {0} {1}".format("hello", "world"))  # 设置指定位置

print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))
 
# 通过字典设置参数
site = {"name": "菜鸟教程", "url": "www.runoob.com"}
print("网站名：{name}, 地址 {url}".format(**site))
 
# 通过列表索引设置参数
my_list = ['菜鸟教程', 'www.runoob.com']
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的

class AssignValue(object):
    def __init__(self, value):
        self.value = value
my_value = AssignValue(6)
print('value 为: {0.value}'.format(my_value))  # "0" 是可选的

print("'{:.2f}'.format(3.1415926) 保留小数点后两位: ",'{:.2f}'.format(3.1415926))
print("'{:+.2f}'.format(3.1415926) 带符号保留小数点后两位: ",'{:+.2f}'.format(3.1415926))
print("'{:-.2f}'.format(-3.1415926) 带符号保留小数点后两位: ",'{:-.2f}'.format(-3.1415926))
print("'{:.0f}'.format(3.1415926) 不带小数: ",'{:.0f}'.format(3.1415926))
print("'{:0>2d}'.format(5) 数字补零 (填充左边, 宽度为2): ",'{:0>2d}'.format(5))
print("'{:x<4d}'.format(5) 数字补x  (填充右边, 宽度为4): ",'{:x<4d}'.format(5))
print("'{:,}'.format(1000000) 以逗号分隔的数字格式: ",'{:,}'.format(1000000))
print("'{:.2%}'.format(0.25) 百分比格式: ",'{:.2%}'.format(0.25))
print("'{:.2e}'.format(1000000000) 指数记法: ",'{:.2e}'.format(1000000000))
print("'{:10d}'.format(11) 右对齐 (默认, 宽度为10): ",'{:10d}'.format(11))
print("'{:<10d}'.format(11) 左对齐 (宽度为10): ",'{:<10d}'.format(11))
print("'{:^10d}'.format(11) 中间对齐 (宽度为10): ",'{:^10d}'.format(11))
'''
    ^, <, > 分别是居中、左对齐、右对齐，后面带宽度， 
    : 号后面带填充的字符，只能是一个字符，不指定则默认是用空格填充。
    + 表示在正数前显示 +，负数前显示 -；  
    （空格）表示在正数前加空格
    b、d、o、x 分别是二进制、十进制、八进制、十六进制。
    此外我们可以使用大括号 {} 来转义大括号
'''
print("'{:b}'.format(11) : ",'{:b}'.format(11))
print("'{:d}'.format(11) : ",'{:d}'.format(11))
print("'{:o}'.format(11) : ",'{:o}'.format(11))
print("'{:x}'.format(11) : ",'{:x}'.format(11))
print("'{:#x}'.format(11) : ",'{:#x}'.format(11))
print("'{:#X}'.format(11) : ",'{:#X}'.format(11))

print("'abcd'.capitalize() 字符串的第一个字符大写: ",'abcd'.capitalize())
print("'abcd'.upper() 转换 string 中的小写字母为大写: ",'abcd'.upper())
print("'ABCD'.lower() 转换 string 中所有大写字符为小写.: ",'ABCD'.lower())
print("'aBcD'.swapcase() 翻转 string 中的大小写: ",'aBcD'.swapcase())

print("'hello world'.title() 所有单词都是以大写开始，其余字母均为小写: ",'hello world'.title())
print("'abcd'.count('c', 0, 3) 字符串的第一个字符大写: ",'abcd'.count('c', 0, 3))

print("print1：",sys.getdefaultencoding())
name ="中国"
name = name.encode("utf-8")
print("print2：",type(name))
name = name.decode("utf-8")
print("print3：",type(name))
name = name.encode("gbk")
print("print4：",type(name))

print("'abcd'.startswith('a', 0,4) 检查字符串是否是以 obj 开头，是则返回 True，否则返回 False。: ",'abcd'.startswith('a', 0,4))
print("'abcd'.endswith('d', 0, 4)  检查字符串是否以   obj 结束，是则返回 True，否则返回 False。: ",'abcd'.endswith('d', 0, 4))
print("max('abcde') 返回字符串 str 中最大的字母。: ",max('abcde'))
print("min('abcde') 返回字符串 str 中最小的字母。: ",min('abcde'))

str1 = "this is string example....wow!!!"
print (str1.split( ))
# ['this', 'is', 'string', 'example....wow!!!']
print (str1.split('i',1))
# ['th', 's is string example....wow!!!']
print (str1.split('w'))
# ['this is string example....', 'o', '!!!']

mySent='This book is the best book on Python or M.L. I have ever laid eyes upon'
print(mySent.split())
#['This', 'book', 'is', 'the', 'best', 'book', 'on', 'Python', 'or', 'M.L.', 'I', 'have', 'ever', 'laid', 'eyes', 'upon']

regEx = re.compile('\\W')                               #正则表达式，定义分隔符是除单词、数字外的任意字符串
listOfTokens = regEx.split(mySent)                      #根据正则表达式的规则进行切分
print("re.compile('\\W').split(mySent):",listOfTokens)

print([it for it in listOfTokens if len(it) > 0]) #去掉空格
print([it.lower() for it in listOfTokens if len(it) > 2])   #全部小写，去掉长度小于3的单词

'''
表示符    描述
'\n'    换行
'\r'    回车
'\r\n'    回车 + 换行
'\v' 或 '\x0b'    行制表符
'\f' 或 '\x0c'    换表单
'\x1c'    文件分隔符
'\x1d'    组分隔符
'\x1e'    记录分隔符
'\x85'    下一行 (C1 控制码)
'\u2028'    行分隔符
'\u2029'    段分隔符
'''
a = 'ab c\n\nde fg\rkl\r\n'
print (a.splitlines())
#['ab c', '', 'de fg', 'kl']

b = 'ab c\n\nde fg\rkl\r\n'
print (b.splitlines(keepends=True))
#['ab c\n', '\n', 'de fg\r', 'kl\r\n']

print("'-'.join( ('a', 'b', 'c') 合并为一个新的字符串: ",'-'.join( ('a', 'b', 'c')))

#string.find(str, [[beg], end]) 
#string.rfind(str, beg,end)     类似于 find()函数，不过是从右边开始查找.
info = 'abca'
print(info.find('a'))    # 从下标0开始，查找在字符串里第一个出现的子串，返回结果：0
print(info.find('a',1))  # 从下标1开始，查找在字符串里第一个出现的子串：返回结果3
print(info.find('3'))    # 查找不到返回-1
'''
string.index(str, beg=0, end=len(string))     跟find()方法一样，只不过如果str不在 string中会报一个异常.
string.rindex( str, beg=0,end=len(string))     类似于 index()，不过是从右边开始.
string.ljust(width)     返回一个原字符串左对齐,并使用空格填充至长度 width 的新字符串
string.rjust(width)     返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串
string.zfill(width)     返回长度为 width 的字符串，原字符串 string 右对齐，前面填充0
string.strip([obj])     在 string 上执行 lstrip()和 rstrip()
string.lstrip()     截掉 string 左边的空格
string.rstrip()     删除 string 字符串末尾的空格.
string.maketrans(intab, outtab])     maketrans() 方法用于创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。
string.translate(str, del="")     根据 str 给出的表(包含 256 个字符)转换 string 的字符,要过滤掉的字符放到 del 参数中
string.replace(str1, str2,  num=string.count(str1)     把 string 中的 str1 替换成 str2     如果 num 指定，则替换不超过 num 次.
string.partition(str)     有点像 find()和 split()的结合体,从 str 出现的第一个位置起,把 字 符 串 string 分 成 一 个 3 元 素 的 元 组 (string_pre_str,str,string_post_str),如果 string 中不包含str 则 string_pre_str == string.
string.rpartition(str)     类似于 partition()函数,不过是从右边开始查找.
'''










