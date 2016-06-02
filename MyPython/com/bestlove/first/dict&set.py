# -*- coding:utf-8 -*-
# dict 亦或是map
d = {'张三丰':98,'李元霸':87,'柳如是':89}
print('柳如是：',d['柳如是'])
print('张三丰：',d['张三丰'])
d['张三丰']=62
print('张三丰：',d['张三丰'])
#print('邦德:',d['邦德']) #如果没有这个key,则抛出错误
print('邦德' in d) # 返回False，来判断
print(d.get('邦德'))# 返回None，来判断
print(d.get('邦德',-1))# 自定义值返回-1，来判断
# 删除
print(d.pop('张三丰'))
print('张三丰：',d.get('张三丰',-1))
# set
s = set([1,23,45])
print(s)
s.add(56)
print(s)
s.add(56)
print(s)
s.remove(1)
print(s)
s2 = set([4,24,56,45])
print(s2)
print(s & s2)
print(s | s2)
a = ['章三道','仇倩云','青龙侠']
print(a)
a.sort()
print(a)
b = 'abc'
b.replace('a','A')
print(b.replace('a','A'))
print(b)
