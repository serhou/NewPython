# !/usr/bin/env python3
# -*- coding: utf-8 -*-
from enum import Enum, unique

'''
    文件名my_enum.py不能写成与Python自己的模块enum.py同名，不然会报错。
'''

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)  # value属性则是自动赋给成员的int常量，默认从1开始计数


# 如果需要更精确地控制枚举类型，可以从Enum派生出自定义类
@unique  # @unique装饰器可以帮助我们检查保证没有重复值
class Weekday(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


def my_test():
    # 访问枚举类型有以下若干方法：
    day1 = Weekday.Mon
    print(day1)
    print(Weekday.Tue)
    print(Weekday['Wed'])
    print(Weekday.Sun.value)
    print(day1 == Weekday.Mon)
    print(day1 == Weekday.Fri)
    print(Weekday(6))
    print(day1 == Weekday(1))
    # print(Weekday(7))  # ValueError: 7 is not a valid Weekday
    for name, member in Weekday.__members__.items():
        print(name, '->', member, '=', member.value)  # 可见，既可以用成员名称引用枚举常量，又可以直接根据value的值获得枚举常量

    '''
        Enum 可以把一组相关常量定义在一个class中，且class不可变，而且成员可以直接比较
    '''

def main():
    my_test()

if __name__ == '__main__':
    main()