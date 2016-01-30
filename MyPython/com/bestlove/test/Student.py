# -*- coding: utf-8 -*-

# 面向对象   类是抽象的模板   类Class和实例Instance

# (object)表示该类从哪个类继承下来，通常没有合适的继承类，就使用object类，这是所有类最终都会继承的类
class Student(object):
    # 我们可以再创建实例的时候，把一些我们认为必须绑定的属性强制填写进入，通过定义一个__int__方法
    def __init__(self,name,score,gender): # __init__方法的第一个参数永远是self，表示创建的实例本身，
        self.name = name # 因此__init__方法内部就可以把各种属性绑定到self，因为self就指向创建的实例本身
        self.score =score # 有了__init__方法，在创建实例的时候，就不能传入空参数了，必须传入与__init__方法匹配的参数
        self.gender =gender # 但是self不需要传，Python解释器自己会把实例变量传进去
    # 这些封装数据的函数是和Student类本身是关联起来的，我们称之为方法
    def print_stu(self):
        print('%s得了%s分，是个%s人！' %(self.name,self.score,self.gender))
    # 封装的另一个好处是可以给Student类增加新的方法
    def get_grade(self):
        if self.score >=90:
            return 'A'
        elif self.score >=60:
            return 'B'
        else:
            return 'C'



# 创建实例是通过类名+()实现的
def my_test():
    # bart = Student()
    # print(bart) # <__main__.Student object at 0x000000D400BA80B8>
    # print(Student) # <class '__main__.Student'>
    # 可以自由地给一个实例变量绑定属性，比如，给实例绑定一个name属性
    # bart.name='张三丰'
    # print(bart.name) # 我感觉这个有点扯，这个和赋值给一个变量有什么区别
    bart2 = Student('柳如是',98,'女')
    print(bart2.name,bart2.score,bart2.gender)
    print('%s得了%s分，是个%s人！' % (bart2.name,bart2.score,bart2.gender))
    bart3 = Student('李元霸',89,'男')
    bart3.print_stu() # 直接定义方法即可
    print(bart2.get_grade())
    print(bart3.get_grade())

def main():
    my_test()


if __name__ == '__main__':
    main()