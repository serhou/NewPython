# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio
import threading


@asyncio.coroutine
def hello():
    print('Hello World! (%s)' % threading.currentThread())
    # 异步调用asyncio.sleep(1)
    r = yield from asyncio.sleep(1)
    print('Hello again! (%s)' % threading.currentThread())


def my_test():
    # 获取EventLoop
    loop = asyncio.get_event_loop()
    # 执行coroutine
    # loop.run_until_complete(hello())
    tasks = [hello(), hello()]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()


def main():
    my_test()


if __name__ == '__main__':
    main()