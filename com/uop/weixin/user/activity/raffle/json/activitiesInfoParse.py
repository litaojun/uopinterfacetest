#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Created on 201

@author: li.taojun
'''
from com.uop.util.schemajson import check_rspdata,Validator
import json

activitiesInfoScma = {
                       "type":"object",
                       "properties":
                                    {
                                       "code" : {"type":"string"},
                                       "message" : {"type":"string"},
                                       "data": {
                                                  "type":"object",
                                                  "properties":{
                                                                    "success": {"type":"boolean"},
                                                                   # "envContext": {"type":"string"},
                                                                   # "errorContext": {"type":"string"},
                                                                    "totalPoints": {"type":"integer"},
                                                                    "sex": {"type":"string"},
                                                                    "nickName":{"type":"string"},
                                                                    "headimgUrl": {"type":"string"},
                                                                    "isSign": {"type":"boolean"},
                                                                    "readInvite": {"type":"boolean"}
                                                                }
                                                }
                                    }
                     }

validator = Validator(activitiesInfoScma)
#获取非即开活动抽奖所需积分
@check_rspdata(validator)
def parseActivitiesPointByRspJSON(response=None):
    #addressjson = response.TEXT\
    print "response=%s" % str(response)
    activitiesPoint = response.get("raffleBaseInfo").get("point")
    return activitiesPoint

if __name__ == '__main__':
    pass