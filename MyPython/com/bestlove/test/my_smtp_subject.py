# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib

'''
    From:xxxxx@163.com
    Password:********
    To:xxxxxx@sohu.com
    SMTP server:smtp.163.com
'''


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def my_test():
    from_addr = input('From:')
    password = input('Password:')
    to_addr = input('To:')
    smtp_server = input('SMTP server:')
    # msg = MIMEText('你好,我是一名Python程序员 ...', 'plain', 'utf-8')
    # 发送HTML邮件
    msg = MIMEText('<html><body><p><h1>你好,</h1>我是一名Python程序员 ...<br><a href="http://www.python.org">Python</a></p></body></html>', 'html', 'utf-8')
    msg['From'] = _format_addr('Python程序员 <%s>' % from_addr)
    msg['To'] = _format_addr('管理员 <%s>' % to_addr)
    msg['Subject'] = Header('来自北京的Python程序员使用SMTP发来祝贺...', 'utf-8').encode()
    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()


def main():
    my_test()


if __name__ == '__main__':
    main()