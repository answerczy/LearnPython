#_*_coding:utf-8_*_
"""
输入年份，如果是闰年则输出True，否则输出Flase
Date:2019/5/28 20:51 
"""
year = int(input('请输入年份：'))
is_leap = (year % 4 == 0 and year % 100 != 0 or year % 400 == 0)
print(is_leap)