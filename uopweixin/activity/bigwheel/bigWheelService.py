#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017

@author: li.taojun
'''
import requests
from uopweixin.util.configurl import memeraddressurl,bigwheelurl,awaredurl
from uopweixin.util.jsonTransform import transUopHttpHears
from uopweixin.center.address.ParseMemberAddJons import parseMemberDefalutAddJSON
from uopweixin.activity.bigwheel.bigWheelJson import transUserBigWheelHttpJson,paserOrderIdFromJson,transUserAwardHttpJson
from uopweixin.activity.raffle.userSignActivitiesCpr import checkSignUpActivitiesResultFormat
from uopweixin.activity.raffle import parseActivitiesPointByRspJSON
# from uopweixin.raffle.httpsTest import hearder
class BigWheelService(object):
    '''
                       大转盘抽奖
    '''
    userBigWheelurl = bigwheelurl
    memberId = None
    openid = None
    activitiesId = None
    def __init__(self, memberId,openid,activitiesId):
        '''
            memberId ： 会员ID
            openid ： 微信OPenid
            activitiesId : 大转盘活动ID
        '''
        self.memberId = memberId
        self.openid = openid
        self.activitiesId = activitiesId
    
    #大转盘抽奖动作
    def userSignupActivities(self):
        jsonheart = transUopHttpHears(self.memberId,self.openid)

        userSignupActivitiesjson = transUserBigWheelHttpJson(self.memberId,
                                                             self.activitiesId)
        userBigWheelResultJson = requests.post(self.userBigWheelurl,
                                                 json=userSignupActivitiesjson,
                                                 headers = jsonheart)
        return userBigWheelResultJson
    
    #获取大转盘抽奖中奖后，从返回数据中获取相关信息(订单ID,返回码等）
    def getOrderIdFromBigWheelResultJson(self,bigWheelResultJson):
        '''
            bigWheelResultJson  :  大转盘抽奖动作中奖后返回的json数据
        '''
        userBigResultJson = self.userSignupActivities()
        orderId = paserOrderIdFromJson(respse = userBigResultJson)
        return orderId
    
    #获取大转盘抽奖未中奖(返回码）
    def getRetcodeFromBigWheelResultJson(self,bigWheelResultJson):
        '''
            bigWheelResultJson  :  大转盘抽奖动作中奖后返回的json数据
        '''
        pass 
    
    
    #大转盘去领奖动作 
    def userBigWheelAward(self,orderId):
        '''
            orderId  : 大转盘抽奖动作中奖后返回的json数据中的orderId
        '''
        jsonheart = transUopHttpHears(self.memberId,self.openid)
        useraddrspjson = requests.get(url=self.defaultAddress,headers = jsonheart)
        useraddressid = parseMemberDefalutAddJSON(useraddrspjson)
        awardJson = transUserAwardHttpJson(orderId,useraddressid)
        awardResultjson = requests.post(url=awaredurl,json=awardJson,headers=jsonheart)
        return awardResultjson
     
    #根据大转盘活动ID获取活动详情
    def getActivitiesByID(self):
        jsonheart = transUopHttpHears(self.memberId,self.openid)
        activityrspjson = requests.get(url=self.userBigWheelurl,headers = jsonheart)
        return activityrspjson
    
    #获取大转盘活动抽奖所需积分
    def getActivitiesPointByAid(self):
        activityrspjson = self.getActivitiesByID()
        activitiesPoint = parseActivitiesPointByRspJSON(activityrspjson)
        return activitiesPoint
    
if __name__ == '__main__':
    pass