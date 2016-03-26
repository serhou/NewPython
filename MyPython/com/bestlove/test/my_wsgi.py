# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# 最简单的网页


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    # return [b'<h1>Hello, World!</h1><h3>Welcome to China!</h3>']
    body = '<head><meta charset="utf-8"></head><h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or '中国')
    return [body.encode('utf-8')]