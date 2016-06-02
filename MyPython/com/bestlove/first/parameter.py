#-*- coding:utf-8 -*-
# 位置参数
def power(x):
	return x*x
def power_two(x,n):
	s = 1
	while n>0:
		n = n-1
		s = s*x
	return s
# 默认参数 默认参数在必选参数之后如果不传值，则使用默认参数，如果传值则使用传入的值
def power_three(x,n=2):
	s = 1
	while n>0:
		n = n-1
		s = s*x
	return s
def enroll(name,gender,age=6,city='北京'):
	print('name',name)
	print('gender',gender)
	print('age',age)
	print('city',city)
	
#enroll('张三丰','男',123,'武当')	
#enroll('李元霸','男')
#enroll('柳如是','女',34)
#enroll('李婉儿','女',city='金陵')

# 一个坑
def add_end(L=[]):
	L.append('END') # 如果不传参，则执行多次，会出现多个END
	return L
# 修改后
def add_end2(L=None):
	if L is None:
		L = []
	L.append('END2')
	return L
	

# 定义一个list或者tuple参数
def calc(numbers):
	sum = 0
	for n in numbers:
		sum = sum+n*n
	return sum
# calc([1]) #list
# calc((1,)) # tuple
# calc((1,2,3))
# calc([1,2,3,4,5])

# 可变参数 定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。
def calc2(*numbers):
	sum = 0
	for n in numbers:
		sum = sum+n*n
	return sum
# calc2(1)
# calc2(1,3,5,6,73)

# 关键字参数 函数person除了必选参数name和age外，还接受关键字参数kw
def person(name,age,**kw):
	print('name:',name,'age:',age,'other:',kw)
# person('张三丰',23,city='武当')
# person('张君宝',188,father='张弢',mother='辛凤穗')
# extra = {'city': 'Beijing', 'job': 'Engineer'}
# person('Jack', 24, **extra)

# 命名关键字参数 如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。
# 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
def person_two(name,age,*,city,job):
	print(name,age,city,job)
# person_two('张三丰',177,city='武当',job='太极宗师')
def person_three(name,age,*,city='北京',job):
	print(name,age,city,job)
# person_three('朱元璋',23,job='皇帝')

# 参数组合
# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用，
# 除了可变参数无法和命名关键字参数混合。
# 但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数/命名关键字参数和关键字参数。
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
# 注意：
# 使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

# 命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。

# 定义命名的关键字参数不要忘了写分隔符*，否则定义的将是位置参数。
