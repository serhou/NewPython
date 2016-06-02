#!usr/lib/env python3
#-*- coding:utf-8 -*-


# 切片
def my_test():
	L = ['张三丰','李元霸','柳如是','李婉儿']
	print(L[1:3])
	print(L[0:4])
	# 如果第一个索引是0，则可以省略
	print(L[:2])
	# Python同样支持倒数切片
	print(L[-1:])
	print(L[-3:-1])
	
	L2 = list(range(100))
	print(L2)
	print(L2[:10])
	print(L2[-10:])
	print(L2[10:20])
	# 前10个数，每两个取一个
	print(L2[:10:2])
	# 所有数，每5个取一个
	print(L2[::5])
	# 什么都不写，只写[:]就可以原样复制一个list
	print(L2[:])
	# tuple也是一种list，唯一区别是tuple不可变,所以tuple也可以用切片操作，只是操作的结果仍是tuple
	T = tuple(range(100))
	print('T:',T)
	print(T[:3])
	print(T[4:19:5])
	# 字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串
	S = 'ABCDEFGHIG'
	print(S[:3])
	print(S[::2])
	
	
def main():
	my_test()
	
if __name__ == '__main__':
	main()