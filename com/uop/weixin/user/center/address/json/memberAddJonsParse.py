#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Created on 2017

@author: li.taojun
'''
from com.uop.util.schemajson import check_rspdata,Validator
import json
useraddressScma = {}
validator = Validator(useraddressScma)
@check_rspdata(validator)

#非即开活动提交时，获取地址ID
def parseMemberDefalutAddJSON(resphome):
    addressjson = resphome.TEXT
    useraddressid = addressjson.get("data").get("id")
    return useraddressid

if __name__ == '__main__':
    pass