# -*- coding: utf-8 -*-
# 返回函数 函数作为返回值 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回

# 求和函数可以这样定义
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax

# 如果不需要立即求和，而是在后面的代码中再求，可以不返回求和结果，而是返回求和函数
def lazy_sum(*args):
    def pre_sum():
        ax = 0
        for n in args:
            ax += n
        return ax
    return pre_sum

# 在上面的这个例子中，我们在函数lazy_sum中定义了函数pre_sum，并且内部函数pre_sum可以引用外部函数lazy_sum的参数和局部变量，
# 当lazy_sum返回函数pre_sum时，相关参数和变量都保存在返回函数中，这种成为“闭包”(Closure)的程序结构拥有极大的威力。
# 返回一个函数时，牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量。

def count_test():
    fs = []
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs

# 如果一定要引用循环变量，方法再是创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变
def count_test2():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1,4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入g()
    return fs

# 可以利用lambda函数缩短代码
def count_test3():
    def f(j):
        return lambda :j*j
    fs = []
    for i in range(1,6):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入g()
    return fs



def my_test():
    a_sum = calc_sum(1,23,34,45)
    print(a_sum)
    la_sum1 = lazy_sum(1,23,45,6,6)
    la_sum2 = lazy_sum(1,23,45,6,6)
    # print(la_sum) # 此时返回的不是求和结果，而是求和函数
    print(la_sum1()) # 调用函数时才返回求和结果
    print(la_sum1==la_sum2) # 每次调用都会返回一个新的函数，即使传入相同的参数

    f1,f2,f3 = count_test()
    print(f1()) # 9 全部都是9，原因就在于返回的函数引用了变量i，但它并非立刻执行。
    print(f2()) # 9 等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9
    print(f3()) # 9 返回闭包时牢记一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量

    f4,f5,f6 = count_test2()
    print(f4())
    print(f5())
    print(f6())

    f7,f8,f9,f10,f11 = count_test3()
    print(f7())
    print(f8())
    print(f9())
    print(f10())
    print(f11())




def main():
    my_test()

if __name__ == '__main__':
    main()



