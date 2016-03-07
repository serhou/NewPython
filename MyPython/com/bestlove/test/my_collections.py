# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import namedtuple, deque, defaultdict, OrderedDict, Counter

# 集合 collections


def my_test5():
    # Counter是一个简单的计数器
    c = Counter()  # Counter实际上也是dict的一个子类
    for ch in 'programming':
        c[ch] = c[ch] + 1
    print(c)


# OrderedDict可以实现一个FIFO(先进先出)的dict，当容量超出限制时，先删除最早添加的Key

class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add', (key, value))
        OrderedDict.__setitem__(self, key, value)


def my_test4():
    d = dict([('a', 1), ('b', 2), ('c', 3)])  # key是无序的
    print(d)
    od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])  # key是有序的
    print(od)
    odd = OrderedDict()
    odd['z'] = 1
    odd['y'] = 2
    odd['x'] = 3
    print(list(odd.keys()))  # 按照插入的key的顺序返回，而不是key本身排序


def my_test3():
    dd = defaultdict(lambda : 'N/A')  # 注意默认值是调用函数返回的，而函数在创建defaultdict对象时传入
    dd['key1'] = 'abc'
    print(dd['key1'])
    print(dd['key2'])  # 除了在key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样。


def my_test2():
    q = deque(['a', 'b', 'c'])
    q.append('x')
    q.appendleft('y')
    print(q)
    q.pop()
    q.popleft()
    print(q)


def my_test():
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(1, 2)
    print(p.x)
    print(p.y)
    print(isinstance(p, Point))
    print(isinstance(p, tuple))
    # namedtuple('名称', [属性list])
    Circle = namedtuple('Circle', ['x', 'y', 'z'])


def main():
    my_test()
    my_test2()
    my_test3()
    my_test4()
    my_test5()


if __name__ == '__main__':
    main()