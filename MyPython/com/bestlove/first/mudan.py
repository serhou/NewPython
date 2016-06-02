# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

def main():
	print('唯有牡丹真国色，花开时节动京城')
	# os.system('ipconfig/all')
	print('人间四月芳菲尽，山寺桃花始盛开')
	a = 0
	for x in '唯有牡丹真国色，花开时节动京城':
		b = 0 
		a = a + 1 
		print(x)
		for y in '人间四月芳菲尽，山寺桃花始盛开':
			b = b + 1
			if a==b and x != '，':
				print(y)



if __name__ == '__main__':
	main()