# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# 导入socket库
import socket

def test_socket():
    # 创建一个socket,AF_INET指定是要IPv4协议，SOCK_STREAM指定使用面向流的TCP协议
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 建立连接
    s.connect(('www.sina.com.cn', 80))
    s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
    # 接受数据
    buffer = []
    while True:
        # 每次最多接收1k字节
        d = s.recv(1024)
        if d:
            buffer.append(d)
        else:
            break
    data = b''.join(buffer)
    # 关闭连接
    s.close()
    # 分离数据
    header, html = data.split(b'\r\n\r\n', 1)
    print(header.decode('utf-8'))
    # 把接收的数据写入文件
    with open('sina.html', 'wb') as f:
        f.write(html)
    f.close()



def my_test():
    test_socket()



def main():
    my_test()


if __name__ == '__main__':
    main()