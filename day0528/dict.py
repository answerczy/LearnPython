#_*_coding:utf-8_*_
"""
声明：
emp = {'name':'tom','age':20 , 'salary':8000.00}
book = dict(title = 'python',author = 'tom',price = 90.00)

Set声明：
不包含重复的对象
S = {1,2,3,4} type(s) -> set
Date:2019/5/29 21:35 
"""
import sys

emp = {'name':'tom','age':20 , 'salary':8000.00}
#常用操作
print('age' in emp)
print(emp['name'])
print(emp.get('age'))
#遍历
item = emp.items()
print(item)
for k,v in item:
    print(k,v)
for k in emp.keys():
    print(k)
for v in emp.values():
    print(v)
#字典表增删改查操作
d = {'job':'dev'}
emp.update(d)
print(emp)
del emp['age']
emp.pop('job')
print(emp)

def say_hello():
    print('hello world!')
person = {'name':'jerry','hello':say_hello}  #不加括号不执行
person.get('hello')()

#列表推导
f1 = [x for x in range(1,10)]
print(f1)
f2= [x + y for x in 'ABCDE' for y in '1234567']
print(f2)
print(len(f2))
#用列表的生成表达式语法创建列表容器
#用这种语法创建列表之后元素已经准备就绪，耗费时间较多
f3 = [x**2 for x in range(1,1000)]
print(sys.getsizeof(f3))
print(f3)
#通过下面代码创建的是一个列表而是一个生成器对象
#通过生成器可以获取到数据，但是不占额外的空间存储数据
#每次需要数据通过内部运算得到,遍历得到
f4 = (x**2 for x in range(1,100))   #得到一个生成器generator
print(sys.getsizeof(f4))
print(f4)
for val in f4:
    print(val)