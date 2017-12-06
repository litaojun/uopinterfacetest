#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017

@author: li.taojun
'''
import requests
from com.uop.util.configurl import memeraddressurl,bigwheelurl,awaredurl
from com.uop.util.jsonTransform import transUopHttpHears
from com.uop.weixin.user.center.address.json.memberAddJonsParse import parseMemberDefalutAddJSON
from com.uop.weixin.user.activity.bigwheel.json.bigWheelJson import transUserBigWheelHttpJson,paserOrderIdFromJson,transUserAwardHttpJson
from com.uop.weixin.user.activity.raffle.cpr.userSignActivitiesCpr import checkSignUpActivitiesResultFormat
from com.uop.weixin.user.activity.raffle import parseActivitiesPointByRspJSON
from com.uop.weixin.user.raffle.cpr.httpsTest import hearder
class BigWheelService(object):
    '''
    classdocs
    '''
    userBigWheelurl = bigwheelurl
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
    
    #大转盘抽奖动作
    def userSignupActivities(self):
        jsonheart = transUopHttpHears(self.memberId,self.openid)

        userSignupActivitiesjson = transUserBigWheelHttpJson(self.memberId,
                                                             self.activitiesId)
        userBigWheelResultJson = requests.post(self.userBigWheelurl,
                                                 json=userSignupActivitiesjson,
                                                 headers = jsonheart)
    
    #大转盘去领奖动作 
    def userBigWheelAward(self):
        jsonheart = transUopHttpHears(self.memberId,self.openid)
        userBigResultJson = self.userSignupActivities()
        orderId = paserOrderIdFromJson(respse = userBigResultJson)
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