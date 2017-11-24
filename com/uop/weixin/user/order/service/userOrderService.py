#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017

@author: li.taojun
'''
import requests,json
from com.uop.util.configurl import memeraddressurl,signUpOpenActUrl,personalCenterUrl,userOrderUrl
from com.uop.util.jsonTransform import transUopHttpHears
from com.uop.weixin.user.order.json.paserMemberOrderJson import parseUserPointByRspJSON
class centerOrderService(object):
    '''
    classdocs
    '''
    def __init__(self, memberId,openid):
        '''
        Constructor
        '''
        self.memberId = memberId
        self.openid = openid
        self.userOrderUrl = userOrderUrl
        
    def userOrderListByStatus(self,status= ""):
        jsonheart = transUopHttpHears(self.memberId,self.openid)
        print "jsonheart=%s,personalCenterUrl=%s" % (jsonheart,self.userOrderUrl)
        orderlistrspjson = requests.get(url=self.userOrderUrl,headers = jsonheart,verify=False)
        orderlsjson = parseUserPointByRspJSON(response = json.loads(orderlistrspjson.text))
        return orderlsjson
    
    def setUserOrderUrl(self,orderurl):
        self.userOrderUrl = orderurl
        
if __name__ == "__main__":
        a = centerOrderService("997da560-6de2-4056-8614-e7cd95dd967b","ovQBPxGwi5RUfDoZDc-xep7EraEI")
        a.setUserOrderUrl("https://dev-uop-api.opg.cn/order-service/orders?memberId=997da560-6de2-4056-8614-e7cd95dd967b&orderStatus=&page=1&pageSize=10")
        orderls = a.userOrderListByStatus()
        print "orderls=%s" % (orderls)
        
    