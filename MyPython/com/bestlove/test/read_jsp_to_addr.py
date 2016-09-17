# !/usr/bin/env python3
# -*- coding: utf-8 -*-



def my_test():
    jsps = open('jsp.txt', 'r', encoding='utf-8')
    for line in jsps.readlines():
        print(('/eweb/WebContent/WEB-INF/zh_CN/query/TransJnlQry/'+line).strip('\r\n'))
    jsps.close()
    jsps2 = open('jsp2.txt', 'r', encoding='utf-8')
    for line in jsps2.readlines():
        print(('/eweb/WebContent/WEB-INF/zh_CN/query/TransJnlQry/Edraft/'+line).strip('\r\n'))
    jsps2.close()


def main():
    my_test()


if __name__ == '__main__':
    main()