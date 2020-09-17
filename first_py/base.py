'''
在文件开头加入 # -*- coding: UTF-8 -*- 或者 #coding=utf-8 解决中文乱码
'''
#!/usr/bin/python
# -*- coding: UTF-8 -*-
print('张晓宝');
#*************************
total = 'item_one' + \
        'item_two' + \
        'item_three';
print('total:'+total) ;  
x="a";
y="b";
# 换行输出
print(x,y),
print(y),   

# if elif else
x=5;
y=5;
if x < y : 
    print(x);
elif x == y : 
    print(x);
else :  
    print(y);

counter = 100 # 赋值整型变量
miles = 1000.0 # 浮点型
name = "John" # 字符串
 
print(counter) 
print(miles) 
print(name) 

a = b = c = 1
print(a,b,c) 
a, b, c = 1, 2, "john"
print(a,b,c) 

s = 'Hello World!'
print (s )          # 输出完整字符串
print (s[0] )       # 输出字符串中的第一个字符
print (s[2:5])      # 输出字符串中第三个至第五个之间的字符串
print (s[2:])       # 输出从第三个字符开始的字符串
print (s * 2)       # 输出字符串两次
print (s + "TEST")  # 输出连接的字符串

#List 列表
list1 = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
print (list1  )             # 输出完整列表
print (list1[0] )           # 输出列表的第一个元素
print (list1[1:3] )         # 输出第二个至第三个元素 
print (list1[2:])           # 输出从第三个开始至列表末尾的所有元素
print (tinylist * 2  )     # 输出列表两次
print (list1 + tinylist  )  # 打印组合的列表

#Tuple 元组
tuple1 = ( 'runoob', 786 , 2.23, 'john', 70.2 )
tinytuple = (123, 'john')
print (tuple1  )             # 输出完整元组
print (tuple1[0] )           # 输出元组的第一个元素
print (tuple1[1:3] )         # 输出第二个至第三个的元素 
print (tuple1[2:])           # 输出从第三个开始至列表末尾的所有元素
print (tinytuple * 2  )     # 输出元组两次
print (tuple1 + tinytuple  ) # 打印组合的元组
 
# Dictionary 字典    
dict1 = {}
dict1['one'] = "This is one"
dict1[2] = "This is two"
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
print(dict1['one'])          # 输出键为'one' 的值
print(dict1[2])              # 输出键为 2 的值
print(tinydict)             # 输出完整的字典
print(tinydict.keys())      # 输出所有键
print(tinydict.values())    # 输出所有值

print( int())               # 不传入参数时，得到结果0
print( int(3))
print( int(3.6))
print( int('12',16))        # 如果是带参数base的话，12要以字符串的形式进行输入，12 为 16进制
print( int('0xa',16))  
print( int('10',8) ) 

print(float(1))
print(float(112)) 
print(float(-123.6)) 
print(float('123') ) 

print(complex(1, 2))
print(complex(1)) # 数字
print(complex("1"))  # 当做字符串处理
# 注意：这个地方在"+"号两边不能有空格，也就是不能写成"1 + 2j"，应该是"1+2j"，否则会报错
print(complex("1+2j")) 

s = 'RUNOOB'
print('str(s):'+str(s))
print('repr(s):'+repr(s))
dict1 = {'runoob': 'runoob.com', 'google': 'google.com'};
print('str(dict1):'+str(dict1))
print('repr(dict1):'+repr(dict1))

x = 7
print(eval('1+1'))
print(eval('pow(2,2)'))
print(eval('2 + 2'))
n=81
print(eval("n + 4"))

print(tuple([1,2,3,4]))
print(tuple({1:2,3:4}))    #针对字典 会返回字典的key组成的tuple
print(tuple((1,2,3,4)))    #元组会返回元组自身

print(list([1,2,3,4]))
print(list({1:2,3:4}))    
print(list((1,2,3,4)))    

print(dict(a='1', b='2', t='3'))
# 传入关键字 {'a': '1', 'b': '2', 't': '3'}
print(dict(zip(['one', 'two', 'three'], [1, 2, 3])))
# 映射函数方式来构造字典 {'three': 3, 'two': 2, 'one': 1}
print(dict([('one', 1), ('two', 2), ('three', 3)]) )
# 可迭代对象方式来构造字典 {'three': 3, 'two': 2, 'one': 1}

x = set('runoob')
y = set('google')

#(set(['b', 'r', 'u', 'o', 'n']), set(['e', 'o', 'g', 'l']))   # 重复的被删除
print (x,y)
# 交集 set(['o'])
print (x & y)
# 并集 set(['b', 'e', 'g', 'l', 'o', 'n', 'r', 'u'])
print (x | y)
# 差集 set(['r', 'b', 'u', 'n'])
print (x - y)

a = frozenset(range(10)) 
print(a    )
# 生成一个新的不可变集合     frozenset([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
b = frozenset('runoob') 
print(b)
# 创建不可变集合    frozenset(['b', 'r', 'u', 'o', 'n'])

print(chr(0x30), chr(0x31), chr(0x61))   
# 十六进制 0 1 a
print(chr(48), chr(49), chr(97))         
# 十进制 0 1 a

print(hex(255))
# '0xff'
print(hex(-42))
# '-0x2a'
print(hex(1))
# '0x1'

print(oct(10))
# '012' 十进制转八进制
print(oct(20))
# '024' 十进制转八进制
print(oct(15))
# '017' 十进制转八进制

print(5/3)   # 1.6666666666666667
print(5%3)   # 2
print(5//3)  # 1
print(2**3)  # 8

a,b=10,20
print(a,b) 
print(a and b)        #  x and y    布尔"与"  - 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。    (a and b) 返回 20。
print(a or b)         #  x or y    布尔"或"  - 如果 x 是非 0，它返回 x 的值，否则它返回 y 的计算值。    (a or b) 返回 10。
print( not (a and b)) #  not x    布尔"非"  - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。    not(a and b) 返回 False

a = 60            # 60 = 0011 1100 
b = 13            # 13 = 0000 1101 
c = 0
c = a & b;        # 12 = 0000 1100
print ("1 - c 的值为：", c)
c = a | b;        # 61 = 0011 1101 
print ("2 - c 的值为：", c)
c = a ^ b;        # 49 = 0011 0001
print ("3 - c 的值为：", c)
c = ~a;           # -61 = 1100 0011
print ("4 - c 的值为：", c)
c = a << 2;       # 240 = 1111 0000
print ("5 - c 的值为：", c)
c = a >> 2;       # 15 = 0000 1111
print ("6 - c 的值为：", c)

a = 10
b = 20
list1 = [1, 2, 3, 4, 5 ];
 
if ( a in list1 ): print ("1 - 变量 a 在给定的列表中 list1 中")
else: print ("1 - 变量 a 不在给定的列表中 list1 中")
 
if ( b not in list1 ): print ("2 - 变量 b 不在给定的列表中 list1 中")
else: print ("2 - 变量 b 在给定的列表中 list1 中")
 
# 修改变量 a 的值
a = 2
if ( a in list1 ): print ("3 - 变量 a 在给定的列表中 list1 中")
else: print ("3 - 变量 a 不在给定的列表中 list1 中")

i = 1
while i < 10:   
    i +=1
    if i%2 > 0:     # 非双数时跳过输出
        continue
    print (i)         # 输出双数2、4、6、8、10

i = 1
while 1:            # 循环条件为1必定成立
    print (i)         # 输出1~10
    i += 1
    if i > 10:     # 当i大于10时跳出循环
        break

count = 0
while count < 5:
    print (count, " is  less than 5")
    count = count + 1
else:
    print (count, " is not less than 5")
    
for letter in 'Python':     # 第一个实例
    print ('当前字母 :', letter)
 
fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # 第二个实例
    print ('当前水果 :', fruit)
 
print ("Good bye!")
 
 
fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
    print ('当前水果 :', fruits[index])
 
print ("Good bye!")

for num in range(10,20):  # 迭代 10 到 20 之间的数字
    for i in range(2,num): # 根据因子迭代
        if num%i == 0:      # 确定第一个因子
            j=num/i          # 计算第二个因子
            print ('%d 等于 %d * %d' % (num,i,j))
            break            # 跳出当前循环
    else:                  # 循环的 else 部分
        print (num, '是一个质数')   

print (range(0, 5))
rows = 5
i = j = k = 1 
'''
#声明变量，i用于控制外层循环（图形行数），
j用于控制空格的个数，k用于控制*的个数
#等腰直角三角形1
'''
print ("等腰直角三角形1")
for i in range(0, rows):
    for k in range(0, rows - i):
        print (" * ",end=''    ) #注意这里的","，一定不能省略，可以起到不换行的作用
        k += 1
    i += 1
    print ("\n")   
    
rows=5
print( range(0, rows + 1))
#打印实心等边三角形
print("打印空心等边三角形，这里去掉if-else条件判断就是实心的")
for i in range(0, rows + 1):#变量i控制行数
    for j in range(0, rows - i):#(1,rows-i)
        print("s1",end='')
        j += 1
    for k in range(0, 2 * i - 1):#(1,2*i)
        if k == 0 or k == 2 * i - 2 or i == rows:
            if i == rows:
                if k % 2 == 0:#因为第一个数是从0开始的，所以要是偶数打印*，奇数打印空格
                    print("K1",end='')
                else:
                    print("s2",end='') #注意这里的","，一定不能省略，可以起到不换行的作用
            else:
                print("K2",end='')
        else:
            print("s3",end='')
        k += 1
    print("\n")
    i += 1   
    
rows=5
print( range(0, rows + 1))
#打印菱形
print("打印空心等菱形，这里去掉if-else条件判断就是实心的")
for i in range(rows):#变量i控制行数
    for j in range(rows - i):#(1,rows-i)
        print("s1",end='')
        j += 1
    for k in range(2 * i - 1):#(1,2*i)
        if k == 0 or k == 2 * i - 2:
            print("k1",end='')
        else:
            print("s2",end='')
        k += 1
    print("\n")
    i += 1
#菱形的下半部分
for i in range(rows):
    for j in range(i):#(1,rows-i)
        print("s3",end='')
        j += 1
    for k in range(2 * (rows - i) - 1):#(1,2*i)
        if k == 0 or k == 2 * (rows - i) - 2:
            print("k2",end='')
        else:
            print("s4",end='')
        k += 1
    print("\n")
    i += 1        
        
rows=5
print(  range(0, rows + 1))
#实心正方形
print( "实心正方形")
for i in range(0, rows):
    for k in range(0, rows):
        print( " * ",end='') #注意这里的","，一定不能省略，可以起到不换行的作用
        k += 1
    i += 1
    print( "\n")
 
#空心正方形
print( "空心正方形")
for i in range(0, rows):
    for k in range(0, rows):
        if i != 0 and i != rows - 1:
            if k == 0 or k == rows - 1:
                #由于视觉效果看起来更像正方形，所以这里*两侧加了空格，增大距离
                print( " 1 ",end='') #注意这里的","，一定不能省略，可以起到不换行的作用
            else:
                print( "   ",end='') #该处有三个空格
        else:
            print( " 2 ",end='') #这里*两侧加了空格
        k += 1
    i += 1
    print( "\n")        
        
print (range(0, 5))
rows = 5
i = j = k = 1 
'''
#声明变量，i用于控制外层循环（图形行数），
j用于控制空格的个数，k用于控制*的个数
#等腰直角三角形1
'''
print ("等腰直角三角形1")
for i in range(0, rows):
    for k in range(0, rows - i):
        print (" * ",end=''    ) #注意这里的","，一定不能省略，可以起到不换行的作用
        k += 1
    i += 1
    print ("\n")   
    
rows=5
print( range(0, rows + 1))
#打印实心等边三角形
print("打印空心等边三角形，这里去掉if-else条件判断就是实心的")
for i in range(0, rows + 1):#变量i控制行数
    for j in range(0, rows - i):#(1,rows-i)
        print("s1",end='')
        j += 1
    for k in range(0, 2 * i - 1):#(1,2*i)
        if k == 0 or k == 2 * i - 2 or i == rows:
            if i == rows:
                if k % 2 == 0:#因为第一个数是从0开始的，所以要是偶数打印*，奇数打印空格
                    print("K1",end='')
                else:
                    print("s2",end='') #注意这里的","，一定不能省略，可以起到不换行的作用
            else:
                print("K2",end='')
        else:
            print("s3",end='')
        k += 1
    print("\n")
    i += 1   
    
rows=5
print( range(0, rows + 1))
#打印菱形
print("打印空心等菱形，这里去掉if-else条件判断就是实心的")
for i in range(rows):#变量i控制行数
    for j in range(rows - i):#(1,rows-i)
        print("s1",end='')
        j += 1
    for k in range(2 * i - 1):#(1,2*i)
        if k == 0 or k == 2 * i - 2:
            print("k1",end='')
        else:
            print("s2",end='')
        k += 1
    print("\n")
    i += 1
#菱形的下半部分
for i in range(rows):
    for j in range(i):#(1,rows-i)
        print("s3",end='')
        j += 1
    for k in range(2 * (rows - i) - 1):#(1,2*i)
        if k == 0 or k == 2 * (rows - i) - 2:
            print("k2",end='')
        else:
            print("s4",end='')
        k += 1
    print("\n")
    i += 1   






