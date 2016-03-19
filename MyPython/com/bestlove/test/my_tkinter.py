# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *
import tkinter.messagebox as messagebox
'''
    Python 内置的TKinter可以满足基本的GUI程序的要求，如果是非常复杂的GUI程序，
    建议用操作系统原生支持的语言和库来编写
'''
# 输入文本
class Application2(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message', 'Hello, %s' % name)


# 简单退出按钮
class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text='Hello, World!')
        self.helloLabel.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()


def test_gui():
    app = Application()
    # 设置窗口标题
    app.master.title('Hello World')
    # 主消息循环
    app.mainloop()


def test_input():
    # 调用输入框
    app2 = Application2()
    # 设置窗口标题
    app2.master.title('你好，中国')
    # 主消息循环
    app2.mainloop()


def my_test():
    # test_gui()
    test_input()



def main():
    my_test()


if __name__ == '__main__':
    main()