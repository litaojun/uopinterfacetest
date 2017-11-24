#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Created on 2017年11月21日
#http://xiaorui.cc/2014/10/20/python%E4%BD%BF%E7%94%A8schema%E5%BA%93%E8%BF%9B%E8%A1%8C%E6%95%B0%E6%8D%AE%E6%A0%A1%E9%AA%8C/
@author: li.taojun
'''
from jsonschema import validate
from com.uop.util.schemajson import Draft4Validator
schema = {
            "type" : "object",
            "properties" : 
                        {
                            "price" : {"type" : "number"},
                            "name" : {"type" : "string"},
                            "list":{"maxItems":2},
                            "address":{'regex':'bj'},
                        },
         }
schemaa = {
                "$schema": "http://json-schema.org/schema#",
                "type": "object",
                "properties": {
                                "name": {"type": "string"},
                                "email": {"type": "string"}
                              },
                "required": ["email"],
          }
curschema = {
                "title": "Example Schema",
                "type": "object",
                "properties": {
                                    "firstName": {
                                                    "type": "string"
                                                 },
                                    "lastName": {
                                                    "type": "string"
                                                },
                                    "age":  {
                                                "description": "Age in years",
                                                "type": "integer",
                                                "minimum": 0
                                            }
                                },
                "required": ["firstName", "lastName"]
            }
def a():
    josntest = {
                    "code": 1,
                    "message": "请求成功",
                    "data": {
                                "success": True,
                                "envContext": None,
                                "errorContext": " fff",
                                "totalPoints": 50,
                                "sex": "1",
                                "nickName": "李涛军",
                                "headimgUrl": "http://wx.qlogo.cn/mmopen/6Jkxxk5dmNk7HlVN9mLz5BgiakCF8qpVYp4RyDfu7q0I3gu3fGcBr0ng7TyA7U2kYnXleiblKHQFjATH8jelOcbbb35nADZgry/0",
                                "isSign": False,
                                "readInvite": False
                              }
               }
    jsonschem = {
                    "type" : "object",
                    "properties" : {
                                            "code" : {"type":"string"},
                                            "message" :  {"type":"string"},
                                            "data":{
                                                     "type":"object",
                                                     "properties":
                                                                    {
                                                                                    "success":{"type":"boolean"},
                                                                                    #"envContext": {"type":"object"},
                                                                                    "errorContext": {"type":"string"},
                                                                                    "totalPoints": {"type":"number"},
                                                                                    "sex": {"type":"string"},
                                                                                    "nickName": {"type":"string"},
                                                                                    "headimgUrl": {"type":"string"},
                                                                                    "isSign": {"type":"boolean"},
                                                                                    "readInvite": {"type":"boolean"}
                                                                    },
                                                     "required": ["nickName", "headimgUrl"]
                                                    }
                                    
                                    },
                    }
    validate(josntest,jsonschem)
def checkSchema():
    validate({"name" : "Eggs", "price" : 34.99,'list':[1,5,7],'address':'bj-jiuxianqiao'}, schema)
    #validate([2, 3, 4], {"maxItems" : 2})
def checkSchemaFormat():
    Draft4Validator.check_schema(schemaa)
if __name__ == '__main__':
    #checkSchema()
    #checkSchemaFormat()
    a()
    print "a"