# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, INT, Float, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

'''
    ORM框架，Object-Relational Mapping,把数据库的表结构映射到对象上。
    在Python中，最有名的ORM框架是SQLAlchemy。
'''

# 创建对象的基类
Base = declarative_base()

# 定义User对象
class User(Base):
    # 表名字
    __tablename__ = 'mianshi'
    # 表结构
    name = Column(String(255), primary_key=True)
    subject = Column(String(255))
    score = Column(Float(12))
    sid = Column(INT)
    # 一对多
    books = relationship('Book')


class Book(Base):
    __tablename__ = 'book'
    bid = Column(String(255), primary_key=True)
    bookname = Column(String(255))
    # 多对一方的book表是通过外键关联到user表的
    ssid = Column(INT, ForeignKey('mianshi.sid'))


# 初始化数据库连接
engine = create_engine('mysql+mysqlconnector://root:think@localhost:3306/mianshi')
# 创建DBSession类型
DBSession = sessionmaker(bind=engine)


def test_query():
    # 创建session对象
    session = DBSession()
    # 创建Query查询，filter是where条件，最后调用one()返回唯一行，
    # 如果调用all()则返回所有行
    list = session.query(User, Book).filter(User.sid == Book.ssid).all()
    # 打印类型和对象的name属性
    # print('type:', type(user))
    # print('name:', user.name)
    # print(user.name, user.subject, user.score, user.sid)
    for user,book in list:
        print(user.name, book.bookname)
    # 关闭session
    session.close()


def test_insert():
    # 创建session对象
    session = DBSession()
    # 创建新的User对象
    new_user = User(name='吴文熙', subject='体育', score=78, sid=6)
    # 添加到session
    session.add(new_user)
    # 提交事务
    session.commit()
    # 关闭session
    session.close()


def my_test():
    # test_insert()
    test_query()

def main():
    my_test()


if __name__ == '__main__':
    main()