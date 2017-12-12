#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Created on 2017��11��20��

@author: li.taojun
'''
from uopweixin.util.schemajson import check_rspdata,Validator
import json
useraddressScma = {
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
#                                                                     "webToken": null,
#                                                                     "ipAddress": null
                                                                   }
                                                       },
#                                         "errorContext": null,
                                        "resultId": "b21812b8-2cec-4613-92a9-80bd2565494e"
                                       }
                    }
validator = Validator(useraddressScma)
@check_rspdata(validator)
def checkSignUpActivitiesResultFormat(resphome):
    sign  = True
    signkeyjson = ['success','envContext','errorContext','resultId']
    envContextSubJson = ['traceInfo','webToken','webToken']
    traceSubJson = ['traceId','spanId']
    return sign

if __name__ == '__main__':
    pass