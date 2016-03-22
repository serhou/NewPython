# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import threading

import time


def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8')=='exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)



def my_test():
    # 创建socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定监听体制和端口  小于1024的端口号必须要有管理员权限才能绑定
    s.bind(('127.0.0.1', 9999))  # 我们写的这个服务不是标准服务，所以用9999这个端口号，以免冲突
    # 调用listen()方法开始监听端口
    s.listen(5)  # 传入的参数指定等待连接的最大数量
    print('Waiting for connection...')
    # 服务器程序通过一个永久循环来接受来自客户端的连接,accept()会等待并返回一个客户端连接
    while True:
        # 接受一个新连接
        sock, addr = s.accept()
        # 创建新线程来处理TCP连接
        t = threading.Thread(target=tcplink, args=(sock, addr))
        t.start()

def main():
    my_test()


if __name__ == '__main__':
    main()