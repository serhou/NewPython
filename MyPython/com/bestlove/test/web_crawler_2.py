# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib import request
from bs4 import BeautifulSoup
import socket

# ip代理的使用
def get_pro():
    user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
    header = {}
    header['User-Agent'] = user_agent
    url = 'http://www.xicidaili.com/nn/1'
    req = request.Request(url, headers=header)
    print('开始发送请求....')
    res = request.urlopen(req).read()
    print('请求完毕...')
    soup = BeautifulSoup(res, 'html.parser')
    print('开始解析网页...')
    ips = soup.find_all('tr')
    f = open('pro.txt', 'w')
    for x in range(1,len(ips)):
        ip = ips[x]
        tds = ip.find_all('td')
        ip_temp = tds[2].contents[0]+'\t'+tds[3].contents[0]+'\n'
        print('写入文件中...')
        f.write(ip_temp)
    print('写入文件完毕...')


def test_ip():
    socket.setdefaulttimeout(3)
    f = open('pro.txt')
    lines = f.readlines()
    proxys = []
    for i in range(0, len(lines)):
        ip = lines[i].strip('\n').split('\t')
        proxy_host = 'http://'+ip[0]+':'+ip[1]
        proxy_temp = {'http':proxy_host}
        proxys.append(proxy_temp)
    url = 'http://ip.chinaz.com/getip.aspx'
    for proxy in proxys:
        try:
            proxy_support = request.ProxyHandler(proxy)
            opener = request.build_opener(proxy_support)
            request.install_opener(opener)
            res = request.urlopen(url).read()
            print(res)
            print(proxy)
        except Exception as e:
            continue


def my_test():
    get_pro()
    test_ip()

def main():
    my_test()


if __name__ == '__main__':
    main()