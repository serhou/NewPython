# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import config
import ibm_db


conn_str = "DATABASE=%s;HOSTNAME=%s;PORT=%d;PROTOCOL=TCPIP;UID=%s;PWD=%s;" % (config.database, config.hostname, config.port, config.user, config.password)

def operatorResult():
	# 查询数据库
	# 处理查询结果
    arr, dc = connectBD2()
    getSameAcNo(arr, dc)

def getSameAcNo(arr, dc):
	for d in arr:
		a = 0
		for m in arr:
			if(d==m):
				a += 1
		if a > 1:
			print('重复的是：%s，名称:%s，重复了%s次' % (d, dc[d], a))


def connectBD2():
	# 连接数据库
    # conn = ibm_db.connect('DATABASE=uibs;HOSTNAME=10.125.192.32;PORT=60000;PROTOCOL=TCPIP;UID=db2inst1;PWD=db2inst1;', '', '')
    conn = ibm_db.connect(conn_str, '', '')
    # 获取数据库服务器信息
    server = ibm_db.server_info(conn)
    # 查询数据库sql
    sql ='select PID, "NAME" from PRODUCT'
    arr = []
    dc = {}
    if conn:
    	# 执行查询语句
    	stmt = ibm_db.exec_immediate(conn, sql)
    	# 处理查询结果
    	while (ibm_db.fetch_row(stmt)):
    		acno, dc[acno] = ibm_db.result(stmt, 0), ibm_db.result(stmt, 1)
    		arr.append(acno)
    	# 打印服务器名称
    	print(server.DBMS_NAME)

    	# 关闭数据库连接
    	ibm_db.close(conn)
    return arr, dc

def main():
	operatorResult()

if __name__ == '__main__':
	main()