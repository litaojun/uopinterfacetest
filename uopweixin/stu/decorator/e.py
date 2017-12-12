#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017年12月3日
装饰器类
@author: ｌｉｔａｏｊｕｎ
'''
import time
import functools 

class decorator(object):
    def __init__(self, max):
        self.max = max
        self.count = 0
    def __call__(self, fun):
        self.fun = fun
        return self.call_fun

    def call_fun(self, *args, **kwargs):
        self.count += 1
        if ( self.count == self.max):
            print "%s run more than %d times"%(self.fun.__name__, self.max)
        elif (self.count<self.max):
            self.fun(*args, **kwargs)
        else:
            pass

@decorator(10)
def do_something():
    print "play game"
@decorator(15)
def do_something1():
    print "play game 1"
    for i in xrange(20):
        do_something()
        do_something1()
if __name__ == '__main__':
    pass