#_*_coding:utf-8_*_
"""
声明：
emp = {'name':'tom','age':20 , 'salary':8000.00}
book = dict(title = 'python',author = 'tom',price = 90.00)
Date:2019/5/29 21:35 
"""
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