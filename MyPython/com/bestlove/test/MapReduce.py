# -*- coding: utf-8 -*-
# Python 内建了map() 和 reduce()函数
# map()函数接受两个参数，一个是函数，一个是Iterable，map将传入的参数依次作用到序列的每个元素，并把结果作为Iterator返回
from functools import reduce
import time
def f(x):
    return x*x

def test_map():
    r = map(f,[1,2,3,4,5,6,7]) # map()传入的第一个参数是f,即函数对象本身
    print(list(r)) # 由于结果r是一个Iterator，Iterator是惰性数列，因此通过list()函数让它把整个序列都计算出来并返回一个list
    s = map(str,[1,3,4,56,7,8,89])
    print(list(s))

def add(x,y):
    return x+y

def fn(x,y):
    return x*10+y


# 配合map()，我们就可以写出把str转换成int的函数
def char2num(s):
    return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]

def test_reduce():
    r = reduce(add,[1,2,3,4,5,6])
    print(r) # 序列求和 r不是Iterator
    n = reduce(fn,[1,3,5,7])
    print(n)
    m = reduce(fn,map(char2num,'13579'))
    print(m)

# 整理成一个str2int的函数就是
def str2int(s):
    def fn(x,y):
        return x*10+y
    def char2num(s):
        return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
    return reduce(fn,map(char2num,s))

# 还可以用lambda函数进一步简化
def str2int2(s):
    # lambda函数的用法在后面介绍
    return reduce(lambda x,y:x*10+y,map(char2num,s))

# 转换人名
def normalize(name):
    return name[0].upper()+name[1:].lower()
# 求list中元素之乘积
def prod(L):
    def product(x,y):
        return x*y
    return reduce(product,L)
# 字符串转浮点数，pow()是个知识点，求n次方的？
def str2float(s):
    s1,s2 = s.split('.')
    return reduce(lambda x,y:x*10+y,map(char2num,s1))+(reduce(lambda x,y:x*10+y,map(char2num,s2)))/pow(10,len(s2))


def my_test():
    test_map()
    test_reduce()
    print(str2int('192348'))
    print(str2int2('9829384')) #如果Python没有提供int()函数，我们完全可以自己写一个把字符串转化为整数的函数，而且只需几行代码
    L1 = ['ahshYjs','JSJEWUE','AjskdU']
    L2 = list(map(normalize,L1))
    print(L2)
    print('3*5*7*9 =',prod([3,5,7,9]))
    print(str2float('18383.450384'))
    print(time.time())


def main():
    my_test()

if __name__ == '__main__':
    main()