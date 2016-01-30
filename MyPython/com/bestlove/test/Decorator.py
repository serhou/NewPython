# -*- coding: utf-8 -*-
# 装饰器 Decorator
import time

'''
    假设我们要加强now()函数的功能，
    比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义
    这种在代码运行期间动态增加功能的方式，称之为“装饰器”(Decorator)
    本质上，decorator就是一个返回函数的高阶函数
'''

def log(func):
    def wrapper(*args,**kw):
        print('call %s():' % func.__name__)
        return func(*args,**kw)
    return wrapper

# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂
def log2(text):
    def decorator(func):
        def wrapper(*args,**kw):
            print('%s %s():' % (text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator




@log
@log2('execute')
def now():
    print(time.time())

def my_test():
    f = now
    print(now.__name__)
    print(f.__name__)
    now()



def main():
    my_test()


if __name__ == '__main__':
    main()
