# !/usr/bin/env python3
# -*- coding:utf-8 -*-

from datetime import datetime, timedelta, timezone
'''
    datetime是Python处理日期和时间的标准库
    注意到datetime时模块，datetime模块还包含一个datetime类。
'''


def get_cur_time():
    now = datetime.now()  # 获取当前datetime
    print(now)
    print(type(now))
    print(now.timestamp())


def get_every_time():
    dt = datetime(2014, 2, 15, 18, 34)  # 用指定日期时间创建datetime
    print(dt)
    # datetime转换为timestamp
    tt = dt.timestamp()  # 把timestamp转换为datetime
    print(tt)
    # timestamp转换为datetime
    t = 1273848400.127343
    print(datetime.fromtimestamp(t))
    '''
        注意到timestamp是一个浮点数，它没有时区的概念，而datetime是有时区的。
        上述转换都是在timestamp和本地时间做转换
        本地时区是指当前操作系统设定的时区
        UTC
        我们把1970年1月1日00:00:00 UTC+00:00时区的时刻称为epoch time,
        记为0（1970年以前的时间timestamp为负数），当前时间就是相对于epoch time
        的秒数，称为timestamp

        北京时间是 timestamp = 0 = 1970-1-1 08:00:00 UTC+8:00
        可见timestamp的值与时区毫无关系，因为timestamp一旦确定，其UTC时间就确定了，
        转换到任意时区的时间也是完全确定的，这就是为什么计算机存储的当前时间是以
        timestamp表示的，因为全球各地的计算机在任意时刻的timestamp都是完全相同的（假定时间已校准）。

        注意Python的timestamp是一个浮点数。如果有小数位，小数位表示毫秒数。

        某些编程语言（如Java和JavaScript）的timestamp使用整数表示毫秒数，这种情况下只需要把timestamp
        除以1000就得到Python的浮点表示方法。
    '''
    # timestamp也可以直接被转换到UTC标准时区的时间
    print(datetime.utcfromtimestamp(t))  # 格林威治标准时间UTC
    # str 转换为datetime
    cday = datetime.strptime('2014-05-22 18:45:53', '%Y-%m-%d %H:%M:%S')
    print(type(cday), cday)  # 注意转换后的datetime是没有时区信息的
    # datetime转换为str
    cur_time = datetime.now()
    time2str = cur_time.strftime('%a, %b %d %H:%M')
    time2str2 = cur_time.strftime('%Y/%m/%d %A %H:%M:%S')
    print(type(time2str), time2str)
    print(type(time2str2), time2str2)
    # datetime加减 可以直接用+和-运算符，需要导入timedelta类
    my_time = cur_time + timedelta(hours=10)  # 当前时间加10个小时
    print(my_time)
    my_time2 = cur_time -timedelta(days=3)  # 当前时间减3天
    print(my_time2)
    my_time3 = cur_time + timedelta(weeks=3,minutes=30,seconds=10)
    print(my_time3)
    # 本地时间转换为UTC时间 timezone
    tz_utc_8 = timezone(timedelta(hours=8))  # 创建时区UTC+8:00
    print(datetime.now())
    tz2 = dt.replace(tzinfo=tz_utc_8)
    print(tz2)
    # 时区转换 我们可以先通过utcnow()拿到当前的UTC时间，再转换为任意时区的时间
    utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
    print(utc_dt)  # 拿到UTC时间并强制设置时区为UTC+0:00
    # astimezone()将转换时区为北京时间
    bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
    print(bj_dt)
    # 转换为东京时间
    tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
    print(tokyo_dt)
    # 将北极时间转换为东京时间
    tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
    print(tokyo_dt2)
    '''
        时区转换的关键在于，拿到一个datetime时，要获知其正确的时区，然后强制设置时区，作为基准时间。

        利用带时区的datetime，通过astimezone()方法，可以转换到任意时区。

        注：不是必须从UTC+0:00时区转换到其他时区，任何带时区的datetime都可以正确转换，例如上述bj_dt到tokyo_dt的转换。

        datetime表示的时间需要时区信息才能确定一个特定的时间，否则只能视为本地时间。

        如果要存储datetime，最佳方法是将其转换为timestamp再存储，因为timestamp的值与时区完全无关。
    '''



def my_test():
    get_cur_time()
    get_every_time()


def main():
    my_test()


if __name__ == '__main__':
    main()