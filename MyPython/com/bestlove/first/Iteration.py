# -*- coding:utf-8 -*-
# 迭代
# 判断一个对象是可迭代对象的方法是通过collections模块的Iterable类型判断
from collections import Iterable

def my_test():
	d = {'a':1,'b':2,'c':3}
	# 迭代key
	for m in d:
		print(m)
	# 迭代value
	for n in d.values():
		print(n)
	# 迭代key和value
	for key,value in d.items():
		print(key,value)
	# 迭代字符串
	for s in 'ABCD':
		print(s)
	# 判断是否可以被迭代，返回布尔值
	print(isinstance('abc',Iterable))
	print(isinstance([1,3,4,5],Iterable))
	print(isinstance({'name':'张三丰','age':100,'地址':'武当'},Iterable))
	print(isinstance(12345,Iterable))
	# Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以再for循环中同时迭代索引和元素本身
	for i,val in enumerate(['康熙','雍正','乾隆','嘉庆']):
		print(i,val)
	
	# 两个变量的for循环,很常见
	for x,y in [(1,'A'),(2,4),('B',2),('C','D')]:
		print(x,y)
	
def main():
	my_test()

if __name__=='__main__':
	main()