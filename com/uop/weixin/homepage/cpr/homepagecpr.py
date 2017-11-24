#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Created on 2017

@author: li.taojun
'''

import json


#检查首页响应数据json格式及返回码
def checkHomepageFormat(resphome):
    sign = False
    rspkey = ['code','data','message']
    datakey = ['position','activities']
    keynext =       [
                       'position','listOrder','picPath','activityId','title','subhead','activityStartTime',
                       'activityStartTimeStr','activityEndTime','activityEndTimeStr','activityAddress','originalPrice','point',
                       'minPrice','skuNumber','status','displayType','sellingStartTime','sellingEndTime'
                    ]
    keynextkey = {
                  "01":[
                           'position','listOrder','picPath','activityId','title','subhead','activityStartTime',
                           'activityStartTimeStr','activityEndTime','activityEndTimeStr','activityAddress','originalPrice','point',
                           'minPrice','skuNumber','status','displayType','sellingStartTime','sellingEndTime'
                       ],
                   "02":[
                           
                        ],
                   "03":[
                           
                        ],
                   "04":[
                           
                        ]
                  }
    resphomepage = resphome.text
    if resphomepage is not None and resphomepage != "":
          print  "resphomepage = " +resphomepage
          homejson = json.loads(resphomepage)
          hoemkeys = homejson.keys()
          if set(hoemkeys) == set(rspkey):
          #if "code" in hoemkeys and "data" in hoemkeys:
              datajsonlist = homejson.get("data")
              if datajsonlist is not None and len(datajsonlist)>0:
                   datakeysAct = datajsonlist[0].keys()
                   if sorted(datakeysAct) == sorted(datakey):
                       keynextact = datajsonlist[0].get("activities")[0].keys()
                       if set(keynext) == set(keynextact):
                           sign = True
    return sign

#获取首页响应消息返回码
def getHomeRspCode(resphome):
    rspcode = None
    resphomepage = resphome.text
    if resphomepage is not None and resphomepage != "":
          homejson = json.loads(resphomepage)
          if homejson.has_key("code"):
               rspcode = homejson.get("code")
    return rspcode


class Testmem():
    a = 1
    b = "litaojun"
    
    def __init__(self,m,n):
        a = m
        b = n
    def __eq__(self,t):
        return True
    def __hash__(self):
        return hash(self.b)
        
if __name__ == '__main__':
    t1 = Testmem(2,"test")
    t2 = Testmem(2,"test")
    a = ['code','data','message',(1,2,3),t1]
    b = ['code','data','message',(1,2,3),t2]
    c = ['data','code','message',(1,2,3),t1]
    x = {t1:"aaa"}
    print x[t1]
    if a == b:
        print "scu"
    else:
        print "err"
    if c == b:
        print "scu"
    else:
        print "err"
    if set(c) == set(b):
        print "scu"
    else:
        print "err"