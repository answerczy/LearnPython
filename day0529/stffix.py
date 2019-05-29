#_*_coding:utf-8_*_
"""
description
Date:2019/5/29 23:00 
"""
def get_suffix(filename,has_dot=True):
    """
    rfind()函数：返回字符串最后一次出现的位置，如果没有匹配项则返回-1。
    :param filename:
    :param has_dot: 返回后缀名是否带点
    :return: 文件后缀名
    """
    pos = filename.rfind('.')  #pos = 4
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1  #三元表达式
        print(filename[index:])
        return filename[index:]
    else:
        return ''
if __name__ == '__main__':
    get_suffix('demo.py')