# -*-coding:utf-8 -*-
# 条件判断 if... elif ...elif ...else
# height = 1.75
# weight = 80.5
height = input('请输入你的身高(单位:m)：')
height = float(height)
weight = input('请输入你的体重(单位：kg)：')
weight = float(weight)
a = weight/(height**2)
if a<=18.5:
	print('你这瓜娃子过轻了')
elif a <=25:
	print('你这瓜娃子正常')
elif a <= 32:
	print('你这瓜娃子肥胖')
else:
	print('你这瓜娃子严重肥胖')
# 循环语句 for ... in ...
# list
names = ['小儿他娘','孩他爹','孩他姑','孩他舅']
for name in names:
	print(name)
# tuple
names2 = ('张三','李斯','王五','赵马子',['小宝','小草'])
for name in names2:
	if type(name)==list:
		for n in name:
			print(n)
	else:
		print(name)
sum = 0
for tmp in [1,2,3,4,5,6,7,8,9,10]:
	sum = sum + tmp
print(sum)
# range
print(list(range(5)))
# 1-100的整数之和
sum = 0
for m in range(101):
	sum = sum + m
print(sum)
# while 循环
# 计算100以内所有奇数之和
sum = 0
n = 99
while n > 0:
	sum = sum + n
	n = n-2
print(sum)