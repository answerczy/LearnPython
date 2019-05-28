#_*_coding:utf-8_*_
#@author：Casonchen
from decimal import Decimal
#精度更高的场合的浮点型计算使用Decimal类，传参使用字符串传参。Decimal('0.1')
result = 5 + 3
print(type(result))  #int  二进制0b1101换算成10进制为2^0+2^2+2^3=13
print(type(3.4))     #float
print(type('tome')) #str
l  = [3,7,9,4,2]
x = l.sort() #sort函数只影响本身列表
print(x is None)   #空对象
print(5 > 3) #True
print(5 < 3) #False
print(type(5<3))  #bool类型
print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3'))

"""
True对应数值1，False对应数值0
对应转换功能，有值就为True。真值测试bool(1)->Ture bool(0)->False   bool(3) = False  bool(None)->False
"""