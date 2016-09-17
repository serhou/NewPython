# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from xml.parsers.expat import ParserCreate
import io

prdtrs = []

class DefaultSAXHandler(object):

    def start_element(self, name, attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))
        if attrs['name']!='viewName' :
            if attrs['name']!='isBatch':
                if attrs['name']!='viewMap':
                    if attrs['name']!='listName':
                        prdtrs.append(attrs['name'])
    def end_element(self, name):
        print('sax:end_element: %s' % name)

    def char_data(self, text):
        print('sax:char_data: %s' % text)


def my_test():
    xml = open('productrs.xml', 'r', encoding='utf-8')
    productrs = xml.read()
    handler = DefaultSAXHandler()
    # 创建解析器
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    productrsxml = parser.Parse(productrs)
    print(productrsxml)
    xml.close()
    print('========================')
    print(prdtrs)




def main():
    my_test()


if __name__ == '__main__':
    main()