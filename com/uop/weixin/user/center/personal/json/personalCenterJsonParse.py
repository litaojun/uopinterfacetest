#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017

@author: li.taojun
'''

from com.uop.util.schemajson import check_rspdata,Validator
import json

userCenterScma = {
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
validator = Validator(userCenterScma)
#
@check_rspdata(validator)
def parseUserPointByRspJSON(response=None):
    #addressjson = response.TEXT\
    print "response=%s" % str(response)
    userPoint = response.get("data").get("totalPoints")
    return userPoint
if __name__ == '__main__':
    pass