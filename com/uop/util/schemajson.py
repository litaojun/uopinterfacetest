#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Created on 2017

@author: li.taojun
'''
import json
#from jsonschema import validators 
#from jsonschema import validate
from jsonschema import Draft4Validator
from functools import wraps
from jsonschema import FormatChecker
from jsonschema import ValidationError
class Validator(object):
    def __init__(self, schemaformat):
        #self.name = name
        self.schema = schemaformat
        checker = FormatChecker()
        self.validator = Draft4Validator(self.schema,
                                                format_checker=checker)

    def validate(self, data):
        try:
            self.validator.validate(data)
        except ValidationError as ex:
            #OG.exception(ex.message)
            # TODO(ramineni):raise valence specific exception
            raise Exception(ex.message)


##validator.py
def check_rspdata(validator):
    def decorated(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            print "kwargs="+str(kwargs)
            #print "litaojun11111"
            #jsondata = json.loads(kwargs["response"])
            jsondata = kwargs["response"]
            #LOG.debug("validating input %s with %s", data, validator.name)
            validator.validate(jsondata)
            ##这里看起来有个bug，应该是f(*args, **kwargs),未测试
            #lsstr = f()
            #print lsstr
            return f(jsondata)
            #print "litaojun22222"
        return wrapper
    return decorated



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
validator = Validator(schema)
@check_rspdata(validator)
def a(response = None):
    #jsond = {"name" : "Eggs", "price" : 34.99,'list':[1,5,7],'address':'bj-jiuxianqiao'}
    #print "litaojun00000"
    return "litaojun"
if __name__ == '__main__':
    jsond = {"name" : "Eggs", "price" : 34.99,'list':[1,5],'address':'bj-jiuxianqiao'}
    a(response=json.dumps(jsond))