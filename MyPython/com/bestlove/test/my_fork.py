# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import os


def test_os():
	print('Process (%s) start...' % os.getpid())
	# 该方法只能运行在linux,unix等系统上
	pid = os.fork()
	if pid == 0:
		print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
	else:
		print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

	'''
		由于Windows 没有fork调用，上面的代码在Windows上无法运行，上面的代码在CentOS上运行正常
		有了fork调用，一个进程在接到新任务时就可以复制一个子进程来处理新任务，常见的Apache服务器就是由父进程监听端口，当有新的http请求时，就fork出子进程来处理新的http请求
	'''

def my_test():
	test_os()


def main():
	my_test()



if __name__== '__main__':
	main()
