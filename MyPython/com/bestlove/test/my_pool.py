# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from multiprocessing import Pool
import os, time, random

# 如果要启动大量的子进程，可以用进程池的方式批量创建子进程


def login_time_task(name):
	print('Run task %s (%s)...' % (name, os.getpid()))
	start = time.time()
	time.sleep(random.random()*3)
	end = time.time()
	print('Task %s runs %0.2f seconds.' % (name, (end - start)))


def my_test():
	print('Parent process %s.' % os.getpid())
	p = Pool(4)  # 设置进程池大小为4
	for i in range(5):
		p.apply_async(login_time_task, args=(i,))
	print('Waiting for all subprocesses done...')
	p.close()  # 对于Pool对象，调用join()之前必须先调用close()方法，调用join()完毕后就不能继续添加新的Process了
	p.join()  # 调用join()方法会等待所有子进程执行完毕
	print('All subprocesses done.')

	'''
		请注意输出结果，task 0, 1, 2, 3 是立刻执行的，
		而task 4 要等待前面某个task 完成后才能执行
		这是因为我们设置进程池的默认大小为4，因此，最多同时执行4个进程。
		这是Pool有意设计的限制，并不是操作系统的限制，我们可以改成p=Pool(5)就可以同时跑5个进程
		由于Pool的默认大小是CPU的核心数，如果你不幸拥有8核CPU,你至少需要
		提交9个子进程才能看到上面的效果
	'''

def main():
	my_test()


if __name__ == '__main__':
	main()
