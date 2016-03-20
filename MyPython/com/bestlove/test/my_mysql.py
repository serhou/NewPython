# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import mysql.connector

def test_qry():
    # 建立数据库连接
    conn = mysql.connector.connect(user='root', password='think', database='mianshi')
    # 创建游标
    cursor = conn.cursor()
    # 执行SQL语句
    cursor.execute('select * from mianshi where sid = %s', [3])
    # cursor.execute('select * from mianshi')
    # 获取查询返回的数据
    values = cursor.fetchall()
    print(values)
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()




def test_conn():
    # 建立数据库连接
    conn = mysql.connector.connect(user='root', password='think', database='mianshi')
    # 创建游标
    cursor = conn.cursor()
    # 执行SQL语句
    cursor.execute('insert into mianshi(name, subject,score,sid) VALUES (%s, %s, %s, %s)', ['李香君', '音乐', 88, 4])
    cursor.execute('insert into mianshi(name, subject,score,sid) VALUES (%s, %s, %s, %s)', ['侯孝贤', '电影', 90, 5])
    print(cursor.rowcount)
    # 提交事务
    conn.commit()
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()


def my_test():
    # test_conn()
    test_qry()


def main():
    my_test()


if __name__ == '__main__':
    main()