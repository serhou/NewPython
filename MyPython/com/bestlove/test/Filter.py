# -*- coding:utf-8 -*-
# Python内建的filter()函数用于过滤序列
'''
    和map()类似，filter()也接收一个函数和一个序列。
    和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
'''

# 在一个list中，删掉偶数，只保留奇数
def is_odd(n):
    return n%2==1

# 把一个序列中的空字符串删掉，可以这个写
def not_empty(s):
    return s and s.strip()

# 用Filter求素数
'''
    计算素数的一个方式是艾氏筛法，它的算法理解起来非常简单：
    首先，列出从2开始的所有自然数，构造一个序列：
    2,3,4,5,6,7,8,9,10,11.....
    取序列的第一个数2,它一定是素数，然后用2把序列的2的倍数筛掉
    3,5,7,9,11,13,15,17....
    去序列的第一个数3,它一定是素数，然后用3把序列的3的倍数筛掉：
    5,7,11,13,17.....
    取序列的第一个数5，然后用5把序列的5的倍数筛掉：
    7,11,13,17....
    不断筛选下去，就可以得到所有的素数。
'''

# 用Python来实现这个算法，可以先构造一个从3开始的奇数序列：
def _odd_iter():
    n = 1
    while True:
        n = n+2
        yield n # 注意这是一个生成器，并且是一个无限序列
# 然后定义一个筛选函数：
def _not_divisible(n):
    return lambda x:x%n>0
# 最后定义一个生成器，不断返回下一个素数：
def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n),it) # 构造新序列

# 回数
def is_palindrome(n):
    n = str(n)
    return n == n[::-1]


def my_test():
    # 保留奇数
    L = list(filter(is_odd,[1,2,3,4,5,6,7,8,9,10]))
    print(L)
    # 删除序列中的空字符串
    L2 = list(filter(not_empty,['a',None,'b','',' ','c','','d','e']))
    print(L2)
    # 打印1000以内的素数
    for n in primes():
        if n < 1000:
            print(n)
        else:
            break
    # 回数
    output = filter(is_palindrome,range(1,1000))
    print(list(output))

def main():
    my_test()

if __name__ == '__main__':
    main()