#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017年12月3日
目标函数带不固定参数的装饰器
@author: ｌｉｔａｏｊｕｎ
'''
import time
def decorator(fun):
    def wrapper(*args, **kwargs):
        start = time.time()
        fun(*args, **kwargs)
        runtime = time.time()-start
        print runtime
    return wrapper
@decorator
def do_something(name):
    for i in range(1000000):
        pass
    print "play game " + name

@decorator
def do_something2(user, name):
    for i in range(1000000):
        pass
    print user+" play game " + name

if __name__ == '__main__':
    do_something("san guo sha")
    #decorator(do_something)("san guo sha")  #和直接do_something("san guo sha")一致 
    do_something2("wang xiao er","san guo sha")
    #decorator(do_something)("wang xiao er","san guo sha")  #和直接do_something("wang xiao er","san guo sha")一致 