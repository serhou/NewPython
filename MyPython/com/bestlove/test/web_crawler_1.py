# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib import request
from bs4 import BeautifulSoup

'''
    简单爬取一个导航网站的网址
'''


def my_test():
    res = request.urlopen('http://www.2345.com/')
    res_str = res.read()
    soup = BeautifulSoup(res_str, 'html.parser')
    # BeautifulSoup 官方文档 http://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html
    dao_div = soup.find(attrs={'id':'nav'})  # 获取一个div
    dao_all = dao_div.find_all(attrs={'class':'menu-hd', 'name':'2'})  # 获取指定属性的tags
    for s in dao_all:
        ats = s.attrs
        print(ats['href'], s.string)

    '''
        爬取导航网站的网址
        http://www.sina.com.cn 新　浪
        http://www.sohu.com 搜　狐
        http://www.ifeng.com/ 凤 凰 网
        http://www.qq.com 腾 讯
        http://www.163.com 网　易
        http://www.baidu.com/index.php?tn=site888_3_pg 百　度
    '''


def main():
    my_test()


if __name__ == '__main__':
    main()