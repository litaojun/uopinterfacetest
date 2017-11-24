#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017

@author: li.taojun
'''
import requests,json
from com.uop.util.configurl import memeraddressurl,signUpOpenActUrl,personalCenterUrl
from com.uop.util.jsonTransform import transUopHttpHears
from com.uop.weixin.user.center.personal.json.personalCenterJsonParse import parseUserPointByRspJSON
class MemberPerCenterService(object):
    '''
    classdocs
    '''
    def __init__(self, memberId,openid):
        '''
        Constructor
        '''
        self.memberId = memberId
        self.openid = openid
        self.personalCenterUrl = personalCenterUrl
    def personalCenter(self):
        jsonheart = transUopHttpHears(self.memberId,self.openid)
        print "jsonheart=%s,personalCenterUrl=%s" % (jsonheart,self.personalCenterUrl)
        activityrspjson = requests.get(url=self.personalCenterUrl,headers = jsonheart,verify=False)
        return activityrspjson
        
    def getPersonalSign(self):
        #usertotalPoint = 0
        usersignjson = self.personalCenter()
        print "usersignjson=%s" % usersignjson.text
        usertotalPoint = parseUserPointByRspJSON(response = json.loads(usersignjson.text))
        return usertotalPoint

    def setPersonalCenterUrl(self,centerurl):
        self.personalCenterUrl = centerurl
    
if __name__ == "__main__":
    a = MemberPerCenterService("997da560-6de2-4056-8614-e7cd95dd967b","ovQBPxGwi5RUfDoZDc-xep7EraEI")
    a.setPersonalCenterUrl("https://dev-uop-api.opg.cn/member-service/members/personalCenter")
    userpoint = a.getPersonalSign()
    print "userpoint=%s" % userpoint
        