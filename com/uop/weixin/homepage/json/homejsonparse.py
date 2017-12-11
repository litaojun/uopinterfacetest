#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Created on 2017

@author: li.taojun
'''
import json
#
def parsejsonOne(resphome):
    rspkey = ['code','data','message']
    actkey = []
    resphomepage = resphome.text
    if resphomepage is not None and resphomepage != "":
          print("resphomepage = " +resphomepage)
          homejson = json.loads(resphomepage)
          actkey = homejson.keys()
          #if set(hoemkeys) == set(rspkey):
    return actkey

def parsejonsTwo(resphome):
    actdatakey = []
    datakey = ['position','activities']
    resphomepage = resphome.text
    datajson = resphomepage.get("data")
    if datajson is not None and len(datajson) > 0:
         actdatakey = datajson[0].keys()
    return actdatakey

def parsejonsThree(resphome):
    actActivitieskey = [
                           'position','listOrder','picPath','activityId','title','subhead','activityStartTime',
                           'activityStartTimeStr','activityEndTime','activityEndTimeStr','activityAddress','originalPrice','point',
                           'minPrice','skuNumber','status','displayType','sellingStartTime','sellingEndTime'
                       ]
    activitiesjsonkey = []
    resphomepage = resphome.text
    activitiesjsonkey = resphomepage.get("data")[0].get("activities")[0].keys()
    return activitiesjsonkey
    
    
if __name__ == '__main__':
    pass