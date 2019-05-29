#_*_coding:utf-8_*_
"""
1.元组，声明使用（）声明，
2.空的元组需加（，）
3.t = tuple(range(1,5))
4.不支持原位改变
5.支持的操作 x in t min/max/sum t.index()  t.count()
a,b = 5,10
Date:2019/5/29 20:34 
"""
t = (1,2,3,'tom',3.14,[99,100])
print(t)
print(type(t))
name = ('tom',) #声明一个字符的元组
print(name)
print(type(name))

for i in range(5):
    print('hello world!'+ str (i))