#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
Created on 2017

@author: li.taojun
'''
import json
#
def parseMemberDefalutAddJSON(resphome):
    pass
#非即开活动提交请求json数据
def transUserSignupActivitiesHttpJson(memberid="",activitiesid = "",addressid = ""):
    '''
        memberid : 
        activitiesid : 
        addressid : 
    '''
    usersignactivities = {
                           "memberId":memberid,
                           "activitiesId":activitiesid,
                           "addressId":addressid
                         }
    return usersignactivities
if __name__ == '__main__':
    pass