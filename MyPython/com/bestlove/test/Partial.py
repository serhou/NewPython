# -*- coding: utf-8 -*-

# 偏函数
import functools
'''
    Python的functools模块提供了很多有用的功能，其中一个就是偏函数(Partial function)。
    要注意，这里的偏函数和数学意义上的偏函数不一样
'''
# int() 函数可以把字符串转换为整数，当仅传入字符串时，int()函数默认按十进制转换
# 但int()函数还提供额外的base参数，默认值为10.如果传入base参数，就可以做N进制的转换
# base=10默认，且必须 36 >= base >= 2
def char_other(s,base=2):
    i = int(s,base) # 是字符串10，表示2进制，然后转换为10进制表示2
    print(i)

# functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2
int2 = functools.partial(int,base=2)

'''
    所以，简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是默认值），
    返回一个新的函数，调用这个新函数会更简单
    注意到上面的新的int2函数，仅仅是把base参数重新设定默认值为2，但也可以再函数调用时传入其他值

    最后，创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数
    当传入int2 = functools.partial(int,base=2)
    实际上固定了int()函数的关键字参数base，也就是int2('10001')
    相当于：
    kw = {'base':2}
    int('100010',**kw)

'''
kw = {'base':8}

# 当传入
max2 = functools.partial(max,10)
'''
    实际上会把10作为*args的一部分自动加到左边
    想当于：
    args = (10,3,5,6)
    max2(*args)
'''
def my_test():
    char_other('10',2)
    print(int2('110101')) # 53
    print(int2('0x12d2e',base=16)) # 16进制转换为十进制：77102
    print(int2('153627',**kw)) # 8进制：55191
    print(max2(3,5,6)) # 10
'''
    小结
    当函数的参数个数太多，需要简化时，使用functools.pratial可以创建一个新的函数，
    这个新函数可以固定住原函数的部分参数，从而在调用时更简单。
'''



def main():
    my_test()


if __name__ == '__main__':
    main()