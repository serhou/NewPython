#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print('我们都有一个家，名字叫中国！')
print((233+348)*2+238-384)
print('问一声那海鸥，你飞来飞去有何求','问一问，你会不会想家')
print((233+348)*2+238-384/343-123*(3+172))
print('1024*768=',1024*768)
print('I\'m,"OK"')
print('I\'m learning\nPython')
print('\\\n\\')
print(r'\\\n随意')
print('''你是谁
我不知道你是谁
你到底是谁''')
print(3>2 and 2>3)
print(3>2 or 2>3)
print(not 2>3)
print(10/3)
print(10//3)
print(10%3)
print(ord('A'))
print(chr(66))
print(chr(25991))
print('\u4e2d\u6587')
print('ABC'.encode('ascii'))
print('中国不高兴'.encode('utf-8'))
print(b'\xe4\xb8\xad\xe5\x9b\xbd\xe4\xb8\x8d\xe9\xab\x98\xe5\x85\xb4'.decode('utf-8'))
print(len('ABC'))
print(len('中国人民在今天胜利了'))
print(len(b'ABC'))
print(len(b'\xe4\xb8\xad\xe5\x9b\xbd\xe4\xb8\x8d\xe9\xab\x98\xe5\x85\xb4'))
print(len('中国不高兴'.encode('utf-8')))
print('Hello,%s' % '张三丰')
print('Hi,%s,你有￥%d' % ('李元霸',100000))
print('%5d-%03d' % (4,5))#格式化整数和浮点数还可以指定是否补0和整数与小数的位数
print('%.2f' % 3.1415926)
print('Age: %s Gender: %s' % (25,True))
print('growth rate: %d %%' % 6)
s1 = 72
s2 = 85
r = (85/72-1)*100
print('%.1f%%' % r)
a = input('3+12=')
a = int(a)
if a==15:
	print('恭喜你，算对了')
elif a==16:
	print('加油啊，差一点')
elif a==14:
	print('加油啊，差一点')
else:
	print('你大爷，算错了')
name = input('请愉快的输入你的名字：')
print(name,'和情人在一起坐过山车')

