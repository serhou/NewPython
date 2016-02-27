# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# 序列化  我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling,
# 而把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling
# Python 提供了pickle模块来实现序列化

import pickle


def my_test():
    d = dict(name='张三丰', age=99, score=100)
    # pickle.dumps()方法把任意对象序列化成一个bytes，
    # 然后，就可以把这个bytes写入文件或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object
    b = pickle.dumps(d)
    print(b)
    # 将对象写入文件
    w = open('lambda.txt', 'wb')
    pickle.dump(d, w)
    w.close()
    # 当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes,然后用pickle.loads()方法反序列化出对象
    # 也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象
    r = open('lambda.txt', 'rb')
    d2 = pickle.load(r)
    r.close()
    print(d2)  # 变量的内容又回来了，这个变量和原来的变量是完全不相干的对象，只是内容相同而已

    '''
    pickle的问题和所有其他编程语言特有的序列化问题一样，就是它只能用于Python，
    并且可能不同版本的Python彼此都不兼容，因此，只能用pickle保存那些不重要的数据，不能成功地反序列化也没关系

    '''


def main():
    my_test()


if __name__ == '__main__':
    main()