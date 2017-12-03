#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017年12月3日
http://python.jobbole.com/87805/
@author: ｌｉｔａｏｊｕｎ
'''
import dis
def test():
     x = [1, 2, 3]
     y = iter(x)
     z = iter(x)
     print next(y)
     print next(y)
     print next(z)
     print type(x)
     print type(y)
     
def testa():
    x = [1, 2, 3]
    dis.dis('for _ in x : pass')
from itertools import islice

class Fib:
    def __init__(self,max):
        self.prev = 0
        self.curr = 1
        self.max = max
 
    def __iter__(self):
        return self
 
    def next(self):
        value = self.curr
        if value > self.max:
            raise StopIteration
        print value
        self.curr += self.prev
        self.prev = value
        return value
    
def fib():
    prev, curr = 0, 1
    while True:
        yield curr
        prev, curr = curr, curr + prev
def testfib():
    f = fib()
    a = list(islice(f, 0, 10))
    print str(a)
if __name__ == '__main__':
    #test()
    testfib()
    t = Fib(100)
    lt = [x for x in t ]
    print str(lt)