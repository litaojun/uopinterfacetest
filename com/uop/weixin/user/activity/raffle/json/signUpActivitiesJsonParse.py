#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
Created on 2017��11��20��

@author: li.taojun
'''
import json
#������һ��JSON��KEY
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