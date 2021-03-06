# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio


async def wget(host):
    print('wget %s...' % host)
    connect  = asyncio.open_connection(host, 80)
    reader, writer = await connect
    header = 'GET / HTTP/1.1\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    await writer.drain()
    while True:
        line = await reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()


def my_test():
    loop = asyncio.get_event_loop()
    tasks = [wget(host) for host in ['www.sina.com.cn', 'www.qq.com', 'www.163.com']]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

    '''
        执行结果如下：
        wget www.qq.com...
        wget www.sina.com.cn...
        wget www.163.com...
        www.163.com header > HTTP/1.0 302 Moved Temporarily
        www.163.com header > Server: Cdn Cache Server V2.0
        www.163.com header > Date: Sat, 26 Mar 2016 07:52:10 GMT
        www.163.com header > Content-Length: 0
        www.163.com header > Location: http://www.163.com/special/0077jt/error_isp.html
        www.qq.com header > HTTP/1.1 200 OK
        www.qq.com header > Server: squid/3.4.3
        www.qq.com header > Date: Sat, 26 Mar 2016 07:52:18 GMT
        www.qq.com header > Content-Type: text/html; charset=GB2312
        www.qq.com header > Transfer-Encoding: chunked
        www.qq.com header > Connection: keep-alive
        www.qq.com header > Vary: Accept-Encoding
        www.qq.com header > Vary: Accept-Encoding
        www.qq.com header > Expires: Sat, 26 Mar 2016 07:53:18 GMT
        www.qq.com header > Cache-Control: max-age=60
        www.qq.com header > Vary: Accept-Encoding
        www.qq.com header > Vary: Accept-Encoding
        www.qq.com header > X-Cache: HIT from tianjin.qq.com
        www.sina.com.cn header > HTTP/1.1 200 OK
        www.sina.com.cn header > Content-Type: text/html
        www.sina.com.cn header > Vary: Accept-Encoding
        www.sina.com.cn header > X-Powered-By: schi_v1.02
        www.sina.com.cn header > Server: nginx
        www.sina.com.cn header > Date: Sat, 26 Mar 2016 07:51:57 GMT
        www.sina.com.cn header > Last-Modified: Sat, 26 Mar 2016 07:48:36 GMT
        www.sina.com.cn header > Expires: Sat, 26 Mar 2016 07:52:57 GMT
        www.sina.com.cn header > Cache-Control: max-age=60
        www.sina.com.cn header > Age: 36
        www.sina.com.cn header > Content-Length: 546408
        www.sina.com.cn header > X-Cache: HIT from ja180-188.sina.com.cn
    '''


def main():
    my_test()


if __name__ == '__main__':
    main()