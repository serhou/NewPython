# !/usr/bin/env python3
# -*- coding:utf-8 -*-

import base64

'''
    Base64是一种用64个字符来表示任意二进制数据的方法
    Base64编码会把3个字节的二进制数据编码为4字节的文本数据，长度增加33%,
    好处是编码后的文本数据可以再邮件正文、网页等直接显示
    如果要编码的二进制数据不是3的倍数，最后会剩下1个或2个字节，Base64用\x00
    字节在末尾补足后，再在编码的末尾加上1个或2个=号，表示不了多少字节，
    解码的时候会自动去掉
'''

def my_test():
    b = base64.b64encode(b'binary\x00string')
    print(b)
    b2 = base64.b64decode(b'YmluYXJ5AHN0cmluZw==')
    print(b2)
    # 由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，所以又一种
    # "urlsafe"的base64编码实际就是把字符+和/分别变成-和_
    b3 = base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
    print(b3)
    b4 = base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
    print(b4)
    b5 = base64.urlsafe_b64decode('abcd--__')
    print(b5)
    '''
        # Base64是一种通过查表的编码方法，不能用于加密，即使使用自定义的编码表也不行
        # Base64适用于小段内容的编码，比如数字证书签名，Cookie的内容
        # 由于=字符也可能出现在Base64编码中，但=用在URL、Cookie里面会造成歧义，
        # 所以很多Base64编码后会把=去掉，解码时把字符串加上=，变成4的倍数就可以正常解码了
    '''


def main():
    my_test()


if __name__ == '__main__':
    main()