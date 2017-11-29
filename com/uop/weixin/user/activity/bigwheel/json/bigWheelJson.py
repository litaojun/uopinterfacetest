#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017��11��29��

@author: li.taojun
'''

#大转盘活动提交请求json数据
def transUserBigWheelHttpJson(memberid="",activitiesid = ""):
    usersignactivities = {
                           "memberId":memberid,
                           "activitiesId":activitiesid
                         }
    return usersignactivities

#中奖后，提交地址
def transUserAwardHttpJson(orderId='',addressid=''):
    awardjson = {
                 "id":orderId,
                 "addressId":addressid
                }
#从大转盘抽奖提交后，从返回数据中提取orderId.  
def paserOrderIdFromJson(respse):
    orderid = respse.get("luckDrawResultInfo").get("orderId")
    return orderid
if __name__ == '__main__':
    pass