# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# 多重继承
from socketserver import TCPServer, ForkingMixIn, UDPServer, ThreadingMixIn


class Animal(object):
    pass

# 大类
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

# 各种动物
class Dog(Mammal):
    pass

class Bat(Mammal):
    pass

class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass

# 给动物再加上Runnable和Flyable的功能，只需要先定义好Runnable和Flyable的类
class Runnable(object):
    def run(self):
        print('Running......')

class Flyable(object):
    def fly(self):
        print('Flying......')

# 对于需要Runnable功能的动物，就多继承一个Runnable
class Pig(Mammal, Runnable):
    pass

# 对于需要Flyable功能的动物，就多继承一个Flyable
class Eagle(Bird, Flyable):
    pass

class Dragon(Mammal, Flyable):
    pass


'''
    MixIn
    在设计类的继承关系时，通常，主线都是单一继承下来的，例如，Ostrich继承自Bird。
    但是，如果需要混入额外的功能，通过多重继承就可以实现，比如，让Ostrich除了
    继承自Bird外，再同时继承Runnable。这种设计通常称之为MixIn。

    为了更好地看出继承关系，我们把Runnable和Flyable改为RunnableMixIn和FlyableMixIn。
    类似的，你还可以定义出肉食动物CarnivorousMixIn和植食动物HerbivoresMixIn,让某个动物同时拥有好几个MixIn

'''

class RunnableMixIn(object):
    pass

class HerbivoresMixIn(object):
    pass

class Rabbit(Mammal, RunnableMixIn, HerbivoresMixIn):
    pass


'''
    Python自带的很多库也使用了MixIn。举个例子，Python自带了TCPServer
    和UDPServer这两类网络服务，而同时服务多个用户就必须使用多进程或多线程
    模型，这两种模型由ForkingMixIn和ThreadingMixIn提供。通过组合，我们
    可以创造出合适的服务来
'''

# 编写一个多进程模式的TCP服务
class MyTCPServer(TCPServer, ForkingMixIn):
    pass

# 编写一个多线程模式的UDP服务
class MyUDPServer(UDPServer, ThreadingMixIn):
    pass

# 也可以写一个更先进的协程模型，也可以编写一个CoroutineMixIn
class CoroutineMixIn(object):
    pass

class YourTCPServer(TCPServer, CoroutineMixIn):
    pass

'''
    这样一来，我们不需要复杂而庞大的继承链，只要选择组合不同的类的功能，
    就可以快速构造出所需的子类

    由于Python运行使用多重继承，因此，MixIn就是一种常见的设计。
    只允许单一继承的语言（如java）不能使用MixIn的设计。
    但是Java有class可以implements interface（实现接口）
'''

def my_test():
    pass


def main():
    my_test()


if __name__ == '__main__':
    main()