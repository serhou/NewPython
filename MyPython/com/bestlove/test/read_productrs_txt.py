# !/usr/bin/env python3
# -*- coding: utf-8 -*-

strs = []

def my_test():
    productrs = open('shuju.txt', 'r', encoding='utf-8')
    for line in productrs.readlines():
        strs.append(line.split('|')[0].strip())
    productrs.close()
    print(strs)

def main():
    my_test()


if __name__ == '__main__':
    main()