# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest, sys, os
import ibm_db
import config

name = 'name'
picture = 'picture'
conn_str = "DATABASE=%s;HOSTNAME=%s;PORT=%d;PROTOCOL=TCPIP;UID=%s;PWD=%s;" % (config.database, config.hostname, config.port, config.user, config.password)
# 测试类
class IbmDbTestCase(unittest.TestCase):
	
	# 测试方法
	def run_test_000():
		# 建立数据库连接
		conn = ibm_db.connect(conn_str, '', '')
		if conn:
			# 获取数据库服务信息
			server = ibm_db.server_info(conn)
			print('连接数据库服务器：', server.DBMS_NAME)
			# 删除已经存在的表
			drop_sql = 'DROP TABLE animals'
			try:
				result = ibm_db.exec_immediate(conn, drop_sql)
			except Exception as e:
				# 若不存在表，打印信息，程序继续往下执行
				print(drop_sql, '删除的表不存在：', e)
			# 创建表 animal
			create_sql = 'CREATE TABLE animals (id INTEGER, breed VARCHAR(32), name CHAR(16), weight DECIMAL(7,2))'
			# 执行建表语句
			result = ibm_db.exec_immediate(conn, create_sql)
			# 插入数据
			animals = (\
				(0, 'cat', 'Pook', 3.2),\
				(1, 'dog', 'Peaches', 12.3),\
				(2, 'horse', 'Smarty', 350.0),\
				(3, 'gold fish', 'Bubbles', 0.1),\
				(4, 'budgerigar', 'Gizmo', 0.2),\
				(5, 'goat', 'Rickety Ride', 9.7),\
				(6, 'llama', 'Sweater', 150))
			# 插入语句
			insert_sql = 'INSERT INTO animals (id, breed, name, weight) VALUES (?, ?, ?, ?)'
			# 准备  写这个似乎以前是Java程序员 stmt这很Java
			stmt = ibm_db.prepare(conn, insert_sql)
			if stmt:
				# 循环
				for animal in animals:
					# 执行插入动作
					result = ibm_db.execute(stmt, animal)
					print(animal, ', 插入结果：', result)

			# 创建视图
			# 首先删除视图
			drop_sql = 'DROP VIEW anime_cat'
			try:
				result = ibm_db.exec_immediate(conn, drop_sql)
			except Exception as e:
				# 若不存在表，打印信息，程序继续往下执行
				print(drop_sql, '删除的视图不存在：', e)
			# 接着创建视图
			ibm_db.exec_immediate(conn, '''
					CREATE VIEW anime_cat AS
					SELECT name, breed FROM animals WHERE id = 0
				''')
			
			# 删除表 animal_pics
			drop_sql = 'DROP TABLE animal_pics'
			try:
				result = ibm_db.exec_immediate(conn, drop_sql)
			except Exception as e:
				# 若不存在表，打印信息，程序继续往下执行
				print(drop_sql, '删除的表不存在：', e)
			# 创建表
			create_sql = 'CREATE TABLE animal_pics (name VARCHAR(32), picture BLOB)'
			# 执行建表语句
			result = ibm_db.exec_immediate(conn, create_sql)
			# 插入数据
			animals = (\
				('Spook', 'spook.png'),\
				('Helmut', 'pic1.jpg'))
			insert_sql = 'INSERT INTO animal_pics (name, picture) VALUES (?, ?)'
			# 预插入
			stmt = ibm_db.prepare(conn, insert_sql)
			if not stmt:
				print('Attempt to prepare statament failed.')
				return 0
			# 准备数据
			for animal in animals:
				name = animal[0]
				# 读取硬盘文件
				print('文件位置：', os.path.abspath(__file__))
				print('所属文件夹：', os.path.dirname(os.path.abspath(__file__)))
				print('读取图片位置：', os.path.dirname(os.path.abspath(__file__)) + '/' + animal[1])
				fileHandle = open(os.path.dirname(os.path.abspath(__file__)) + '/' + animal[1], 'rb') # 以二进制方式读取文件
				picture = fileHandle.read()
				if not picture:
					print('Could not retrieve picture "%s".' % animal[1])
					return 0
				# 输入流
				ibm_db.bind_param(stmt, 1, name, ibm_db.SQL_PARAM_INPUT)
				ibm_db.bind_param(stmt, 2, picture, ibm_db.SQL_PARAM_INPUT)
				# 执行插入
				result = ibm_db.execute(stmt)
				print(animal, ', 插入结果：', result)



			# 关闭数据库连接
			ibm_db.close(conn)

def main():
	IbmDbTestCase.run_test_000()


if __name__ == '__main__':
	main()