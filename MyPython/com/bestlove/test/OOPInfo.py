# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# Get OOP Infomation 获取对象信息 新年新气象

import types

'''
    实例属性和类属性
'''

# 由于Python是动态语言，根据类创建的实例可以任意绑定属性
# 给实例绑定属性的方法是通过实例变量，或者通过self变量

class Student(object):
    def __init__(self,name):
        self.name = name

# 但是，如果Student类本身需要绑定一个属性呢？可以直接在class中定义属性，
# 这种属性是类属性归Student类所有

class Student2(object):
    name = '柳如是'





def my_test2():
    s = Student('李婉儿')
    s.score = 90
    print(s.name, s.score)
    s2 = Student2()
    print(s2.name)  # 这个属性虽然归lei所有，但类的所有实例都可以访问到
    print(Student2.name)
    s2.name = '李香君'  # 给实例绑定name属性
    print(s2.name)  # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
    print(Student2.name)  # 但是类属性并未消失，用Student2.name任然可以访问
    del s2.name  # 如果删除实例的name属性
    print(s2.name)  # 再次调用s2.name，由于实例的name属性没有找到，类的name属性就会显示出来


'''
    从上面的例子可以看出，在编写程序的时候，实例属性和类属性千万不能使用相同的名称，
    相同的名称的实例属性将会屏蔽掉类属性，但是当你删除实例属性后，在使用相同的名称，
    访问到的将是类属性。
'''







# 获取对象类型
def getOOPInfo(temp):
    t = type(temp)  # type()函数返回的是Class类型，可以通过if判断
    print(t)


class Animal(object):
    def getInfo(self):
        print('I\'m an Animal')


class Dog(Animal):
    def getInfo(self):
        print('I\'m a Dog')

# 如果也想用len(myObject)的话，就自己写一个__len__()方法
class MyDog(Animal):
    def __len__(self):
        return 100
    # 配合getattr()、setattr()和hasattr()，我们可以直接操作一个对象的状态
    def __init__(self):
        self.x = 193
    def power(self):
        return self.x * self.x


def flag(a,b):
    if type(a)==type(b):
        print('两个是同一个类型')
    else:
        print('不同的两个类型')


# 对于class的继承关系来说，使用type()就很不方便，我们要判断class的类型，可以使用isinstance()函数
def getResult(a,b):
    return isinstance(a, b)


# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list
def getAttribute(a):
    print(dir(a))


'''
    通过内置的一系列函数，我们可以对任意一个Python对象进行剖析，拿到其内部的数据
    要注意的是，只有在不知道对象信息的时候，我们才会去获取对象信息，使用getattr()方法

    假设我们希望从文件流fp中读取图像，我们首先要判断该fp对象是否存在read方法，
    如果存在，则该对象是一个流，如果不存在，则无法读取。hasattr()就派上用场了。

    请注意，在Python这类动态语言中，根据鸭子类型，有read()方法，不代表该fp对象就是一个文件流，
    它也可能是网络流，也可能是内存中的一个字节流，但只要read()方法返回的是有效的图像数据，
    就不影响读取图像的功能
'''


def readImage(fp):
    if hasattr(fp, 'read'):
        return readImage(fp)
    return None


def my_test():
    getOOPInfo(123)
    getOOPInfo('Hello World')
    getOOPInfo(None)
    getOOPInfo([1, 3, 4, '张三丰', 69, '太极专家'])
    getOOPInfo((3.34, 4, 232,'王生辰', [1, 3, 4, '张三丰', 69, '太极专家']))
    getOOPInfo({'姓名': '李元霸', '性别': '男', '年龄': 58, '爱好': ['睡觉', '吃饭', '游戏']})
    getOOPInfo(abs)
    a = Animal()
    getOOPInfo(a)
    dog = Dog()
    getOOPInfo(dog)
    flag(a,dog)
    flag(123, 456)
    flag('Hello', 'World')
    flag([1, 3, 4, '张三丰', 69, '太极专家'], ['Java', 'Python', 20, 21])
    flag((3.34, 4, 232,'王生辰', [1, 3, 4, '张三丰', 69, '太极专家']), {'姓名': '李元霸', '性别': '男', '年龄': 58, '爱好': ['睡觉', '吃饭', '游戏']})
    # 如果要判断一个对象是否是函数，可以使用types模块中定义的常量
    print(type(flag) == types.FunctionType) # 函数
    print(type(abs) == types.BuiltinFunctionType) # 构造函数
    print(type(lambda x: x)==types.LambdaType) # lambda表达式
    print(type((x for x in range(10)))==types.GeneratorType) # 生成器
    m1 = getResult(dog, Animal)
    print(m1)
    m2 = getResult(dog, Dog)
    print(m2)
    print('两个比较：',m1 and m2)
    # type()判断的基本类型也可以用isinstance()来判断
    print(getResult(123,int))
    print(getResult(b'a',bytes))
    # 并且还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple
    print(getResult([1, 3, 4, '春节要到了'], (list, tuple)))
    print(getResult((3, 4, '马上要回家了'), (list, tuple)))
    # str对象下的所有属性和方法
    getAttribute(str) # 返回一个包含字符串的list

    '''
        类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。
        在Python中，如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，
        它自动去调用该对象的__len__()方法，所以len('ABCDE') 和'ABCDE'.__len__()是等价的
    '''
    print(len('ABCDE'))
    print('ABCDE'.__len__())
    dog2 = MyDog()
    print(len(dog2))
    # 普通的属性方法
    print('ABCDE'.lower())
    print(hasattr(dog2, 'x'))
    print(dog2.x)
    print(hasattr(dog2, 'y'))
    setattr(dog2, 'y', 298)  # 添加一个属性吧
    print(hasattr(dog2, 'y'))
    print(getattr(dog2, 'y'))
    # 等同于
    print(dog2.y)
    # 如果试图获取不存在的属性，get时会抛出AttributeError的错误
    # print(getattr(dog2, 'z'))
    # 可以设置一个默认参数，如果属性不存在，就返回默认值
    print(getattr(dog2, 'z', 404))
    # 也可以获取对象的方法
    print(hasattr(dog2, 'power'))
    print(getattr(dog2, 'power'))
    # 获取属性power 并赋值到变量fn
    fn = getattr(dog2, 'power')
    # 调用
    print(fn())



def main():
    my_test()
    my_test2()


if __name__ == '__main__':
    main()
