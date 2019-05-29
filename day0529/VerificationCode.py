#_*_coding:utf-8_*_
"""
description
Date:2019/5/29 22:45 
"""
import random


def generate_code(code_len= 4):
    """

    :param code_len: 验证码长度为4（默认为4个字符）
    :return: 由大小写英文字母和数字构成的随机验证码
    """
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars)  - 1
    code = ''
    for i in range(code_len):
        # index = random.randint(0,last_pos)
        # code += all_chars[index]
        code += random.choice(all_chars)
    print(code)
    return code  #结束函数

if __name__ == '__main__':
    generate_code()