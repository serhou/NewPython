#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import struct

'''
Python 提供了一个struct模块来解决bytes和其他二进制数据类型的转换
'''


def my_test():
    # pack的第一个参数是处理指令，'>I'的意思是>表示字节顺序是big-endian,也就是网络序，
    # I表示4字节无符号整数
    print(struct.pack('>I', 10240099))
    # unpack把bytes变成相应的数据类型
    print(struct.unpack('>IH',b'\xf0\xf0\xf0\xf0\x80\x80'))
    # 根据>IH的说明，后面的bytes依次变为I：4字节无符号整数和H：2字节无符号整数
    # 所以，尽管Python不适合编写底层操作字节流的代码，但对性能要求不高的地方，利用struct方便多了


def main():
    my_test()

if __name__ == '__main__':
    main()
