# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from email.mime.text import MIMEText
import smtplib

# SMTP是发送邮件的协议，Python内置对SMTP的支持，可以发送纯文本邮件、HTML邮件以及带附件的邮件。

'''
    From:xxxxx@sohu.com
    Password:********
    To:xxxxxx@163.com
    SMTP server:smtp.sohu.com
'''

def my_test():
    msg = MIMEText('Hello, send by Python...', 'plain', 'utf-8')
    # 输入Email地址和口令
    from_addr = input('From:')
    password = input('Password:')
    # 输入收件人地址
    to_addr = input('To:')
    # 输入SMTP服务器地址
    smtp_server = input('SMTP server:')
    # SMTP协议默认端口25
    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()


def main():
    my_test()


if __name__ == '__main__':
    main()