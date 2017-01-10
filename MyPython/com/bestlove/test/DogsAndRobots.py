# !/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
	鸭子类型机制 ------ 潜在类型机制
	perform(anything)中，没有任何针对anything的类型，
	anything只是一个标识符，它必须能够执行perform()
	期望它执行的操作，因此这里隐含着一个借口。但是你
	从来都不必显式地写出这个接口——它是潜在的。perform()
	不关心其参数的类型，因此我可以向它传递任何对象，只要
	该对象支持speak()和sit()方法。如果传递给perform的对象
	不支持这些操作，那么将会得到运行时异常。
'''


class Dog:
	def speak(self):
		print("Arf!")
	def sit(self):
		print("Sitting")
	def reproduce(self):
		pass

class Robot:
	def speak(self):
		print("Click!")
	def sit(self):
		print("Clank!")
	def oilChange(self):
		pass

def perform(anything):
	anything.speak()
	anything.sit()
	
a = Dog()
b = Robot()

perform(a)
perform(b)