# !/usr/bin/env python3
# -*- coding: utf-8 -*-


from multiprocessing import Process, Queue
import os, time, random


'''
	在Linux、Unix下，multiprocessing模块封装了fork()调用，使我们不需要关注fork()的细节
	由于Windows没有fork调用，因此，multiprocessing需要“模拟”出fork()的效果，父进程
	所有的Python对象都必须通过pickle序列化再传到子进程去，所以，如果multiprocessing在
	Windows下调用失败了，要首先考虑是不是pickle失败了
'''



# 写数据进程执行的代码
def write(q):
	print('Process to write: %s' % os.getpid())
	for value in ['A', 'B', 'C']:
		print('Put %s to queue...' % value)
		q.put(value)
		time.sleep(random.random())



# 读取数据进程执行的代码
def read(q):
	print('Process to read: %s' % os.getpid())
	while True:
		value = q.get(True)
		print('Get %s from queue.' % value)





def my_test():
	# 父进程创建Queue，并传给各个子进程
	q = Queue()
	pw = Process(target=write, args=(q,))
	pr = Process(target=read, args=(q,))
	# 启动子进程pw,写入
	pw.start()
	# 启动子进程pr,读取
	pr.start()
	# 等待pw结束
	pw.join()
	# pr进程里是死循环，无法等待其结束，只能强行终止
	pr.terminate()



def main():
	my_test()



if __name__ == '__main__':
	main()
