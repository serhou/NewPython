# !/usr/bin/env python3
# -*- coding: utf-8 -*-




def main():

	# String 字符串  不可以通过索引来修改
	str = 'JavaScript'
	print(str)
	print(str[0:-1])
	print(str[2])
	print(str[2:5])
	print(str[3:])
	print(str * 3)
	print(str + 'Python')


	'''
		Python 字符串不能被改变
		注意：
			1.反斜杠\可以用来转义，使用r可以让反斜杠不发生转义
			2.字符串可以用+运算符连接在一起，用*运算符重复
			3.Python中的字符串有两种索引方式，从左往右以0开始，从右往左以-1开始
			4.Python中的字符串不能改变
	'''


	# List 列表
	list = [1, 123, 12.45, True]
	print(list)
	print(list[1:3])
	print(list[0:-2])
	print(list[2:])
	print(list * 2)
	print(list + list + list)
	# 赋值  通过索引来修改数据
	list[2:4] = ['When do', False]
	print(list)

	"""
		注意：
			1.List写在方括号之间，元素用逗号隔开
			2.和字符串一样，list可以被索引和切片
			3.List可以使用+操作符进行拼接
			4.List中的元素是可以改变的
	"""


	# Tuple 元组 不可以通过索引赋值
	# tuple的元素不可改变，但它可以包含可变的对象，比如list列表
	tuple = ('java', 78, 2.45, 'Python', True)
	tinytuple = (34, 'redis')
	print(tuple)
	print(tuple[0])
	print(tuple[1:3])
	print(tuple[2:])
	print(tinytuple*2) # 重复一遍
	print(tuple + tinytuple)
	# tuple[2:3] = (66, False) # TypeError: 'tuple' object does not support item assignment
	print(tuple)

	tup1 = () # 空元组
	tup2 = (29,) # 只一个元素，需要在元素后添加逗号
	print(tup1)
	print(tup2)
	tup3 = (48) # int
	print(type(tup3))
	tup4 = (True) # bool
	print(type(tup4))
	tup5 = ('Java') # string
	print(type(tup5))

	# sting、list和tuple都属于sequence(序列)
	'''
		注意：
			1.与字符串一样，元组的元素不能修改
			2.元组也可以被索引和切片，方法一样
			3.注意构造包含0或1个元素的特殊语法规则
			4.元组也可以使用+操作符进行拼接
	'''

	# Set 集合 是一个无序不重复元素的序列
	'''
		# 基本功能是进行成员关系测试和删除重复元素
		# 可以使用大括号{} 或者set()函数创建集合
		# 注意：创建一个空集合必须用set()而不是{}
		# 因为{} 是用来创建一个空字典
	'''
	student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
	print(student) # 输出集合，重复的元素被自动去掉
	# 成员测试
	if('Rose' in student):
		print('Rose 在集合中')
	else:
		print('Rose 不在集合中')

	# set可以进行集合运算
	a = set('我们都是中国人')
	b = set('we are Chinese')
	c = set('ni qu na er')
	print(a)
	print(b)
	print(c)
	print(b - c) # b和c的差集
	print(b | c) # b和c的并集
	print(b & c) # b和c的交集
	print(b ^ c) # b和c中不同时存在的元素


	# Dictionary 字典
	'''
		字典是Python中另一个非常有用的内置数据类型
		列表是有序的对象结合，字典是无序的对象集合。
		两者之间的区别在于：字典当中的元素是通过键
		来存取的，而不是通过偏移存取

		字典是一种映射类型，字典应{}标识，它是一个
		无序的键key:值value对集合。

		键key必须使用不可变类型

		在同一个字典中，键key必须是唯一的。
	'''

	dicts = {} # 空字典
	dicts['one'] = 'Java'
	dicts[2] = 'Python'

	tinydict = {'name':'Java', 'code':'1', 'score':67}

	print(dicts)
	print(dicts['one']) # 'one' 是键
	print(dicts[2]) # 2是键
	print(tinydict)
	print(tinydict.keys())
	print(tinydict.values())
	# 构造函数dict()可以直接从键值对序列中构建
	joydict = dict([('Go', 1), ('Hadoop', 2), ('Scala', 3)]) 
	print(joydict)
	modict = {x: x**2 for x in (1, 2, 3, 5, 7, 16)} # 构建的方法倒是有许多种
	print(modict)
	dedict = dict(Python=1, Java=2, Oracle=3) # 构建的一种方法
	print(dedict)

	'''
		字典类型也有一些内置的函数，例如clear()、keys()、values()
		注意：
			1.字典是一种映射类型，它的元素是键值对。
			2.字典的关键字必须为不可变类型，且不能重复。
			3.创建空字典使用{}
	'''

	'''
		Python数据类型转换
		数据类型的转换，只需要将数据类型作为函数名即可
	'''




if __name__ == '__main__':
	main()