#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017

@author: li.taojun
'''
import requests
from com.uop.util.configurl import memeraddressurl,signUpOpenActUrl
from com.uop.util.jsonTransform import transUopHttpHears
from com.uop.weixin.user.activity.raffle.json.memberAddJonsParse import parseMemberDefalutAddJSON
from com.uop.weixin.user.activity.raffle.json.signUpActivitiesJsonParse import transUserSignupActivitiesHttpJson
from com.uop.weixin.user.activity.raffle.cpr.userSignActivitiesCpr import checkSignUpActivitiesResultFormat

class SignUpActivitiesService(object):
    '''
    classdocs
    '''
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
    
    def getActivitiesPointByAid(self):
        jsonheart = transUopHttpHears(self.memberId,self.openid)
        activityrspjson = requests.get(url=self.defaultAddress,headers = jsonheart)
        
        
if __name__ == "__main__":
    a = SignUpActivitiesService("","","")
    b = SignUpActivitiesService("","","")
    sta = set()
    sta.add(b)
    sta.add(a)