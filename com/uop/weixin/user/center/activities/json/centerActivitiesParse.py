#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017

@author: li.taojun
'''
from com.uop.util.schemajson import check_rspdata,Validator
from com.uop.weixin.user.activity import transUserSignupActivitiesHttpJson
import json
userCenterScma = {
                        "type":"object",
                         "properties":{
                                        "success": {"type":"boolean"},
                                        "envContext": {
                                                       "type":"object",
                                                       "properties":{
                                                                        "traceInfo": {
                                                                                        "type":"object",
                                                                                        "properties":{
                                                                                                        "traceId": {"type":"string"},
                                                                                                        "spanId": {"type":"string"}
                                                                                                     }
                                                                                     },
                                                                         #"webToken": null,
                                                                         #"ipAddress": null
                                                                    }
                                                      },
                                        #"errorContext": null,
                                        "data": 
                                                {
#                                                  "type":"object",
#                                                  "properties":{
                                                                "type":"array",
                                                                'items': {  
                                                                            "type":"object",
                                                                             "properties":{
                                                                                            #"orderImg": {"type":"string"},
                                                                                            "id": {"type":"string"},
                                                                                            "memberId": {"type":"string"},
                                                                                            "activitiesId": {"type":"string"},
                                                                                            #"orderTime": 1511317297000,
                                                                                             "orderTime":  {"type":"number"},
                                                                                            "prizeState": {"type":"string"},
                                                                                            "dataType":{"type":"string"},
                                                                                            #"orderId": {"type":"string"},
                                                                                            #"activitiesTitle": null,
                                                                                            "lotteryType": {"type":"string"},
                                                                                            "prizeImg": {"type":"string"},
                                                                                            #"prizeName": {"type":"string"},
                                                                                            "activitiesAddress": {"type":"string"},
                                                                                            "joinNum": {"type":"number"},
                                                                                            "address": {"type":"boolean"},
                                                                                            "title":{"type":"string"}
                                                                                          }

                                                                          } 
#                                                                }
                                                }
                                        }
                    }
validator = Validator(userCenterScma)
#
@check_rspdata(validator)
def parseActivitiesIdFromJson(response = None):
    acidls = []
    activitiesLs = response.get("data")
    for ajson in activitiesLs:
        acidls.append(ajson.get("activitiesId"))
    return acidls

def parseMyActivitiesIDFromJson(response = None,activitiesid = None):
    acid = None
    activitiesLs = response.get("data")
    for ajson in activitiesLs:
        if ajson.get("activitiesId") == activitiesid:
            acid = ajson
            break
    return acid


if __name__ == '__main__':
    pass