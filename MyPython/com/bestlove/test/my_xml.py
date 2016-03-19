# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from xml.parsers.expat import ParserCreate

'''
    操作XML有两种方法：DOM和SAX。DOM会把整个XML读入内存，解析为树，因此占用内存大，解析慢，
    优点是可以任意遍历树的节点。SAX是流模式，边读边解析，占用内存小，解析快，缺点是我们
    需要自己处理事件

    正常情况下，优先考虑SAX，因为DOM实在太占内存了

    在Python中使用SAX解析XML非常简洁，通常我们关系的事件是start_element, end_element和char_data,
    准备好这3个函数，然后就可以解析XML了
'''

class DefaultSAXHandler(object):

    def start_element(self, name, attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

    def end_element(self, name):
        print('sax:end_element: %s' % name)

    def char_data(self, text):
        print('sax:char_data: %s' % text)


def my_test():
    xml = r'''<?xml version="1.0"?>
    <ol>
        <li><a href="/python">Python</a></li>
        <li><a href="/java">Java</a></li>
    </ol>
    '''
    handler = DefaultSAXHandler()
    # 创建解析器
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(xml)
    # 生成XML，最简单有效的就是拼接字符串
    L = []
    L.append(r'<?xml version="1.0"?>')
    L.append(r'<root>')
    L.append('风居住的街道')
    L.append(r'</root>')
    print(''.join(L))



def main():
    my_test()


if __name__ == '__main__':
    main()