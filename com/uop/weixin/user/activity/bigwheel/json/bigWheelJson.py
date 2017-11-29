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


def transUserAwardHttpJson(orderId='',addressid=''):
    awardjson = {
                 "id":orderId,
                 "addressId":addressid
                }

def paserOrderIdFromJson(respse):
    orderid = respse.get("luckDrawResultInfo").get("orderId")
    return orderid
if __name__ == '__main__':
    pass