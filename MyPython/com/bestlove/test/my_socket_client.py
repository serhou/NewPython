# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

def my_test():
    # 创建socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 建立连接
    s.connect(('127.0.0.1', 9999))
    # 接收欢迎消息
    print(s.recv(1024).decode('utf-8'))
    for data in [b'sanfeng', b'yuanba', b'rushi']:
        # 发送数据
        s.send(data)
        print(s.recv(1024).decode('utf-8'))
    s.send(b'exit')
    s.close()



def main():
    my_test()


if __name__ == '__main__':
    main()