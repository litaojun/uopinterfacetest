#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017

@author: li.taojun
'''

#大转盘活动提交请求json数据
def transUserBigWheelHttpJson(memberid="",activitiesid = ""):
    '''
       memberid  : 会员ID
       activitiesid : 大转盘活动ID
       return : 大转盘活动提交请求json数据
    '''
    usersignactivities = {
                           "memberId":memberid,
                           "activitiesId":activitiesid
                         }
    return usersignactivities

#中奖后，提交地址
def transUserAwardHttpJson(orderId='',addressid=''):
    '''
       orderId   :  大转盘中奖后，返回的订单ID
       addressid :  默认地址ID，或用户选择的地址ID
        return : 中奖后，提交地址请求json数据
    '''
    awardjson = {
                 "id":orderId,
                 "addressId":addressid
                }
    return awardjson
    
#从大转盘抽奖提交后，从返回数据中提取orderId.  
def paserOrderIdFromJson(respse):
    '''
       respse : 大转盘抽奖（中奖）提交后返回的json数据
       return : 中奖后的订单ID
    '''
    orderid = respse.get("luckDrawResultInfo").get("orderId")
    return orderid
if __name__ == '__main__':
    pass