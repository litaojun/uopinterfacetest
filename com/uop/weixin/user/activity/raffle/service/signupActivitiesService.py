#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017

@author: li.taojun
'''
import requests
from com.uop.util.configurl import memeraddressurl,signUpOpenActUrl
from com.uop.util.jsonTransform import transUopHttpHears
from com.uop.weixin.user.center.address.json.memberAddJonsParse import parseMemberDefalutAddJSON
from com.uop.weixin.user.activity.raffle.json.signUpActivitiesJsonParse import transUserSignupActivitiesHttpJson
from com.uop.weixin.user.activity.raffle.cpr.userSignActivitiesCpr import checkSignUpActivitiesResultFormat
from com.uop.weixin.user.activity.raffle import parseActivitiesPointByRspJSON
class SignUpActivitiesService(object):
    '''
    classdocs
    '''
    #非即开抽奖活动URL
    userSignupActivitiesurl = signUpOpenActUrl
    memberId = None
    openid = None
    activitiesId = None
    def __init__(self, memberId,openid,activitiesId):
        '''
        Constructor
        '''
        self.memberId = memberId
        self.openid = openid
        self.activitiesId = activitiesId
    
    #非即开抽奖动作
    def userSignupActivities(self):
        jsonheart = transUopHttpHears(self.memberId,self.openid)
        activityrspjson = requests.get(url=self.defaultAddress,headers = jsonheart)
        useraddressid = parseMemberDefalutAddJSON(activityrspjson)
        userSignupActivitiesjson = transUserSignupActivitiesHttpJson(self.memberId,
                                                                     self.activitiesId,
                                                                     useraddressid)
        userSignUpResultJson = requests.post(self.userSignupActivitiesurl,
                                             json=userSignupActivitiesjson,
                                             headers = jsonheart)
        return userSignUpResultJson
    
    #非即开抽奖中奖后获取订单,code信息
    def getOrderIdBySignUpResultJson(self,userSignUpResultJson):
        pass
    
    #非即开抽奖未中奖，获取code信息
    def getRspCodeBySignUpResultJson(self,userSignUpResultJson):
        pass 
    
    #获取非即开活动详情
    def getActivitiesById(self):
        jsonheart = transUopHttpHears(self.memberId,self.openid)
        activityrspjson = requests.get(url=self.defaultAddress,headers = jsonheart)
        return activityrspjson
        
    #获取非即开活动所需积分
    def getActivitiesPointByAid(self):
        activityrspjson = self.getActivitiesById()
        activitiesPoint = parseActivitiesPointByRspJSON(activityrspjson)
        return activitiesPoint

if __name__ == "__main__":
    a = SignUpActivitiesService("","","")
    b = SignUpActivitiesService("","","")
    sta = set()
    sta.add(b)
    sta.add(a)