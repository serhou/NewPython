# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

def main():

	with open('1.json', 'r', encoding='utf-8') as f:
		data = json.load(f)
	print(type(data['select']))
	datas1 = data['select']
	datas2 = data['select'].copy()
	for d in datas1:
		a = 0
		for m in datas2:
			if(d['ACNO']==m['ACNO']):
				a += 1
		if a > 1:
			print('重复的是：%s，重复了%s次' % (d['ACNO'], a))

if __name__ == '__main__':
	main()