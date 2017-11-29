#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Created on 20171025

@author: li.taojun
'''
from selenium import webdriver
from opg.unit.parametrized import ParametrizedTestCase
from com.uop.util.configurl import homepageurl,userraffleluck
from com.uop.util.httpRequest import  http_get,http_post
from opg.unit.testcaseRunMgr import runTestOneCls
class userRaffleTest(ParametrizedTestCase):
    """
                     即开抽奖提交
    """
    __interfaceName__ = "/activities-service/raffleResult/luckDraw"
    def userRaffleCollect(self):
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
    runTestOneCls(casefilepath='D:\\litaojun\\workspace\\uopweixinInterface\\uop\\weixin\\homepage\\userraffleluck.xlsx', testclse=userRaffleTest, moduleabspath="D:\\litaojun\\workspace\\uopweixinInterface")