#_*_coding:utf-8_*_
"""
description
Date:2019/5/29 22:39 
"""
import os

import time


def main():
    content = '北京欢迎你为你开天辟地....'
    while True:
        # 清理屏幕上的输出
        os.system('cls')
        print(content)
        time.sleep(0.2)
        content = content[1:] + content[0]
if __name__ == '__main__':
    main()