# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask
from flask import request

# Python 的装饰器类似于Java的注解

my_flask_app = Flask(__name__)

# 访问网址http://127.0.0.1:5000/
@my_flask_app.route('/', methods=['GET', 'POST'])
def home():
    return '<head><meta charset="utf-8"></head><h1>欢迎访问我们的首页！</h1>'.encode('utf-8')

# 访问网址http://127.0.0.1:5000/signin
@my_flask_app.route('/signin', methods=['GET'])
def signin_form():
    return '''<head><meta charset="utf-8"></head>
              <body>
              <form action="/signin" method="post">
              <p>用户名<input name="username"></p>
              <p>密  码<input name="password" type="password"></p>
              <p><button type="submit">登录</button></p>
              </form></body>
            '''.encode('utf-8')

# http://127.0.0.1:5000/signin后提交表单
@my_flask_app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容
    if request.form['username']=='admin' and request.form['password']=='password':
        return '<head><meta charset="utf-8"></head><h3>Hello,admin!</h3>'.encode('utf-8')
    return '<head><meta charset="utf-8"></head><h3>用户名或密码错误</h3>'.encode('utf-8')



if __name__ == '__main__':
    my_flask_app.run()