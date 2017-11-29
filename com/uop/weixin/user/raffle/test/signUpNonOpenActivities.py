#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Created on 2017

@author: li.taojun
'''
from selenium import webdriver
from opg.unit.parametrized import ParametrizedTestCase
from com.uop.util.configurl import homepageurl,userraffleluck
from com.uop.util.httpRequest import  http_get,http_post
from opg.unit.testcaseRunMgr import runTestOneCls
import requests
class userRaffleTest(ParametrizedTestCase):
        """
               
        """
        __interfaceName__ = "/activities-service/raffleResult/signUpNonOpenActivities"
        memeraddressurl = "http://uat-uop-wx.opg.cn/member-service/address/memberId"
        signUpOpenActUrl = "http://uat-uop-wx.opg.cn/activities-service/raffleResult/signUpNonOpenActivities"
        def userRaffleCollect(self):
            inputdata =  self.getInputData()
            addressMem =   {
                                "memberId":inputdata['memberId'],
                                "openid":inputdata['openid']
                           }
            homeresp = requests.get(self.memeraddressurl,hearders=addressMem)
            addressid = homeresp['data'][0]['id']
            activityjson = {
                                "memberId":inputdata['memberId'],
                                "activitiesId":inputdata['activitiesId'],
                                "addressId":addressid
                           }
            signopenactivities = requests.post(self.signUpOpenActUrl, 
                                               json=activityjson, 
                                               hearders=addressMem)
            self.assertTrue(1<2, self.getInputData())

        def userRaffleCollectError(self):
            inputdata =  self.getInputData()
            homeresp = http_post(userraffleluck,param=inputdata)
            self.assertTrue(1<2, self.getInputData())

        def getInputData(self):
            data = super(userRaffleTest,self).getInputData()
            itemdata = data.split("\n")
            jsonstr = "{"+",".join(itemdata) + "}"
            dicdata =  eval(jsonstr)
            test = dicdata["memberId"]
            return dicdata


if __name__ == '__main__':
    runTestOneCls(casefilepath='D:\\litaojun\\workspace\\uopweixinInterface\\uop\\weixin\\homepage\\userrafflesignUpNonOpenActivities.xlsx', testclse=userRaffleTest, moduleabspath="D:\\litaojun\\workspace\\uopweixinInterface")
