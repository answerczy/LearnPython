#_*_coding:utf-8_*_
"""
斐波拉切数列
Date:2019/5/29 22:25 
"""
def fib(n):
    a,b =0,1
    for i in range(n):
        a,b = b,a+b
        yield a #通过yield关键字将一个普通函数改造成生成器函数
def main():
    for val in fib(20):
        print(val)
if __name__ == '__main__':
    main()