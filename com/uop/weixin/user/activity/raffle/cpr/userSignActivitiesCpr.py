#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Created on 2017��11��20��

@author: li.taojun
'''
from com.uop.util.schemajson import check_rspdata,Validator
import json
useraddressScma = {}
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