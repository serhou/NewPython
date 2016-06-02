# -*- coding:utf-8 -*-
import math
def my_abs(x):
	if not isinstance(x,(int,float)): # 参数检查
		raise TypeError('bad operand type')
	if x >= 0:
		return x
	else:
		return -x
def my_move(x,y,step,angle=0):
	nx = x + step*math.cos(angle)
	ny = y - step*math.sin(angle)
	return nx,ny