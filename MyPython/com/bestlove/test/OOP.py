# -*- coding: utf-8 -*-

# 面向对象 类 方法  属性

class Student(object):
    def __init__(self,name,score):
        self.name =name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name,self.score))


def my_test():
    zhang = Student('张三丰',99)
    li = Student('李元霸',86)
    liu = Student('柳如是',95)
    zhang.print_score()
    li.print_score()
    liu.print_score()


def main():
    my_test()

if __name__ == '__main__':
    main()