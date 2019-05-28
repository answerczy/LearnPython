#_*_coding:utf-8_*_
"""
description
Date:2019/5/28 21:58 
"""
import math
print(21/7)
print(21//7) #整除
print(22%7) #取余
print(math.floor(3.14)) #3
print(math.ceil(3.14)) #4
print(math.trunc(-3.14)) #总是向0的位置取值-3
print(round(3.14)) #四舍五入
"""
list列表的通用操作
增加：s.appeng(value) 系列相加s1+s2  s.extend(系列)
减少：s.pop()默认最后一个，s.pop(索引)  s.remove(value)   del s[0] del s[::2]
更改：s.insert(索引,值)
"""
s = list(range(1,11))
print(s[:3])
s[:3] = [99]
print(s)
s[::2] = [22,33,44,55]
print(s)
s.insert(1,100) #s[1:1] = 100
print(s)
s.reverse() #等价于s[::-1],只影响本身的列表
print(s)
print(s[::-1])
s.sort() #只影响列表本身
print(s)
people = ['tom','jerry','mike','peter','john']
people.sort()
print(people)
people.sort(key=lambda x:x[-1])
print(people)
print(sorted(people,key= lambda x:x[1]))