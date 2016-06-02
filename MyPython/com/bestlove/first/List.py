# -*- coding: utf-8 -*-
# 列表生成式

import os

def my_test():
	print(list(range(1,11)))
	# 列表生成式时，把要生成的x*x 放到前面，后面跟for循环就可以把list创建出来
	print([x*x for x in range(1,11)])
	# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方
	a = [x*x for x in range(1,11) if x%2 == 0]
	print(a)
	# 双重循环
	b = [m+n for m in 'ABC' for n in 'XYZ']
	print(b)
	# 列出当前目录下的所有文件和目录名
	c = [d for d in os.listdir('.')]
	print(c)
	d = {'梁思成':'林徽因','贾宝玉':'林黛玉','乔峰':'阿朱'}
	e = [k+'='+v for k,v in d.items()]
	print(e)
	f = ['Hello','World','Jams','Zhenni']
	g = [h.lower() for h in f]
	i = [h.upper() for h in f]
	print(g)
	print(i)
	# 去除不是字符串的元素，以免转小写时报错
	L1 = ['Hello','World',18,'Apple',None]
	L2 = [s.lower() for s in L1 if isinstance(s,str)==True ]
	print(L2)
	




def main():
	my_test()


if __name__=='__main__':
	main()