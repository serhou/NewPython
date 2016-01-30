# -*- coding: utf-8 -*-

# 第三方库

'''
   处理图片的库:Pillow
    其他第三方库还有MySQL的驱动：mysql-connector-python
    用于科学计算的NumPy库
    用于生成文本的模板工具Jinja2等等
'''

from PIL import Image
import sys

def image1():
    im = Image.open('vim.jpg')
    print(im.format,im.size,im.mode) # JPEG (1306, 1909) RGB
    im.thumbnail((200,100))
    im.save('thumb.jpg','JPEG')
    th = Image.open('thumb.jpg')
    print(th.format,th.size,th.mode)
    print(sys.path)
    # 导入模块 Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块
    # 直接修改sys.path，添加要搜索的目录 这种方法是在运行时修改，运行接受后无效
    # sys.path.append('/Users/michael/my_py_scripts')
    # 第二种方法是设置环境变量PYTHONPATH，该环境变量的内容会被自动添加到模块搜索路径中。设置方式与设置Path环境变量类似。注意只需要添加你自己的搜索路径，Python自己本身的搜索路径不受影响。

def my_test():
    image1()


def main():
    my_test()


if __name__ == '__main__':
    main()