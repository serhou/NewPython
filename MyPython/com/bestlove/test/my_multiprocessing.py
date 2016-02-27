# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from multiprocessing import Process
import os

'''
	multiprocessing模块提供了一个Process类来代表一个进程对象，
	该模块就是跨平台的多进程模块
'''



def run_proc(name):
	print('Run child process %s (%s)...' % (name, os.getpid()))



def my_test():
	print('Parent process %s ' % os.getpid())
	# 创建子进程时，只需传入一个执行函数和函数的参数
	p = Process(target=run_proc, args=('test',)) 
	print('Child process will start.')
	p.start()  # start()方法启动   
	p.join()  # join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
	print('Child process end.')



def main():
	my_test()


if __name__ == '__main__':
	main()
