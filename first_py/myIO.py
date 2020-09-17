#!/usr/bin/python
# -*- coding: UTF-8 -*-
#coding:utf-8

from io import BytesIO
from io import StringIO
import io
import json
import os
import pickle


print("How old are you?"),
'''
age = input()
print ("so %s old" %age )

str1= input("请输入：");
print ("你输入的内容是: ", str1);
# [x*5 for x in range(2,10,2)]
'''

'''
close()： 冲洗并关闭此流，一旦文件关闭，对文件的任何操作都会引发一次ValueError异常
closed()：如果流文件被关闭则返回True否则返回False
fileno()：返回流的底层文件描述符为整数
flush()： 刷新流到写入缓冲区
isatty()：如果流是交互式即连接到终端设备则返回True否则返回False
readable()：如果可以从流中读取则返回True否则返回False
readline(size=-1)：从流中读取并返回一行，如果size指定，则读取指定大小字节的数据
readlines(hint=-1)：从流中读取并返回行列表，可以指定hint来控制读取的行数。
seek(offset[,whence])：将柳位置更改为给定的字节偏移量（offset），whence为偏移量指示位置，
                       默认为SEEK_SET即0流的开始位置，必须为0或者正整数，
                       SEEK_CUR或1为当前流位置，SEEK_END或2为流的结尾。
seekable()：如果流支持随机访问则返回True否则返回false
tell()：    返回当前流的位置
truncate(size=None)：将流大小调整为以字节为单位的给定大小（size），返回新的文件大小
writable()：         如果流支持写入则返回true，否则返回false
writelines()：       写入流列表，不提供换行符
__del__()：          销毁对象，close()方法为此方法的默认实现


read(size=-1)：从对象中读取size指定大小的字节并返回，
               如果size未指定或为-1则返回EOF之前的所有字节，
               如果对象为非阻塞且没有读取字节则返回None
readall()：   读取并返回流中的所有字节
readinto(b)： 将字节读入预先分配的可写类字节对象b，并返回读取的字节数，读取 完返回None
write(b)：    写入给定类字节对象b，并返回写入字节的数目
'''

output=io.StringIO()
output.write('nihao')
print(output.getvalue())
output.close()

input1 = io.StringIO('Inital value for read buffer')
print(input1.read())

#通过文本创建二进制流可以使用‘b’的模式字符串
#f_b = open("myfile.jpg",'rb')
#通过内存创建二进制流可以使用io的BytesIO方法
f_b_m = io.BytesIO(b"some initial binary data:\x00\x01");
print(f_b_m.getvalue());

b = io.BytesIO(b'abcdef')
view = b.getbuffer()
view[2:4] = b'56'
print(b.getvalue())

#文件创建文本流
#


try:
    f = open('D:\\文件\\temp\\myfile.txt','r',encoding='utf-8')
    for line in f.readlines():
        print(line.strip()) # 把末尾的'\n'删掉
    #result_val=f.read();
    #print('result_val :'+result_val);
finally:
    if f:
        f.close();
        
print('---with---和前面的try ... finally是一样的，但是代码更佳简洁，并且不必调用f.close()方法。-------------------------------------');

with open('D:\\文件\\temp\\myfile.txt','r',encoding='utf-8',errors='ignore') as f:
    print(f.read());

'''
with open('C:\\Users\\00320558\\Desktop\\ko.jpg','rb') as f:
    print(f.read()); # 十六进制表示的字节
'''
    
print('--------写文件-------------');   
try:
    f = open('D:\\文件\\temp\\myfile.txt','w',encoding='utf-8');
    f.write('Hello, world!');
    #result_val=f.read();
    #print('result_val :'+result_val);
finally:
    if f:
        f.close();
        
with open('D:\\文件\\temp\\myfile.txt', 'w') as f:
    f.write('Hello, world 2222 !')        
        
with open('D:\\文件\\temp\\myfile.txt','r',encoding='utf-8',errors='ignore') as f:
    print(f.read());
 
f = StringIO()
f.write('hello') # 5
f.write(' ') # 1
f.write('world!') # 6
print(f.getvalue()) # hello world!
 
f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

f = BytesIO()
f.write('中文'.encode('utf-8')) # 6
print(f.getvalue()) # b'\xe4\xb8\xad\xe6\x96\x87'
 
# 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
print("os.name :",os.name);
print("os.environ :",os.environ);
print("os.environ.get('PATH') :",os.environ.get('PATH'));

# 查看当前目录的绝对路径:
print(os.path.abspath('.')); # D:\\Users\\00320558\\workspace_sms\\first_py
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
print(os.path.join('D:\\Users\\00320558\\workspace_sms\\first_py', 'testdir'));
print(os.mkdir('D:\\Users\\00320558\\workspace_sms\\first_py\\testdir'));  # 然后创建一个目录:
print(os.rmdir('D:\\Users\\00320558\\workspace_sms\\first_py\\testdir'));  # 删掉一个目录:

# 通过os.path.split()函数， 路径拆分为两部分 最后级别的目录或文件名
print(os.path.split('D:\\文件\\temp\\myfile.txt'))

# os.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便：
print(os.path.splitext('D:\\文件\\temp\\myfile.txt'));

# 对文件重命名:
#os.rename('D:\\文件\\temp\\myfile.txt', 'D:\\文件\\temp\\myfile.py')
# 删掉文件:
#os.remove('D:\\文件\\temp\\myfile.txt')

print([x for x in os.listdir('.') if os.path.isdir(x)]);
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']);

d = dict(name='Bob', age=20, score=88)
print(d);
print(pickle.dumps(d));

d= dict(name='Bob', age=20, score=88);
print(json.dumps(d)) #'{"age": 20, "score": 88, "name": "Bob"}';

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str))


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 20, 88)
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }
print(json.dumps(s,default=student2dict))
print(json.dumps(s, default=lambda obj: obj.__dict__))

def dict2student(d):
    return Student(d['name'], d['age'], d['score'])
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))

# 给出当前的目录
print(os.getcwd())
# 将当前目录改为"D:\\文件\\temp\\"
print(os.chdir("D:\\文件\\temp\\"))
print(os.getcwd()) #D:\文件\temp