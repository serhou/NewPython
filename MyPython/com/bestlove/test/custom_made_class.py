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


# __getattr__


class Student2(object):

    def __init__(self):
        self.name = '张三丰'

    def __getattr__(self, item):
        if item == 'score':
            return 88

        if item == 'age':  # 返回函数
            return lambda: 23

        raise AttributeError('\'Student\' object has no attribute \'%s\'' % item)

        '''
            实际上可以把一个类的所有属性和方法调用全部动态化处理了，不需要任何特殊手段。
            而Java是静态类型的语言，所以用Java写的项目易于维护，而Python则不宜维护
        '''


# 利用完全动态的__getattr__,可以写出一个链式调用

class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


# __call__

'''
    一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用。
'''


class Student3(object):

    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)



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

    s = Student2()
    print(s.name)
    print(s.score)
    print(s.age())  # 函数调用
    # print(s.addr)  # 没有的属性会抛出异常
    print(Chain().status.user.timeline.list)
    s2 = Student3('柳如是')
    s2()  # self参数不要传入

    '''
    __call__()还可以定义参数。对实例进行直接调用就好比对一个函数进行调用一样，
    所以你完全可以把对象看出函数，把函数看成对象，因为这两者之间本来就没啥根本区别。

    如果你把对象看出函数，那么函数本身其实也可以再运行期动态创建出来，因为类的实例都是
    运行期创建出来的，这么一来，我们就模糊了对象和函数的界限。

    我们要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象，比如函数和我们
    上面定义的带有__call__()的实例
    '''
    # 通过callable()函数，我们就可以判断一个对象是否是“可调用”对象
    print(callable(Student3))
    print(callable(max))
    print(callable([1, 2, 4, 5]))
    print(callable(None))
    print(callable('str'))
    print(callable(str))




def main():
    my_test()


if __name__ == '__main__':
    main()
