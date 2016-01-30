# -*- coding: utf-8 -*-


# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，
# 在Python中，实例的变量名如果以__开头，就变成了一个私有变量(private),
# 只有内部可以访问，外部不能访问

class Student(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score = score
    # 添加get方法供外部访问
    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score
    # 添加set方法供外部代码修改属性值
    def set_name(self,name):
        self.__name = name
    def set_score(self,score):
        if 0<= score <= 100:
            self.__score = score
        else:
            raise ValueError('你的分数超过了界线')

'''
    需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，
    是特殊变量，特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名

    有些时候，你会看到一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，
    但是按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”

    双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是，不能直接访问__name是因为Python解释器对外把
    __name变量改成了_Student__name，所以仍然可以通过_Student__name来访问__name变量

    但是，强烈建议你不要这么干，因为不同版本的Python解释器可能会把__name改成不同的变量名，
    总的来说就是，Python本身没有任何机制阻止你干坏事，一切全靠自觉。

'''



def print_info(self):
    print('学生%s,得分%s。' % (self.__name,self.__score))





def my_test():
    stu = Student('李婉儿',99)
    stu.print_info()
    name = stu.get_name()
    print('我的叫%s' % name)
    score = stu.get_score()
    print('我得了%s分' % score)

    stu.set_name('修文殊')
    stu.set_score(78)
    print(stu.get_name(),stu.get_score())




def main():
    my_test()


if __name__ == '__main__':
    main()