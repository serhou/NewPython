# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket


def my_test():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    for data in [b'zhenni', b'kangsitensi', b'feilipusi']:
        # 发送数据 不需要调用connect()，直接通过sendto()给服务器发数据
        s.sendto(data, ('127.0.0.1', 9999))
        # 接受数据
        print(s.recv(1024).decode('utf-8'))
    s.close()


def main():
    my_test()


if __name__ == '__main__':
    main()