# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket


def my_test():
    # 创建socket  OCK_DGRAM指定了这个Socket的类型是UDP
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定端口
    s.bind(('127.0.0.1', 9999))
    print('Bind UDP on 9999...')
    while True:
        # 接收数据 recvfrom()方法返回数据和客户端的地址与端口
        data, addr = s.recvfrom(1024)
        print('Received from %s:%s.' % addr)
        # 服务器收到数据后，直接调用sendto()就可以把数据用UDP发给客户端
        s.sendto(b'Hello, %s!' % data, addr)


def main():
    my_test()


if __name__ == '__main__':
    main()