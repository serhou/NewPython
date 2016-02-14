#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# __str__

class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):  # 类似于Java的toString方法
        return 'Student object (name: %s)' % self.name

    __repr__ = __str__  # __str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的


# __iter__

'''
    如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，
    然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。
'''

# 以斐波那契数列为例，写一个Fib类


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a, b

    def __iter__(self):
        return self  # 实例本身就是迭代对象

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 10000:  # 退出循环的条件
            raise StopIteration()
        return self.a  # 返回下一个值

    # 还可以添加切片的判断
    def __getitem__(self, item):
        if isinstance(item, int):  # item是索引
            a, b = 1, 1
            for x in range(item):
                a, b = b, a + b
            return a
        if isinstance(item, slice):  # item是切片
            start = item.start
            stop = item.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


# __getitem__

'''
    Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list使用还是不行，比如取第6个元素Fib()[5]，
    会报错：TypeError: 'Fib' object does not support indexing
    要表现的像list那样按照下标取出元素，需要实现__getitem__()方法
'''


def my_test():
    print(Student('家教机'))
    s = Student('郑凯文')
    for n in Fib():
        print(n)
    print(Fib()[5])  # 第6个元素
    f = Fib()
    print(f[0:5])
    print(f[:10])
    # print(f[:10:4])  # 但是没有对step做参数处理默认为1

    '''
        也没有对负数作处理，所以，要正确实现一个__getitem__()还是有很多工作要做的
        此外，如果把对象看成dict，__getitem__()的参数也可能是一个作key的object，例如str
        与之对应的是__setitem__()方法，把对象试做list或dict来对集合赋值。
        最后，还有一个__delitem__()方法，用于删除某个元素
        总之，通过上面的方法，我们自己定义的类表现的和Python自带的list, tuple, dict没什么区别，
        这完全归功于动态语言的“鸭子类型”，不需要强制继承某个接口
    '''

def main():
    my_test()


if __name__ == '__main__':
    main()
