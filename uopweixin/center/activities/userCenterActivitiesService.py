#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017

@author: li.taojun
'''

import requests
from uopweixin.util.configurl import userActiviesUrl
from uopweixin.util.jsonTransform import transUopHttpHears
# from com.uop.weixin.user.center.address.json.memberAddJonsParseport parseMemberDefalutAddJSON
# from com.uop.weixin.user.activity.raffle.json.signUpActivitiesJsonParse import transUserSignupActivitiesHttpJson
from uopweixin.activity.raffle.userSignActivitiesCpr import checkSignUpActivitiesResultFormat
from uopweixin.center.activities.ParseCenterActivitiesJson import parseActivitiesStatus,parseActivitiesIdFromJson,parseMyActivitiesIDFromJson
import json
class PersonalActiviesService(object):
    '''
    classdocs
    '''
    #userSignupActivitiesurl = signUpOpenActUrl
    memberId = None
    openid = None
    def __init__(self, memberId,openid):
        '''
        Constructor li.taojun
        '''
        self.memberId = memberId
        self.openid = openid
        self.userActiviesUrl = userActiviesUrl
        
    #获取我的活动列表
    def userActivies(self):
        jsonheart = transUopHttpHears(self.memberId,self.openid)
        actjson = {"memberId":self.memberId,"page":1,"limit":10}
        activityrspjson = requests.post(url=self.userActiviesUrl,json = actjson,headers = jsonheart,verify=False)
        return activityrspjson
    
    #根据活动ID获取我的活动中信息
    def getMyActivitiesByID(self,activitiesId = "",activityrspjson=""):
#       actjson = self.userActivies()
        myactivities = parseMyActivitiesIDFromJson(activityrspjson,activitiesId)
        return myactivities
    
    #获取活动状态
    def getMyActivitiesStatus(self,activitiesId):
        myactivities = self.getMyActivitiesByID(activitiesId)
        actstatus = parseActivitiesStatus(myactivities)
        return actstatus
        
    #得到活动ID列表
    def getActivitiesidList(self):
        actjson = self.userActivies()
        actidls = parseActivitiesIdFromJson(response = json.loads(actjson.text))
        return actidls
    
    
    #检查活动ID是否存在
    def checkActivitiesExsit(self,activiId = ""):
        sign = False
        actidls = self.getActivitiesidList()
        if activiId in actidls:
            sign = True
        return sign
    
    
    def setUserActiviesUrl(self,url):
        self.userActiviesUrl = url
        
        
if __name__ == '__main__':
    a = PersonalActiviesService('997da560-6de2-4056-8614-e7cd95dd967b','ovQBPxGwi5RUfDoZDc-xep7EraEI')
    a.setUserActiviesUrl('https://dev-uop-api.opg.cn/activities-service/raffleResult/getMemberRaffleReCords')
    acils = a.getActivitiesidList()
    print(acils)
    