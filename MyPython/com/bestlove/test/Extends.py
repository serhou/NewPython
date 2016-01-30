# -*- coding: utf-8 -*-

# 继承和多态 还缺了个多态


# 先定义一个父类
class Animal(object):
    def run(self):
        print("Animal is running......")


# 定义子类
class Dog(Animal):
    pass


# 再定义一个子类
class Cat(Animal):
    pass


# 给子类增加一些方法
class Pig(Animal):
    def run(self):
        print("Pig is running......")

    def eat(self):
        print("Pig love eat......")


# 再给子类增加一些方法
class Mouse(Animal):
    def run(self):
        print("Mouse is running......")

    def rice(self):
        print("Mouse love rice......")


# 要理解多态的好处，我们还需要再编写一个函数，这个函数接受一个Animal类型的变量
def run_twice(animal):
    animal.run()  # 只要有run方法的对象都可以传入到这个方法，这和java不同


# 再添加一个实例Tortoise
class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly......')


def my_test():
    animal = Animal()
    animal.run()  # 这是父类
    dog = Dog()  # 创建对象
    dog.run()  # 继承自父类的方法
    cat = Cat()  # 创建对象
    cat.run()  # 继承自父类的方法
    pig = Pig()  # 创建对象
    pig.run()  # 重写了父类的方法
    pig.eat()  # 定义了属于自己独有的方法
    mouse = Mouse()  # 创建对象
    mouse.run()  # 重写了父类的方法
    mouse.rice()  # 定义了属于自己独有的方法
    # 判断对象是否是某个类型
    print(isinstance(dog, Dog), isinstance(cat, Animal), isinstance(animal, Mouse), isinstance(pig, Dog))
    # Animal实例传入
    run_twice(Animal())
    # Dog
    run_twice(Dog())
    # Cat
    run_twice(Cat())
    # Pig
    run_twice(Pig())
    # Mouse
    run_twice(Mouse())
    # Tortoise
    run_twice(Tortoise())  # 新增一个Animal子类，不必对run_twice()做任何修改，这就是多态

'''
    多态的真正威力：调用方只管调用，不管细节，而当我们新增一种Animal的子类时，只要确保run()方法编写正确，
    不管原来的代码是如何调用的，这就是著名的“开闭”原则：
    对扩展开放：允许新增Animal子类；
    对修改封闭：不需要修改依赖Animal类型的run_twice()等函数
    继承也可以多级继承，最后可以追溯到跟类object

    对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了
    这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，它就可以被
    看做是鸭子。

    Python的“file-like object”就是一种鸭子类型。对真正的文件对象，它有一个read()方法，返回其内容。但是，许多对象，
    只要有read()方法，都被视为“file-like object”。许多函数接收的参数就是“file-like object”，你不一定要传入真正的
    文件对象，完全可以传入任何实现了read()方法的对象。
'''


def main():
    my_test()


if __name__ == '__main__':
    main()
