#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017年12月3日
最简单的装饰器,装饰器和函数均无参数
http://blog.csdn.net/TangHuanan/article/details/45094497
@author: ｌｉｔａｏｊｕｎ
'''

import time
def decorator(fun):
    def wrapper():
        start = time.time()
        fun()
        runtime = time.time()-start
        print runtime
    return wrapper

def a():
    pass
@decorator
def do_something():
    for i in range(1000000):
        pass
    print "play game"
if __name__ == '__main__':
    do_something()
    decorator(do_something)()   #和直接do_something一致 