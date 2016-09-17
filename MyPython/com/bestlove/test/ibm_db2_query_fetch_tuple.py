# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import config
import ibm_db


conn_str = "DATABASE=%s;HOSTNAME=%s;PORT=%d;PROTOCOL=TCPIP;UID=%s;PWD=%s;" % ("sample", "192.168.1.109", 50000, "db2inst1", "db2inst1")

def operatorResult():
	# 查询数据库
	# 处理查询结果
    connectBD2()


def connectBD2():
	# 连接数据库
    # conn = ibm_db.connect('DATABASE=uibs;HOSTNAME=10.125.192.32;PORT=60000;PROTOCOL=TCPIP;UID=db2inst1;PWD=db2inst1;', '', '')
    conn = ibm_db.connect(conn_str, '', '')
    # 获取数据库服务器信息
    server = ibm_db.server_info(conn)
    # 查询数据库sql
    sql ="select * from emp"
    if conn:
        result = ibm_db.exec_immediate(conn, sql)
        onerow = ibm_db.fetch_tuple(result)
        while ( onerow ):
            print(onerow)
            onerow = ibm_db.fetch_tuple(result)
        
    	# 关闭数据库连接
    	# ibm_db.close(conn)
        

def main():
	operatorResult()

if __name__ == '__main__':
	main()