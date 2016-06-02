# -*- coding:utf-8 -*-
# 函数
# abs 求绝对值的函数
import math
print(abs(-199.28))
print(abs(11239))
# max() 返回最大值的函数
print(max(1,34,2,345,238873,-283,88))
# 数据类型转换
# 字符串转整数型
print(int('1273'))
# 字符串转浮点型
print(float('-1872.273'))
# 浮点转字符串型
print(str(-326.373))
# 整数转字符串型
print(str(3847))
# 布尔类型的
print(bool(1))
print(bool(0))# 0为False,其他值为True
print(bool(-3))
print(bool(''))# 空字符串为False,其他值为True
print(bool('adb'))
# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量
# 相当于给这个函数起一个别名
a = abs
print(a(-3434.3874))
# 十进制整数转换为十六进制的字符串的函数hex()
print(hex(783287312819238))
# 定义一个函数
def my_abs(x):
	if x>=0:
		return x
	else:
		return -x
print('绝对值是：',my_abs(-734.23))
# 空函数 可以用pass语句
# pass 语句什么都不做，实际上pass可以用来作为占位符，比如现在还没有想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来
def nop():
	pass # 如果不写pass，什么也不写，代码运行就会有语法错误
# pass还可以用在其他的语句里
age = 89
if age>8:
	pass # 同理，这里没有pass也是会报错的
def my_move(x,y,step,angle=0):
	nx = x + step*math.cos(angle)
	ny = y - step*math.sin(angle)
	return nx,ny
r = my_move(100,100,60,math.pi/6)
print(r)
