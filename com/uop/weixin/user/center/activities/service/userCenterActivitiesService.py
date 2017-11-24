#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017��11��22��

@author: li.taojun
'''

import requests
from com.uop.util.configurl import userActiviesUrl
from com.uop.util.jsonTransform import transUopHttpHears
from com.uop.weixin.user.activity.raffle.json.memberAddJonsParse import parseMemberDefalutAddJSON
from com.uop.weixin.user.activity.raffle.json.signUpActivitiesJsonParse import transUserSignupActivitiesHttpJson
from com.uop.weixin.user.activity.raffle.cpr.userSignActivitiesCpr import checkSignUpActivitiesResultFormat
from com.uop.weixin.user.center.activities.json.centerActivitiesParse import parseActivitiesIdFromJson
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
        
    def userActivies(self):
        jsonheart = transUopHttpHears(self.memberId,self.openid)
        actjson = {"memberId":self.memberId,"page":1,"limit":10}
        activityrspjson = requests.post(url=self.userActiviesUrl,json = actjson,headers = jsonheart,verify=False)
        return activityrspjson
    
    def getActivitiesidList(self):
        actjson = self.userActivies()
        actidls = parseActivitiesIdFromJson(response = json.loads(actjson.text))
        return actidls
    
    def setUserActiviesUrl(self,url):
        self.userActiviesUrl = url
        
        
if __name__ == '__main__':
    a = PersonalActiviesService('997da560-6de2-4056-8614-e7cd95dd967b','ovQBPxGwi5RUfDoZDc-xep7EraEI')
    a.setUserActiviesUrl('https://dev-uop-api.opg.cn/activities-service/raffleResult/getMemberRaffleReCords')
    acils = a.getActivitiesidList()
    print acils
    