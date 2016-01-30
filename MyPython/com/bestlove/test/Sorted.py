# -*- coding: utf-8 -*-

# 排序算法

# Python内置的sorted()函数就可以对list进行排序
def list_test():
    L = [23,45,6,77,32,5,11,-3,4,-84,-33]
    L2 = sorted(L)
    print(L2)
    L3 = sorted(L,reverse=True)
    print(L3)

# 此外，sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：
# key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序。
def abs_test():
    L = [3,5,3,22,4,-2,4,53,-98,1]
    L2 = sorted(L,key=abs)
    print(L2)
    L3 = sorted(L,key=abs,reverse=True)
    print(L3)

# 对字符串进行排序
def str_test():
    str1 = ['asd','msj','uwh','saw','eww','lsk','Zjs','S']
    str2 = sorted(str1)
    print(str2) # 默认情况下，对字符串排序，是按照ASCII的大小比较的，由于'Z'<'a'，所以大写排在前面
    str3 = sorted(str1,key=str.lower)
    print(str3)
    # 要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True
    str4 = sorted(str1,key=str.lower,reverse=True)
    print(str4)

# 练习：假设我们用一组tuple表示学生名字和成绩，请用sorted()对列表分别按名字排序

def by_name(t):
    return t[0].lower()
def by_score(t):
    return t[1]


def my_test():
    list_test()
    abs_test()
    str_test()
    L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
    L2 = sorted(L,key=by_name)
    print(L2)
    L3 = sorted(L,key=by_score,reverse=True)
    print(L3)

def main():
    my_test()

if __name__ == '__main__':
    main()