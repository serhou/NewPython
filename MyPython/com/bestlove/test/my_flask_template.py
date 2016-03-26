# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, request, render_template

# Flask 默认支持的模板是jinja2  一定要把模板放到正确的templates目录下

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')


@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username=='admin' and password=='passwosrd':
        return render_template('signin-ok.html', username=username)
    return render_template('form.html', message='用户名或密码错误'.encode('utf-8'), username=username)


if __name__ == '__main__':
    app.run()