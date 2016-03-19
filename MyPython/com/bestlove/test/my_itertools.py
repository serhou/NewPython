# !/usr/bin/env python3
# -*- coding:utf-8 -*-

import itertools
import time

'''
    Python的内置模块itertools提供了非常有用的用于操作迭代对象的函数
    itertools模块提供的全部是处理迭代功能的函数，它们的返回值不是list,
    而是Iterator，只有用for循环迭代的时候才真正计算。
'''


def test_iter_fun():
    # chain()可以把一组迭代对象串联起来，形成一个更大的迭代器
    for c in itertools.chain('ABC', 'MNSD'):
        print(c)
    # groupby()把迭代器中相邻的重复元素挑出来放在一起
    for key, group in itertools.groupby('AAABBCCDFGGGHIGGJKKJJ'):
        print(key, list(group))
    # 实际上挑选规则是通过函数完成的，只要作用于函数的两个元素返回值相等，
    # 这两个元素就被认为是在一组的，而函数返回值最为组的key。
    # 如果我们要忽略大小写分组，就可以让元素'A'和'a'都返回相同的key
    for key, group in itertools.groupby('AAaaAaBbbbBBBBbcCCCcc', lambda c : c.upper()):
        print(key, list(group))



def test_takewhile():
    natuals = itertools.count(1)
    ns = itertools.takewhile(lambda x: x <= 10, natuals)
    print(list(ns))


def test_repeat():
    re = itertools.repeat('ABC', 6)
    for r in re:
        print(r)  # repeat()负责把一个元素无限重复下去，
        # 不过如果提供第二个参数就可以限定重复次数
    '''
        无限序列只有在for迭代时才会无限地迭代下去，如果只是创建了一个迭代
        对象，它不会事先把无限个元素生成出来，事实上也不可能在内存中创建
        无限多个元素。
    '''


def test_cycle():
    cs = itertools.cycle('ABCDEF')  # 注意字符串也是序列的一种
    for c in cs:
        print(c)  # cycle()会把传入的一个序列无限重负下去


def test_count():
    natuals = itertools.count(1)
    for n in natuals:
        time.sleep(0.1)
        print(n)  # count()会创建一个无限迭代器，所以上述代码会打印出自然数序列，
        # 根本停不下来，只能Ctrl+C退出。为了看清我们使用sleep()函数来使程序放慢脚步


def my_test():
    # test_count()
    # test_cycle()
    test_repeat()
    test_takewhile()
    test_iter_fun()


def main():
    my_test()


if __name__ == '__main__':
    main()
