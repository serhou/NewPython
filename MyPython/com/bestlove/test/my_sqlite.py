# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# 导入SQLite驱动
import sqlite3

def test_conn():
    # 连接到SQLite数据库,数据库文件是test.db，如果文件不存在，会自动在当前目录创建
    conn = sqlite3.connect('test.db')
    # 创建一个Cursor
    cursor = conn.cursor()
    # 执行一条SQL语句，创建user表
    cursor.execute('create table T_USER (id VARCHAR(20) PRIMARY KEY ,name VARCHAR(20), age NUMBER(3))')
    # 继续执行一条SQL语句，插入一条记录
    cursor.execute('insert into T_USER (id, name, age) VALUES (\'1\',\'张三丰\',99)')
    cursor.execute('insert into T_USER (id, name, age) VALUES (\'2\',\'柳如是\',23)')
    # 通过rowcount获得插入的行数
    print(cursor.rowcount)  # 是1
    # 关闭Cursor
    cursor.close()
    # 提交事务
    conn.commit()
    # 关闭Connection
    conn.close()


def test_qry():
    # 查询记录
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    # 执行查询语句
    # cursor.execute('select * from T_USER where id=?', '2')
    cursor.execute('select * from T_USER')
    # 获得查询结果集
    values = cursor.fetchall()
    print(values)
    cursor.close()
    conn.close()


def my_test():
    # test_conn()
    test_qry()

def main():
    my_test()


if __name__ == '__main__':
    main()