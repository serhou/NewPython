#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#list and tuple
classnames = ['张三丰','李元霸','柳如是']
print(classnames,'的长度是',len(classnames))
print('第一个学生是:',classnames[0])
print('第二个学生是:',classnames[1])
print('第三个学生是:',classnames[2])
print('最后的学生是:',classnames[-1])
print('倒数第二的学生是:',classnames[-2])
classnames.append('李婉儿')
print('添加新学生后的最后的学生是:',classnames[-1])
print(classnames,'的长度是',len(classnames))
classnames.insert(0,'詹姆斯·邦德')
print('插入一个学生后的第一个学生是：',classnames[0])
print(classnames,'的长度是',len(classnames))
print('删除末尾的学生：',classnames.pop())
print(classnames,'的长度是',len(classnames))
print('删除第二个学生是：',classnames.pop(1))
print(classnames,'的长度是',len(classnames))
classnames[0]='弗朗·珍妮'
print('第一个学生被替换后：',classnames)
L = ['Python',13,True]
print('里面值不同类型的List：',L,'的长度是：',len(L))
L2 = ['Python','Java',['Go',23],18,False]
print('List里面还可以有List：',L2,'的长度是：',len(L2))
print('取出里面的那个List中的第一个值:',L2[2][0])
# 另有一种有序列表叫元祖：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改
classnames2 = ('王二小','赵铁蛋','李三胖')
print('tuple是：',classnames2,'的长度是：',len(classnames2))
print('第二个学生是：',classnames2[1])
t = ()
print('空的tuple是：',t)
t = (1)
print('t = (1)定义的不是tuple，而是1这个数：',t)
t = (1,)
print('只有一个元素时定义tuple必须加上一个,如：t = (1,)。打印后：',t)
# 可变的tuple，其实并不是tuple可变，而是tuple中元素的元素可变
t2 = ('李广','华荣',['吴用','卢俊义','李逵'],'时迁')
print(t2,'的长度是：',len(t2))
# 后面添加
t2[2].append('林冲')
print(t2,'的长度是：',len(t2))
# 前排插入
t2[2].insert(0,'武松')
print(t2,'的长度是：',len(t2))
# 替换
t2[2][1]='鲁智深'
print(t2,'的长度是：',len(t2))
