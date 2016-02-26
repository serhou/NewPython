# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import shutil

'''
    CentOS 下运行结果

    >>> import os

    >>> os.name
    'posix'

    >>> os.uname()

    posix.uname_result(sysname='Linux', nodename='localhost.localdomain', release='2.6.32-573.18.1.el6.x86_64', version='#1 SMP Tue Feb 9 22:46:17 UTC 2016', machine='x86_64')
    >>>

'''




def shutil_test():
    # 利用Python的特性来过滤文件，列出当前目录下所有目录，只需一行代码
    d = [x for x in os.listdir('.') if os.path.isdir(x)]
    print(d)
    # 要列出所有.py文件，也只需一行代码
    f = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
    print(f)
    # 拷贝文件 以lambda.py为例
    shutil.copyfile('lambda.py', 'lambda.txt')




def my_test():
    name = os.name  # 获取操作系统名字 'posix' 是Linux，Unix，'nt'是Windows系统
    print(name)
    # print(os.uname())  # Windows 不支持uname()函数
    print(os.environ)  # 操作系统中定义的环境变量，全部都保存在os.environ这个变量中
    # 获取某个环境变量的值，可以调用os.environ.get('key')
    path = os.environ.get('PATH')
    print(path)
    # 操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，需要特别注意
    print(os.path.abspath('.'))  #查看当前目录的绝对路径
    # 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来
    my_path = os.path.join(os.path.abspath('.'), 'testdir')  # 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分割符
    print(my_path)
    os.mkdir('testdir')  # 如果文件目录存在，会报：FileExistsError: [WinError 183] 当文件已存在时，无法创建该文件。: 'testdir'
    os.rmdir('testdir')  # 如果文件目录不存在，会报：FileNotFoundError: [WinError 2] 系统找不到指定的文件。: 'testdir
    # 同样道理，要拆分路径时，也不要直接取拆字符串，而要通过os.path.split()函数
    # 这样可以把一个路径拆分为两个部分，后一部分总是最后级别的目录或文件名
    my_path2 = os.path.split(os.path.abspath('.'))
    print(my_path2)
    # os.path.splittext()可以直接让你得到文件扩展名，很多时候非常方便
    my_path3 = os.path.splitext(os.path.abspath('.'))
    print(my_path3)
    my_path4 = os.path.splitext('G:\\NewPython\\MyPython\\com\\bestlove\\test\\MixIn.py')
    print(my_path4)
    my_path5 = os.path.splitext('MixIn.py')
    print(my_path5)
    # 这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只是对字符串进行操作
    # 文件操作使用下面的函数
    # os.rename('123.html', '123.txt')  # 当前目录下有123.html这个文件，不然会报错
    # os.remove('123.txt')

    '''
        但是复制文件的函数在os模块中并不存在，原因是复制文件并非由操作系统提供的系统调用。
        理论上讲，我们通过IO完全可以完成文件复制，只不过要多写很多代码

        而Python中的shutil模块提供了copyfile()函数，我们还可以再shutil模块中找到很多实用
        的函数，它们可以看做是对os模块的补充
    '''

    shutil_test()


def main():
    my_test()


if __name__ == '__main__':
    main()