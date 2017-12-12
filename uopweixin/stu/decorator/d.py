#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017年12月3日

@author: ｌｉｔａｏｊｕｎ
'''
import time
def decorator(max):
    def _decorator(fun):
        def wrapper(*args, **kwargs):
            start = time.time()
            for i in xrange(max):
                fun(*args, **kwargs)
            runtime = time.time()-start
            print runtime
        return wrapper
    return _decorator
@decorator(2)
def do_something(name):
    for i in range(1000000):
        pass
    print "play game " + name
if __name__ == '__main__':
    do_something("san guo sha")
    decorator(2)(do_something)("san guo sha")  #和直接do_something("san guo sha")一致 