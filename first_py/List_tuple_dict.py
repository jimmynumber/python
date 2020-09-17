#!/usr/bin/python
# -*- coding: UTF-8 -*-

#coding:utf-8
# list tuple 函数雷同
print("len([1, 2, 3]) 长度:",len([1, 2, 3]))
print("[1, 2, 3] + [4, 5, 6] 组合:",[1, 2, 3] + [4, 5, 6])
print("['Hi!'] * 4 重复:",['Hi!'] * 4)
print("3 in [1, 2, 3] 元素是否存在于列表中:",3 in [1, 2, 3])
print([x for x in [1, 2, 3]])
for x in [1, 2, 3]: #迭代
    print(x,)    

list1 = [123, 456,789]
print("len(list) 列表元素个数:",len(list1))
print("max(list) 返回列表元素最大值:",max(list1))
print("min(list) 返回列表元素最小值:",min(list1))
print("list(('1','2','3')) 将元组转换为列表:",list(('1','2','3')))
'''
方法
    list.append(obj)       在列表末尾添加新的对象
    list.count(obj)        统计某个元素在列表中出现的次数
    list.extend(seq)       在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
    list.index(obj)        从列表中找出某个值第一个匹配项的索引位置
    list.insert(index, obj)将对象插入列表
    list.pop(obj=list[-1]) 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
    list.remove(obj)       移除列表中某个值的第一个匹配项
    list.reverse()         反向列表中元素
    list.sort([func])      对原列表进行排序
'''
aList = [123, 'xyz', 'zara', 'abc'];
print("A List : ", aList.pop());
print("B List : ", aList.pop(2));

print("----------------------------------------------------------------------------------");
'''
set 集合内置方法完整列表
方法                               描述
add()                             为集合添加元素  
clear()                           移除集合中的所有元素  
copy()                            拷贝一个集合  
difference()                      返回多个集合的差集  
difference_update()               移除集合中的元素，该元素在指定的集合也存在。  
discard()                         删除集合中指定的元素  
intersection()                    返回集合的交集  
intersection_update()             返回集合的交集。  
isdisjoint()                      判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False。  
issubset()                        判断指定集合是否为该方法参数集合的子集。  
issuperset()                      判断该方法的参数集合是否为指定集合的子集  
pop()                             随机移除元素  
remove()                          移除指定元素  
symmetric_difference()            返回两个集合中不重复的元素集合。  
symmetric_difference_update()     移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中。  
union()                           返回两个集合的并集  
update()                          给集合添加元素  
'''    
print("----------------------------------------------------------------------------------");
'''
内置方法
    dict.clear()                删除字典内所有元素
    dict.copy()                 返回一个字典的浅复制
    dict.fromkeys(seq[, val])   创建一个新字典，以序列 seq 中元素做字典的键，val 为字典所有键对应的初始值
    dict.get(key, default=None) 返回指定键的值，如果值不在字典中返回default值
    dict.setdefault(key, default=None)   和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
    dict.has_key(key)           如果键在字典dict里返回true，否则返回false
    dict.items()                以列表返回可遍历的(键, 值) 元组数组
    dict.update(dict2)          把字典dict2的键/值对更新到dict里
    dict.keys()                 以列表返回一个字典所有的键
    dict.values()               以列表返回字典中的所有值
    pop(key[,default])          删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
    popitem()                   随机返回并删除字典中的一对键和值。
'''
dict1 =  {'user':'runoob','num':[1,2,3]}
 
dict2 = dict1          # 浅拷贝: 引用对象
dict3 = dict1.copy()   # 深拷贝  父对象（一级目录），子对象（二级目录）不拷贝，还是引用
 
# 修改 data 数据
dict1['user']='root'
dict1['num'].remove(1)
 
# 输出结果
print(dict1)
print(dict2)
print(dict3)
'''
实例中 dict2 其实是 dict1 的引用（别名），所以输出结果都是一致的，dict3 父对象进行了深拷贝，
不会随dict1 修改而修改，子对象是浅拷贝所以随 dict1 的修改而修改。
{'num': [2, 3], 'user': 'root'}
{'num': [2, 3], 'user': 'root'}
{'num': [2, 3], 'user': 'runoob'}
'''
seq = ('name', 'age', 'sex')
dict1 = dict.fromkeys(seq)
print("New Dictionary : %s" %  str(dict1))
dict1 = dict.fromkeys(seq, 10)
print("New Dictionary : %s" %  str(dict1))

dict1 = {'Name': 'Zara', 'Age': 27}

print("Value : %s" %  dict1.get('Age'))
print("Value : %s" %  dict1.get('Sex', "Never"))
print("set : %s" %  dict1.setdefault('Sex', "ko"))

if 'Name' in dict1: 
    print("get : %s" %  dict1.get('Name', "ko"))

dict1 = {'Name': 'Runoob', 'Age': 7}
print ("Value : %s" %  dict1.items(str1

dict1 = {'Name': 'Zara', 'Age': 7}
dict2 = {'Sex': 'female','Age': 5 str1
dict1.update(dict2)
print("Value : %s" %  dict1);


print("Value : %s" %  dict1.keys());
print("Value : %s" %  dict1.values());

site= {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
pop_obj=site.pop('name')
print(pop_obj)

site= {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
pop_obj=site.popitem()
print(pop_obj)
print(site)


