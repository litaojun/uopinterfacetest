#!/usr/bin/env python
# -*- coding:utf-8 -*-
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
#from com.uop.weixin.user.raffle.cpr.httpsTest import hearder
class UserAddressService(object):
    '''
    classdocs
    '''
    #获取用户默'认地址
    defaultAddress = memeraddressurl
    #获取用例地址列表
    
    #新增地址
    #删除地址
    memberId = None
    openid = None
    def __init__(self, memberId,openid):
        '''
        Constructor
        '''
        self.memberId = memberId
        self.openid = openid
    
    #获取默认地址请求
    def getUserDefaltAddressJson(self):
        jsonheart = transUopHttpHears(self.memberId,self.openid)
        useraddrspjson = requests.get(url=self.defaultAddress,headers = jsonheart)
        return useraddrspjson
    
    #解析默认址地址ID
    def getUserDefaltAddressID(self):
        addjson = self.getUserDefaltAddressJson()
        useraddressid = parseMemberDefalutAddJSON(addjson) 
        return useraddressid
    
if __name__ == '__main__':
    pass