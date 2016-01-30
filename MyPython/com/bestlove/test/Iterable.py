# -*- coding: utf-8 -*-
# 迭代器
# 我们已经知道，可以直接作用于for循环的数据类型有以下几种：
	# 一类是集合数据类型，如list、tuple、dict、set、str等
	# 一类是generator,包括生成器和带yield的generator function
# 这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。可以使用isinstance()判断一个对象是否是Iterable对象

from collections import Iterable
from collections import Iterator

'''
	为什么list、dict、str等数据类型不是Iterator?
	这是因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，
	直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个有序序列，但是我们却不能提前知道序列的长度，
	只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。
	
	Python的for循环本质上就是通过不断调用next()函数实现的

'''

# Python的for循环本质上就是通过不断调用next()函数实现的，如：
def your_test():
	for x in [1,23,45,93,66,78,45,67]:
		print(x)
	print('##################分割线##################')
	it = iter([1,23,45,6,7,8,8,4,5,67,889,])# 获取Iterator对象
	# 循环
	while True:
		try:
			# 获取下一个值
			x = next(it)
			print(x)
		except StopIteration:
			# 遇到StopIteration就退出循环
			break
	

# 把list,dict,str等Iterable变成Iterator可是使用iter()函数
def iterable_to_iterator(args):
	a = iter(args)
	return a



# 生成器不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，这个对象成为迭代器：Iterator
# 测试迭代器
def  test_iterator(args):
	a  = isinstance(args,Iterator)
	print(a)


# 测试可迭代对象
def my_test(args):
	# a = isinstance([],Iterable)
	# b = isinstance({},Iterable)
	# c = isinstance('ABCD',Iterable)
	# print(a)
	# print(b)
	# print(c)
	a = isinstance(args,Iterable)
	print(a)



def main():
	# 测试可迭代对象
	my_test([2,34,56,78,97]) # list
	my_test({'s':'m','a':'v'}) # dict
	my_test('ABCD') # str
	my_test(123456) # int
	my_test((1,3,4)) # tuple
	my_test({1,23,5,6,'sdf'}) # set 
	my_test(x for x in range(10)) # generator
	print('*******************华丽的分割线*******************')
	# 测试迭代器
	test_iterator([2,34,56,78,97]) # list
	test_iterator({'s':'m','a':'v'}) # dict
	test_iterator('ABCD') # str
	test_iterator(123456) # int
	test_iterator((1,3,4)) # tuple
	test_iterator({1,23,5,6,'sdf'}) # set 
	test_iterator(x for x in range(10)) # generator
	# 生成器都是Iterator对象，但是list,dict,str虽然是Iterable，却不是Iterator
	# 把list,dict,str等Iterable变成Iterator可是使用iter()函数
	print('======================再次分割=======================')
	# 转换成Iterator
	test_iterator(iterable_to_iterator([2,34,56,78,97])) # list
	test_iterator(iterable_to_iterator({'s':'m','a':'v'})) # dict
	test_iterator(iterable_to_iterator('ABCD')) # str
	# test_iterator(iterable_to_iterator(123456)) # int 转不了会报错
	test_iterator(iterable_to_iterator((1,3,4))) # tuple
	test_iterator(iterable_to_iterator({1,23,5,6,'sdf'})) # set 
	print('!!!!!!!!!!!!!!!!!!!!!!!!!分割线!!!!!!!!!!!!!!!!!!!!!!!!!!')
	your_test()

if __name__=='__main__':
	main()