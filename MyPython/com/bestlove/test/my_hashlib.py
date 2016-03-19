# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib

'''
    Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等。
    摘要算法又称为哈希算法、散列算法。它通过一个函数，把任意长度的数据转换为一个
    长度固定的数据串（通常用16进制的字符串表示）

    摘要算法就是通过摘要函数f()对任意长度的数据data计算出固定长度的摘要digest,
    目的是为了发现原始数据是否被人篡改过。

    摘要算法之所以能指出数据是否被篡改过，就是因为摘要函数是一个单向函数，计算f(data)
    很容易，但是通过digest反推data却非常困难。而且，对原始数据做一个bit的修改，
    都会导致计算出的摘要完全不同。

    摘要算法常用于比较两个文件是否一样如，WinRAR这个压缩文件里面都会显示摘要算法的值，
    我们可以通过对比摘要值来判定两个文件是否相同

    摘要算法的另外一个重要应用方向就是对用户密码进行加密，由于摘要算法是单向函数，
    通过计算后的值往往不可逆，所以存储在数据库会更安全。

    但采用MD5存储口令是否就一定安全呢？也不一定。假设黑客已经拿到了存储MD5口令的数据库。
    暴力破解费时费力，真正的黑客不会这么干。而用户通常会喜欢使用123456,88888888,password
    这样简单的口令，于是，黑客可以事先计算出这些常用口令的MD5值，这样无需破解，只要对比数
    据库的MD5，就可以轻松获取用户的明文口令。还有一种俗称撞库的方式来破解的，
    就是通过已经得到用户的邮箱和密码的数据，来与经过新得到的经过加密数据库进行比对，
    来达到破解目的的方法。前一段时间，阿里的被撞库事件就是一个典型的例子，发生这样的情况
    就是基于用户们太懒了，所有的账号密码都是喜欢设置为相同的，导致一旦一个注册网站的数据库
    遭到泄露都会可能影响到其他与这个网站使用相同邮箱相同密码的网站被撞库的风险。

    所以基于以上情况，网站的设计者，软件开发者都一般都要通过对用户输入的原始口令加一个复杂的
    字符串后再进行加密，俗称“加盐”。经过Salt处理的MD5口令，只要Salt不被黑客知道，即使用户输入
    简单口令，也很难通过MD5反推出明文口令

    如果两个用户都使用了相同的简单口令如123456，在数据库中，将存储两条相同的MD5值，这说明这两个
    用户的口令是一样的。如果假定用户无法修改登录名，且用户名唯一，就可以通过把登录名最为Salt的
    一部分来计算MD5，从而实现相同口令的用户也存储不同的MD5。

    最好的方式是将用户的登录名也经过MD5加密后再存储数据库，增加安全性。但性能也是要考虑的。

    另外注意，摘要算法不是加密算法，不能用于加密（因为无法通过摘要反推明文），只能用于防篡改。
    加密算法往往都是可以反推的，往往应用于数据传输过程中的加密。

'''

# 另一种常见的摘要算法是SHA1，调用SHA1和调用MD5完全类似
def test_sha1():
    sha1 = hashlib.sha1()
    sha1.update('问一声海鸥，你飞来飞去有何求？'.encode('utf-8'))
    print(sha1.hexdigest())  # SHA1的结果是160 bit 字节，通常用一个40位的16进制字符串表示
    '''
        比SHA1更安全的算法是SHA256和SHA512,不过越安全的算法不仅越慢，而且摘要长度更长

        有没有可能两个不同的数据通过某个摘要算法得到了相同的摘要，完全有可能，
        因为任何摘要算法都是把无限多的数据集合映射到一个有限的集合中。这种情况称为碰撞。

        摘要相同的情况并非不可能出现，但是要想出现非常困难。
    '''



# 以常见的摘要算法MD5为例，计算出一个字符串的MD5值
def test_md5():
    md5 = hashlib.md5()
    md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
    print(md5.hexdigest())
    # 如果数据量很大，可以分块多次调用update()，最后计算的结果是一样的
    mmdd5 = hashlib.md5()
    mmdd5.update('how to use md5 '.encode('utf-8'))
    mmdd5.update('in python hashlib?'.encode('utf-8'))
    print(mmdd5.hexdigest())  # 得到的结果与上面的一样，注意空格。
    '''
        MD5是最常见的摘要算法，速度很快，生成结果是固定的128bit字节，
        通常用一个32位的16进制字符串表示
    '''


def my_test():
    test_md5()
    test_sha1()


def main():
    my_test()


if __name__ == '__main__':
    main()