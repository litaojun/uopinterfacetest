#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017

@author: li.taojun
'''
import requests,json
from com.uop.util.configurl import memeraddressurl,signUpOpenActUrl,personalCenterUrl,userOrderUrl
from com.uop.util.jsonTransform import transUopHttpHears
from com.uop.weixin.user.center.order.json.paserMemberOrderJson import parseUseOrderListByRspJSON

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
        
    #根据订单状态查询订单列表
    def userOrderListByStatus(self,status= ""):
        jsonheart = transUopHttpHears(self.memberId,self.openid)
        self.userOrderUrl = self.userOrderUrl % status
        print("jsonheart=%s,personalCenterUrl=%s" % (jsonheart,self.userOrderUrl))
        orderlistrspjson = requests.get(url=self.userOrderUrl,headers = jsonheart,verify=False)
        return orderlistrspjson
    
    #根据订单列表解析出有效字段（orderStatus,orderId,buyCount,picPath,point,itemPrice）
    def filterFildOrderList(self,status):
        orderlistrspjson = self.userOrderListByStatus(status)
        orderlsjson = parseUseOrderListByRspJSON(response = json.loads(orderlistrspjson.text))
        
    #检查订单ID是否存在
    def checkOrderStatusExsit(self,status,orderid):
        sign = False
        orderlistrspjson = self.userOrderListByStatus(status)
        for order in parseUseOrderListByRspJSON(response = json.loads(orderlistrspjson.text)):
            if orderid == order[1] and status ==order[0]:
                sign = True
                break
        return sign
        orderlsjson = self.userOrderListByStatus(status)
        
        
    def setUserOrderUrl(self,orderurl):
        self.userOrderUrl = orderurl
        
if __name__ == "__main__":
        a = centerOrderService("997da560-6de2-4056-8614-e7cd95dd967b","ovQBPxGwi5RUfDoZDc-xep7EraEI")
        a.setUserOrderUrl("https://dev-uop-api.opg.cn/order-service/orders?memberId=997da560-6de2-4056-8614-e7cd95dd967b&orderStatus=&page=1&pageSize=10")
        orderls = a.userOrderListByStatus()
        print("orderls=%s" % (orderls))
        
    