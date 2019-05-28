#_*_coding:utf-8_*_
"""
运算符的使用
Date:2019/5/28 20:57 
"""
a = 5
b = 10
c = 3
d = 4
e = 5
a += b
a -= c
a *= d
a /= e
print('a = ',a)
flag1 = 3 >2
flag2 = 2 <1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not flag1
print(flag1,flag2,flag3,flag4,flag5)
print(flag1 is True)
print(flag2 is not True)