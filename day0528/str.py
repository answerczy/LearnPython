#_*_coding:utf-8_*_
"""
字符串声明：单引号声明、双引号声明、三引号声明
常用方法：
str.replace('a','b') 把a替换成b
str.capitalize() 首字母大写  str.upper()  全部大写  str.lower()  全部小写
str.spilt('.')  按.拆分不同部分   str.join()  分隔符连接序列  '.'.join(['www','codeclassroom','com'])
str.format() 格式化输出
Date:2019/5/29 21:08 
"""
name  = 'tom'
age = 20
job = 'dev'
print('姓名：{0}, 年龄：{1}， 工作：{2}'.format(name,age,job))

#打印指定位数的小数
print('%.3f'%3.1415926)
print('{:.3f}'.format(3.141513))
