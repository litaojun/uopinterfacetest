#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017年12月3日
目标函数带固定参数的装饰器
@author: ｌｉｔａｏｊｕｎ
'''
import time
def decorator(fun):
    def wrapper(name):
        start = time.time()
        fun(name)
        runtime = time.time()-start
        print runtime
    return wrapper
@decorator
def do_something(name):
    for i in range(1000000):
        pass
    print "play game " + name
if __name__ == '__main__':
    do_something("litaojun")
    #decorator(do_something)("litaojun")  #和直接do_something("litaojun")一致 