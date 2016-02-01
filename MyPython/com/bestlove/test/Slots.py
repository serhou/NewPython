# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# 使用__slots__ 属性

from types import MethodType


class Student(object):
    pass


def set_age(self,age):  # 定义一个函数作为实例方法
    self.age = age


def set_score(self,score):
    self.score = score


class Student2(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称


# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
class GraduateStudent(Student2):
    pass


class OldStudent(Student2):
    __slots__ = ('sex', 'address')


def my_test4():
    os = OldStudent()
    os.name = '柳如是'
    os.age = 22
    os.sex = '女'
    os.address = '秦淮河'
    print(os.name, os.age, os.sex, os.address)


def my_test3():
    g = GraduateStudent()
    g.score = 182  # 除非在子类中也定义__slots__，这样，子类实例运行定义的属性就是自身的__slots__加上父类的__slots__
    print(g.score)


def my_test2():
    s = Student2()
    s.name = '李元霸'
    s.age = 26
    # s.score = 99  # AttributeError: 'Student2' object has no attribute 'score'


def my_test():
    s = Student()
    s.name = '张三丰'  # 动态给实例绑定一个属性
    print(s.name)
    # 给实例绑定一个方法
    s.set_age = MethodType(set_age,s)
    s.set_age(18)  # 调用实例方法
    print(s.age)  # 测试结果
    # 但是，给一个实例绑定的方法，对另一个实例是不起作用的
    s2 = Student()  # 创建新的实例
    # s2.set_age(22)  # 调用方法后 AttributeError: 'Student' object has no attribute 'set_age'
    # 为了给所有实例都绑定方法，可以给class绑定方法
    Student.set_score = MethodType(set_score,Student)
    # 给class绑定方法后，所有实例均可调用
    s.set_score(172)
    print(s.score)
    s2.set_score(57)
    print(s2.score)
    print(s.score, s2.score)  # 这么设置会覆盖s实例原本已设置的分数


def main():
    my_test()
    my_test2()
    my_test3()
    my_test4()



if __name__ == '__main__':
    main()