#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
Created on 2017年11月20日

@author: li.taojun
'''
import json
#解析第一层JSON的KEY
def parseMemberDefalutAddJSON(resphome):
    pass
def transUserSignupActivitiesHttpJson(memberid="",activitiesid = "",addressid = ""):
    usersignactivities = {
                           "memberId":memberid,
                           "activitiesId":activitiesid,
                           "addressId":addressid
                         }
    return usersignactivities
if __name__ == '__main__':
    pass