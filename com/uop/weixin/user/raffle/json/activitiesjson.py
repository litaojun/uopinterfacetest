#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Created on 2017年11月7日
json 工具类
#https://www.cnblogs.com/wangyayun/p/6699184.html?utm_source=tuicool&utm_medium=referral
@author: li.taojun
'''
import json
def parseSignUpActivitiesJson(userSignActivjson):
    if userSignActivjson is not None and userSignActivjson != "":
          activitiesjson = json.loads(userSignActivjson)
          #if activitiesjson

def testa():
    a = {"a":"b","c":"d"}
    b = '{"a":"b","c":"d"}'
    js = json.dumps(a)
    print js
    jsa = json.loads(js)
    sign = jsa.has_key("a")
    x = jsa['c']
    print x,sign
    
if __name__ == '__main__':
    testa()