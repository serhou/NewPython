# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import smtplib
from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.mime.multipart import MIMEMultipart

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def my_test():
    from_addr = input('From:')
    password = input('Password:')
    to_addr = input('To:')
    smtp_server = input('SMTP server:')
    # 邮件对象  利用MIMEMultipart就可以组合一个HTML和Plain，要注意指定subtype是alternative
    # msg = MIMEMultipart()
    msg = MIMEMultipart('alternative')  # 设置为这个时，可以既是plain又是html
    msg['From'] = _format_addr('Python程序员 <%s>' % from_addr)
    msg['To'] = _format_addr('管理员 <%s>' % to_addr)
    msg['Subject'] = Header('来自北京的Python程序员使用SMTP发来祝贺...', 'utf-8').encode()
    # 邮件正文是MIMEText
    msg.attach(MIMEText('我发给你一个文件...', 'plain', 'utf-8'))  # 当msg = MIMEMultipart('alternative')时，可以和html共存


    '''
        要把图片嵌入到邮件正文中，我们只需按照发送附件的方式，先把邮件作为附件添加进去，
        然后，在HTML中通过引用src="cid:0"就可以把附件作为图片嵌入了。如果有多个图片，
        给它们依次编号，然后引用不同的cid:x即可。
    '''
    msg.attach(MIMEText('<html><body><h1>我发给你一片枫叶森林...</h1><br><h3>邮件可能被加密了</h3><img src="cid:0"/></body></html>', 'html', 'utf-8'))  # 当msg = MIMEMultipart('alternative')时，可以和plain共存

    with open('1.jpg', 'rb') as f:
        # 设置附件的MIME和文件名，这里是jpeg类型
        mime = MIMEBase('image', 'jpeg', filename='fengye.jpg')
        # 加上必要的头信息
        mime.add_header('Content-Disposition', 'attachment', filename='fengye.jpg')
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')
        # 把附件的内容读进来
        mime.set_payload(f.read())
        # 用Base64编码
        encoders.encode_base64(mime)
        # 添加到MIMEMultipart
        msg.attach(mime)
    server = smtplib.SMTP(smtp_server, 25)
    # 创建SSL安全连接，加密邮件
    server.starttls()
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()


def main():
    my_test()


if __name__ == '__main__':
    main()