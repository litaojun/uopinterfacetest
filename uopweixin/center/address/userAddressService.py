#!/usr/bin/env python
# -*- coding:utf-8 -*-
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