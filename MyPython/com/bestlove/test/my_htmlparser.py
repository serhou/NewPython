# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from html.parser import HTMLParser
from html.entities import name2codepoint

'''
    如果我们要编写一个搜索引擎，第一步是用爬虫把目标网站的页面抓下来，
    第二步就是解析HTML页面，看看里面的内容到底是新闻、图片还是视频。

    HTML本质上是XML的子集，但是HTML的语法没有XML那么严格，所以不能用
    标准的DOM或SAX来解析HTML。
    好在Python提供了HTMLParser来非常方便地解析HTML，只需要简单几行代码
'''


class MyHTMLParaser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('开始标签：%s, 属性：%s' % (tag, attrs))

    def handle_endtag(self, tag):
        print('结束标签：%s' % tag)

    def handle_startendtag(self, tag, attrs):
        print('开始结束标签：%s, 属性：%s' % (tag, attrs))

    def handle_data(self, data):
        print('数据：%s' % data)

    def handle_comment(self, data):
        print('注释：%s' % data)

    def handle_entityref(self, name):
        print('这是什么鬼？%s' % name)

    def handle_charref(self, name):
        print('又是什么鬼？%s' % name)



def my_test():
    parser = MyHTMLParaser()
    parser.feed('''<html>
    <head></head>
    <body>
    <!-- test html parser -->
        <p>Some <a href=\"#\">html</a>HTML&nbsp;tutorial...<br>END</p>
    </body></html>''')


def main():
    my_test()


if __name__ == '__main__':
    main()