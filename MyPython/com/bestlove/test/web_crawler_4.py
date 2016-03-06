# !/usr/bin/env python3
# -*- coding:utf-8 -*-
from http.cookiejar import CookieJar
from urllib import request
import json
import socket
from bs4 import BeautifulSoup
import re
from datetime import datetime
import os
import uuid
import random

'''
    爬取汽车之家标致308S图片
'''

proxys = []
proxys.append({'http': 'http://115.159.100.31:80'})
proxys.append({'http': 'http://58.176.140.238:80'})
proxys.append({'http': 'http://119.188.94.145:80'})
proxys.append({'http': 'http://58.218.198.2:6666'})
proxys.append({'http': 'http://171.123.115.214:80'})
proxys.append({'http': 'http://117.83.72.214:80'})
user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0'
accept = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
accept_language = 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3'
accept_encoding = 'gzip, deflate, br'
connection = 'keep-alive'
header = {}
header['User-Agent'] = user_agent
header['Accept'] = accept
header['Accept-Language'] = accept_language
header['Accept-Encoding'] = accept_encoding
header['Connection'] = connection

#声明一个CookieJar对象实例来保存cookie
cookie = CookieJar()
#利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler=request.HTTPCookieProcessor(cookie)


def my_test(dynamic_url):
    socket.setdefaulttimeout(10)
    try:
        url = 'http://car.autohome.com.cn'+dynamic_url
        req = request.Request(url, headers=header)
        index = random.randint(0, 10)
        print('使用代理为：',proxys[index%6])
        proxy_support = request.ProxyHandler(proxys[index%6])
        opener = request.build_opener(proxy_support, handler)
        request.install_opener(opener)
        print('请求地址', url, '中...')
        res = request.urlopen(req).read()
        soup = BeautifulSoup(res, 'html.parser')
        print('解析网页中...')
        car_all2 = soup.find_all('script')[0]
        str1 = ''
        for s in car_all2:
            str1 = str(s)
        str2 = str1.split(';')
        str3 = str2[2].split('\'')
        str4 = str3[1]
        car_one = soup.find_all('img')
        car_img_addr = car_one[0].attrs['src']
        print('获取图片地址:', car_img_addr)
        str5 = datetime.now().strftime('%Y-%m-%d-%H-%M-%S-') +str(datetime.now().timestamp())
        request.urlretrieve(car_img_addr,'C:\\Users\\think\\Desktop\\test\\'+str5+'.jpg')
        print('已本地保存图片为：', str5+'.jpg')
        if str4 == dynamic_url:
            print('已下载完图集最后一张图片')
            return
        if str4 != '':
            my_test(str4)  # 回调进入下一页
        else:
            print('所有图片下载完毕')
            return

    except Exception as e:
        print(e)


def main():
    my_test('/photo/20668/1/2922636.html')  # 308S初始化页面
    # my_test('/photo/20718/1/2777412.html')  # 3008初始化页面
    # my_test('/photo/20106/1/2829322.html')  # 508初始化页面
    # my_test('/photo/series/21039/1/2858293.html')  # 宝马5系初始化页面


if __name__ == '__main__':
    main()