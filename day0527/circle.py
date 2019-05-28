#_*_coding:utf-8_*_
"""
输入半径计算园的周长和面积
Date:2019/5/28 20:46 
"""
import math
radius = float (input('请输入园的半径：'))
perimeter = 2 * math.pi * radius
area = math.pi * radius * radius
print('周长:%.2f' %perimeter)
print('面积:%.2f' %area)

