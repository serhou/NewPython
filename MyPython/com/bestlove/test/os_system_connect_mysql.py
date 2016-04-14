# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import os


def test(hostname, port, username, password, dbname, sqltext, logtext):
	a = os.system('mysql -h %s -P %s -u %s -p%s %s --default-character-set=utf8  < %s > %s' % (hostname, port, username, password, dbname, sqltext, logtext))
	print('返回值：%s'.decode('utf-8') % a)
	if(a==0):
		print('成功')
	else:
		print('失败')


if __name__ == '__main__':
	test('192.168.1.108', '3306', 'webnav', 'webnav', 'webnav', 'webnav2.sql < webnav3.sql', 'webnav8.log') 


