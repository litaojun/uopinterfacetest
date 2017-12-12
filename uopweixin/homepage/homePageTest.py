#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Created on 2017

@author: li.taojun
'''
from selenium import webdriver
from opg.unit.testcaseRunMgr import runTestOneCls
from opg.unit.parametrized import ParametrizedTestCase
from uopweixin.util.configurl import homepageurl
#from com.uop.util.httpRequest import  http_get,http_post
import requests
from uopweixin.util.jsonTransform import transUopHttpHears
#from com.uop.weixin.user.raffle.cpr.httpsTest import hearder
from uopweixin.homepage.homepagecpr import checkHomepageFormat,getHomeRspCode
class homepages(ParametrizedTestCase):
    __interfaceName__ = "/uop-featured/index/configs/queryPublishedActivityInfoShowConfigs"
    homeurl = homepageurl
    def homepageget(self):
        inputdata =  self.getInputData()
        #请求头数据
        jsonheart = transUopHttpHears(inputdata['memberId'],inputdata['openid'])
        #请求首页
        homeresponse = requests.get(url=self.homeurl,headers = jsonheart)
        #验证格式正确行
        self.assertTrue(checkHomepageFormat(homeresponse), "")
        #验证返回
        rspcode = getHomeRspCode(homeresponse)
        self.assertEqual(getHomeRspCode(homeresponse) ,"200", "code not 200 and code= %s" % rspcode)
        self.assertTrue(checkHomepageFormat(homeresponse), "json格式不正确")
        self.assertTrue(1<2, self.getInputData())
        
    def homepagegetError(self):
        homecontent = requests.get(homepageurl)
        inputdata =  self.getInputData()
        #inputdata =  unicode(inputdata, "utf-8") 
        print(inputdata)
        homeresp = requests.post(homepageurl,param=inputdata)
        self.assertTrue(1>2,inputdata)
       
    def homepagegetlen(self):
        homecontent = requests.get(homepageurl)
        inputdata =  self.getInputData()
        #inputdata =  unicode(inputdata, "utf-8")
        print(inputdata)
        homeresp = requests.post(homepageurl,param=inputdata)
        self.assertTrue(1>2,inputdata)
        
    def getInputData(self):
        data = super(homepages,self).getInputData()
        itemdata = data.split("\n")
        jsonstr = "{"+",".join(itemdata) + "}"
        dicdata =  eval(jsonstr)
        #test = dicdata["uuid"]
        return dicdata
        
        
if __name__ == '__main__':
    runTestOneCls(casefilepath='D:\\litaojun\\workspace\\uopweixinInterface\\uop\\weixin\\homepage\\queryPublishedActivityInfoShowConfigs.xlsx', testclse=homepages, moduleabspath="D:\\litaojun\\workspace\\uopweixinInterface")