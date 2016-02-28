# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import time, threading, multiprocessing


'''
    Python的标准库提供了两个模块：_thread和threading，_thread是低级模块，
    threading是高级模块，是对_thread进行了封装。绝大多数情况下，我们只需要使用
    threading这个高级模块

    启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行

    多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，
    互不影响，而多线程中，所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改，
    因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了。

    这就是产生了线程安全和线程不安全问题，线程安全效率低，线程不安全效率高
'''


# 假设这是你的银行存款：
balance = 0
# 上锁
lock = threading.Lock()
def change_it(n):
    # 先存后取，结果应该为0
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        # 先要获取锁
        lock.acquire()
        try:
            # 可以开心的改了：
            change_it(n)
        finally:
            # 改完了一定要释放锁
            lock.release()


# 写个死循环
def loop2():
    x = 0
    while True:
        x = x^1
        print(x)


def my_test3():
    for i in range(multiprocessing.cpu_count()):
        print('我是%s核CPU....' % multiprocessing.cpu_count())
        t = threading.Thread(target=loop2())
        t.start()



def my_test2():
    t1 = threading.Thread(target=run_thread, args=(5,))
    t2 = threading.Thread(target=run_thread, args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(balance)

    '''
        我们定义一个共享变量balance,初始值为0，并且启动两个线程，先存后取，理论上结果为0，
        但是，由于线程的调度是有操作系统决定的，当t1,t2交替执行时，只要循环次数够多，
        balance的结果就不一定是0了

        所以我们必须确保一个线程在修改balance的时候，别的线程一定不能改
        如果我们要确保balance计算正确，就要给change_it()上一把锁
        当某个线程开始执行change_it()时，我们说该线程因为获得了锁，
        因此其他线程不能同时执行change_it()，只能等待，直到锁被释放后，获得该锁以后才能改。
        由于锁只有一个，无论多少线程，同一时刻最多只有一个线程持有该锁，所以，不会造成修改的冲突。
        创建一个锁就是通过threading.Lock()来实现

        当多个线程同时执行lock.acquire()时，只有一个线程能成功地获取锁，然后继续执行代码，
        其他线程就继续等待直到获得锁为止。

        获得锁的线程用完后一定要释放锁，否则那些苦苦等待锁的线程将永远等待下去，成为死线程。
        所以我们用try...finally来确保锁一定会被释放。

        锁的好处就是确保了某段代码只能由一个线程从头到尾完整地执行，坏处当然也很多，首先是阻止了
        多线程并发执行，包含锁的某段代码实际上只能以单线程模式执行，效率就大大地下降了。
        其次，由于可以存在多个锁，不同的线程持有不同的锁，并试图获取对方持有的锁时，可能会造成死锁，
        导致多个线程全部挂起，既不能执行，也无法结束，只能靠操作系统强制终止。

    '''


    '''
        多核CPU
        如果写一个死循环的话，一个死循环线程会100%占用一个CPU,
        如果写两个死循环线程，在多核CPU中，可以监控到到会占用200%的CPU，
        也就是占用两个CPU核心
        要想把N核CPU的核心全部跑满，就必须启动N个死循环线程。

        启动与CPU核心数量相同的N个线程，在4核CPU上可以监控到CPU占用率仅有102%，
        也就是仅使用了一核。

        但是用C、C++或者Java来改写相同的死循环，直接就可以把全部核心跑满，4核就跑到400%，
        8核就跑到800%,为什么Python不行呢？

        因为Python的线程虽然是真正的线程，但是解释器执行代码时，有一个GIL锁，
        Global Interpreter Lock，任何Python线程执行前，必须先得获取GIL锁，然后，
        每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行。
        这个GIL全局锁实际上把所有线程的执行代码都给上了锁，所以多线程在Python中只能交替执行，
        即使100个线程跑在100核的CPU上，也只能用到1核。

        GIL是Python解释器设计的历史遗留问题，通常我们用的解释器是官方实现的CPython，
        要真正利用多核，除非重写一个不带GIL的解释器。

        所以，在Python中，可以使用多线程，但不要指望能有效利用多个。如果一定要通过多线程
        利用多个，那只能通过C扩展来实现，不过这样就失去了Python简单易用的特点。

        不过，也不用过于担心，Python虽然不能利用多线程实现多核任务，但可以通过多进程实现
        多核任务。多个Python进程有各自独立的GIL锁，互不影响。

        Python解释器由于设计时由GIL全局锁，导致多线程无法利用多核。
        多线程并发在Python中就是一个美丽的梦。
    '''


# 新线程执行的代码
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n+1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % (threading.current_thread().name))


def my_test():
    print('thread %s is running...' % threading.current_thread().name)
    t = threading.Thread(target=loop, name='LoopThread')
    t.start()
    t.join()
    print('thread %s ended....' % threading.current_thread().name)

    '''
        由于任何进程默认就会启动一个线程，我们把该线程称为主线程，主线程又可以启动新的线程，
        Python的threading模块有个current_thread()函数，它永远返回当前线程的实例。
        主线程实例的名字叫MainThread，子线程的名字再创建时指定，我们用LoopThread命名子线程。
        名字仅在打印时用来显示，完全没有其他意义，如果不起名字，Python就会自动给线程命名为：
        Thread-1，Thread-2....
    '''


def main():
    my_test()
    my_test2()
    my_test3()


if __name__ == '__main__':
    main()