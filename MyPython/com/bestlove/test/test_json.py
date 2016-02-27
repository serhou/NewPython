# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

'''

    JSON表示的对象就是标准的JavaScript语言的对象，JSON和Python内置的数据类型对应如下：

    JSON类型	     Python类型
        {}	        dict
        []	        list
    "string"	    str
    1234.56	      int或float
    true/false	  True/False
        null	    None

    Python 内置的json模块提供了非常完善的Python对象到json对象格式的转换

'''


#  Python的dict对象可以直接序列化为json的{},不过，很多时候，我们更喜欢用Class来表示对象
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


# student对象转换为dict
def student2dict(stu):
    return {
        'name': stu.name,
        'age': stu.age,
        'score': stu.score
    }


# dict转换为student对象
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])


def my_test():
    d = dict(name='柳如是', age=24, score=89)
    # json.dumps()方法返回一个str，内容就是标准的json，类似的，dump()方法可以直接把json写一个file-like Object
    j = json.dumps(d)
    print(j)
    # 要把json反序列化为Python对象，用loads()或者对应的load()方法，前者把json的字符串反序列化，
    # 后者从file-like Object中读取字符串并反序列化
    json_obj = json.loads(j)
    print(json_obj)  # 由于json标准规定json编码utf-8，所以我们总是能正确地在Python的str与json的字符串之间转换
    # Student直接转json会出错
    s = Student('李元霸', 45, 88)
    # print(json.dumps(s))  # TypeError: <__main__.Student object at 0x000000B2FCB62400> is not JSON serializable
    # 需要先把Student的实例转换为dict，然后再被序列化为json对象
    j2 = json.dumps(s, default=student2dict)
    print(j2)
    # 还有一个偷懒的写法
    print(json.dumps(s, default=lambda obj: obj.__dict__))
    # 反序列化
    json_obj2 = json.loads(j2, object_hook=dict2student)
    print(json_obj2)  # 已转换为对象
    print(json_obj2.name, json_obj2.age, json_obj2.score)  # 可以取出对象中的属性


def main():
    my_test()


if __name__ == '__main__':
    main()