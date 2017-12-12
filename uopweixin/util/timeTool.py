#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Created on 2017

@author: li.taojun
'''
import time
#timeStr = "2016-05-05 20:28:54"
#dateFormate = "%Y-%m-%d %H:%M:%S"
def strStrptime(timeStr="2016-05-05 20:28:54",dateFormate="%Y-%m-%d %H:%M:%S"):
    #转换成时间数组
    timeArray = time.strptime(timeStr, dateFormate)
    print(timeArray)
    return timeArray

#将时间转换成时间戳
def strStrpTimestamp(timeStr="2016-05-05 20:28:54",dateFormate="%Y-%m-%d %H:%M:%S"): 
    timearray = strStrptime(timeStr, dateFormate)
    timestamp = time.mktime(timearray)
    return timestamp

def strRepeatStrftime(timeStr="2016-05-05 20:28:54",fromdateFormate="%Y-%m-%d %H:%M:%S",todataformate ="%Y%m%d-%H:%M:%S"):
    #转换成时间数组
    timeArray = time.strptime(timeStr, "%Y-%m-%d %H:%M:%S")
    #转换成新的时间格式(20160505-20:28:54)
    dt_new = time.strftime("%Y%m%d-%H:%M:%S",timeArray)
    return dt_new

#将时间戳转换成时间
def timestampFtime(timestamp = 1462451334,formatdate = "%Y-%m-%d %H:%M:%S"):
    #转换成localtime
    time_local = time.localtime(timestamp)
    #转换成新的时间格式(2016-05-05 20:28:54)
    dt = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
    return dt

#按指定的格式获取当前时间
def getNowTime(formatedate = "%Y-%m-%d %H:%M:%S"):
    #获取当前时间,转换为时间戳
    time_now = int(time.time())
    print(time_now)
    #转换成localtime
    time_local = time.localtime(time_now)
    print(time_local)
    #转换成新的时间格式(2016-05-09 18:59:20)
    dt = time.strftime(formatedate,time_local)
    print(dt)
    return dt

if __name__ == '__main__':
    timestamp = getNowTime()
    print(timestamp)
