# !/usr/bin/env python3
# -*- coding: utf-8 -*-


# @property

'''
    在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，
    但是，没办法检查参数，导致可以把成绩随便改
    s = Student()
    s.score = 999

    这显然不合逻辑。为了限制score的范围，可以通过一个set_score()方法来设置成绩，
    再通过一个get_score()来获取成绩，这样，在set_score()方法里，就可以检查参数
'''


class Student(object):
    # 类似java中的get方法
    def get_score(self):
        return self._score
    # 类似java中的set方法
    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 and 100')
        self._score = value

'''
    但是，上面的调用方法略显复杂，没有直接用属性这么直接简单
    但，Python内置的@property装饰器就是负责把一个方法变成属性调用的
'''


class Student2(object):

    @property
    def score(self):  # 类似java中的注解
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 and 100')
        self._score = value



    '''
        @property的实现比较复杂，我们先来看看如何使用。把一个getter方法变成属性，
        只需要加上@property就可以了，此时，@preperty本身又创建了另一个装饰器@score.setter,
        负责把一个setter方法变成属性赋值，于是我们就拥有了一个可控的属性操作。

        注意到@property，我们在对实例属性操作的时候，就知道该属性很可能不是直接暴露的，
        而是通过getter和setter方法来实现的
    '''

# 还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性

class Student3(object):

    @property
    def birth(self):  # 有getter和setter方法，所以可以读写
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):  # 这是一个只读属性，因为没有setter方法啊，无法赋值
        return 2016 - self._birth


class Screen(object):

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value
        
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height


def my_test4():
    s = Screen()
    s.width = 24
    s.height = 16
    print(s.resolution)
    assert s.resolution == 384, '24 * 16 = %d ?' % s.resolution



def my_test3():
    s = Student3()
    s.birth = 1993
    print(s.age)
    print(s.birth)


def  my_test2():
    s = Student2()
    s.score = 99
    print(s.score)
    # s.score = 101  # ValueError: score must between 0 and 100





def my_test():
    s = Student()
    s.set_score(79)
    print(s.get_score())
    # s.set_score(999)  #  raise ValueError('score must between 0 and 100')
    # print(s.get_score())  # ValueError: score must between 0 and 100



def main():
    my_test()
    my_test2()
    my_test3()
    my_test4()


if __name__ == '__main__':
    main()