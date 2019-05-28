"""
1.== 判断字面值是否相等
2.is 判断引用地址是否相同
3.字符0-255的会被缓存起来，1个比特位，8个字节，2^^8
"""

x = 'tom'
y = 'jerry'
print(id(x))
print(id(y))
print('x与y是否相等结果:',x==y)  #结果为false
a = 50
b = 50
c = 5000
d = 5000
print('a与b字面值相比较结果：',a == b)
print('a与b内存地址相比较结果：',a is b) #结果为True
print('c与d字面值相比较结果：',c == d)
print(id(c))
print(id(d))
print('c与d内存地址相比较结果：',c is d) #这里的内存地址还是一样

url = 'http://www.codeclassroom.com'
link = 'http://www.codeclassroom.com'
print(id(url))
print(id(link))
