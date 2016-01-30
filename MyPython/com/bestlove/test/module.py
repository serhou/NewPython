# !/usr/bin/env python3
# -*- coding: utf-8 -*-

'一个测试模块'

__author__='think'

import sys
'''
    正常函数和变量名是公开的Public
    特殊函数和变量
    __xxx__ 如：__author__ __name__
    私有变量和函数 用于封装 OOP
    _xxx  private
    __xxx private
'''

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello,World!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')
    print(args)

if __name__ == '__main__':
    test()