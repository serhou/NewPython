# !/usr/bin/env python3
# -*- coding:utf-8 -*-

from urllib import request
import json
import socket
from bs4 import BeautifulSoup
import re
from datetime import datetime
import os
import uuid

'''
    爬取汽车之家标致308S图片
'''

proxys = []
proxys.append({'http': 'http://223.223.182.59:80'})
proxys.append({'http': 'http://115.159.123.204:80'})
proxys.append({'http': 'http://182.254.150.120:80'})
proxys.append({'http': 'http://122.96.59.104:80'})
user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
header = {}
header['User-Agent'] = user_agent


def my_test(dynamic_url):
    socket.setdefaulttimeout(10)
    try:
        url = 'http://car.autohome.com.cn'+dynamic_url
        req = request.Request(url, headers=header)
        for id in range(0, 1, 1):
            proxy_support = request.ProxyHandler(proxys[id%4])
            opener = request.build_opener(proxy_support)
            request.install_opener(opener)
        res = request.urlopen(req).read()
        soup = BeautifulSoup(res, 'html.parser')
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
    # my_test('/photo/20668/1/2922636.html')  # 308S初始化页面
    # my_test('/photo/20718/1/2777412.html')  # 3008初始化页面
    # my_test('/photo/20106/1/2829322.html')  # 508初始化页面
    my_test('/photo/series/21039/1/2858293.html')  # 宝马5系初始化页面


if __name__ == '__main__':
    main()