# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# 协程 Coroutine

'''
    注意到consumer函数是一个generator，把一个consumer传入produce后：

    首先调用c.send(None)启动生成器；

    然后，一旦生产了东西，通过c.send(n)切换到consumer执行；

    consumer通过yield拿到消息，处理，又通过yield把结果传回；

    produce拿到consumer处理的结果，继续生产下一条消息；

    produce决定不生产了，通过c.close()关闭consumer，整个过程结束。

    整个流程无锁，由一个线程执行，produce和consumer协作完成任务，所以称为“协程”，而非线程的抢占式多任务。

    最后套用Donald Knuth的一句话总结协程的特点：

    “子程序就是协程的一种特例。”

    某个函数包含了yield，这意味着这个函数已经是一个Generator,yield是一个表达式(Expression)，通过send(msg)语句让它执行，
    并直到下一个yield表达式处，再次调用会接着上次的位置继续执行;
    send(msg)传递值msg给yield表达式并返回下一个yield表达式的参数,当第一次使用send(None)调用时，yield不执行，此时直接返回等待下一次send()调用；
    注意：第一次调用时，需使用send(None)语句，不能使用send发送一个非None的值，否则会出错的，因为没有yield语句来接收这个值。
'''

def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[Consumer] Consuming %s...' % n)
        r = '200 OK'


def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[Producer] Producing %s...' % n)
        r = c.send(n)
        print('[Producer] Consumer return: %s' % r)
    c.close()


def my_test():
    c = consumer()
    produce(c)


def main():
    my_test()


if __name__ == '__main__':
    main()