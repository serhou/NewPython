# !/usr/bin/env python3
# -*- coding:utf-8 -*-

from urllib import request
import json
import socket


def my_test():
    socket.setdefaulttimeout(10)
    proxys = []
    proxys.append({'http': 'http://223.223.182.59:80'})
    proxys.append({'http': 'http://115.159.123.204:80'})
    proxys.append({'http': 'http://182.254.150.120:80'})
    proxys.append({'http': 'http://122.96.59.104:80'})
    user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
    header = {}
    header['User-Agent'] = user_agent
    for id in range(0, 10, 1):
        try:
            url = 'http://chanyouji.com/api/trips/35214'+str(id)+'.json'
            req = request.Request(url, headers=header)
            print(url)
            proxy_support = request.ProxyHandler(proxys[id%4])
            opener = request.build_opener(proxy_support)
            request.install_opener(opener)
            res = request.urlopen(req).read()
            res_json = json.loads(res.decode('utf-8'))
            print(res_json['name'])
        except Exception as e:
            print(e)
            continue

def main():
    my_test()


if __name__ == '__main__':
    main()