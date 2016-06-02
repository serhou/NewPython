# -*- coding: utf-8 -*-


# 在Python中，一边循环一边计算的机制，称为生成器：generator
def my_test():
	# 要创建一个generator的最简单方法，是只要把一个列表生成式的[]改成()
	# 列表生成式
	L = [x*x for x in range(10)]
	print(L)
	# 生成器:创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator。
	g = (x*x for x in range(10))
	print(g) # <generator object my_test.<locals>.<genexpr> at 0x00000052F12779E8>
	# 如果要一个一个打印出来，可以通过next()函数获得generator的下一个返回值
	print(next(g))
	print(next(g))
	print(next(g))
	print(next(g))
	print(next(g))
	print(next(g))
	print(next(g))
	print(next(g))
	print(next(g))
	print(next(g))
	#print(next(g)) # 第11个会抛出异常StopIteration错误，因为此时已经没有元素了
	# 当然上面这种不断调用next(g)实在是太变态了，正确的方法是使用for循环，因为generator也是可迭代对象
	for n in g:
		print(n) # 成功避免越界
# 如果推算的算法比较复杂，用类似列表生成式的for循环无法实现的时候，还可以用函数来实现
# 例如，著名的斐波那契数列(Fibonacci)，除第一个和第二个数外，任意一个数都可以由前两个数相加得到：1,1,2,3,5,8,13,21,34,55,……
# 斐波那契数列用列表生成式写不出来，但是用函数把它打印出来却很容易：
def fib(max):
		n,a,b = 0,0,1
		while n < max:
			print(b)
			a,b = b,a+b
			n = n+1
		return 'done'
# 仔细观察，可以看出，fib函数实际上是定义了斐波那契数列的推算规则，上面的函数和generator仅一步之遥。要把fib函数变成generator，只需要把print(b)改为yield b 就可以了
def fibonacci(max):
	n,a,b = 0,0,1
	while n < max:
		yield b
		a,b = b,a+b
		n = n+1
	return 'done'

# 实现一个杨辉三角 也是双循环
def triangles():
	L = [1,]
	while True:
		yield L
		i = len(L)-1
		while i:
			L[i] = L[i]+L[i-1]
			i -= 1
		L.append(1)
# 测试杨辉三角
def test(max):
	n = 0
	for x in triangles():
		print(x)
		n = n+1
		if n == max:
			break
	
def main():
	my_test()
	print('请输入你想要的斐波那契数列的元素个数：')
	max = input()
	print('********************华丽的分割线*********************')
	m = fib(int(max))
	print(m)
	print('++++++++++++++++++第二个分割线++++++++++++++++++')
	n = fibonacci(int(max))
	# for c in n:
		# print(c) #用for循环调用generator时，发现拿不到generator的return语句的返回值
	# print('========================再次分割============================')
	# 如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中
	while True:
		try:
			k = next(n)
			print('g:',k)
		except StopIteration as e:
			print('Generator return value:',e.value)
			break

	test(30)
			
if __name__=='__main__':
	main()