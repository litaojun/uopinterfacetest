#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017

@author: li.taojun
'''
from opg.unit.testcaseRunMgr import runTestOneCls
from opg.unit.parametrized import ParametrizedTestCase
from uopweixin.util.configurl import memeraddressurl,signUpOpenActUrl
#from ......util.configurl import memeraddressurl,signUpOpenActUrl
from uopweixin.util.jsonTransform import transUopHttpHears
from uopweixin.center.address.ParseMemberAddJons import parseMemberDefalutAddJSON
from uopweixin import transUserSignupActivitiesHttpJson,PersonalActiviesService
from uopweixin.activity.raffle.userSignActivitiesCpr import checkSignUpActivitiesResultFormat
import requests
from uopweixin.activity.raffle.signupActivitiesService import SignUpActivitiesService
from uopweixin.center.personal.personalCenterService import MemberPerCenterService


class SignUpActivities(ParametrizedTestCase):
      __interfaceName__ = "/activities-service/raffleResult/signUpNonOpenActivities"
      
      def __init__(self):
          self.inputdata =  self.getInputData()
          #memberId,openid,activitiesId
          self.signupservice = SignUpActivitiesService(self.inputdata['memberId'],
                                                       self.inputdata['openid'],
                                                       self.inputdata['activitiesId'])
          self.personalCenterService = MemberPerCenterService(self.inputdata['memberId'],
                                                              self.inputdata['openid'])
          self.personalActiviesSer = PersonalActiviesService(self.inputdata['memberId'],
                                                             self.inputdata['openid'])
          self.defaultAddress = memeraddressurl
          self.userSignupActivities = signUpOpenActUrl
      
      def setUp(self):
          pass
      
      def userSignUpActivities(self):
          #后期抽奖前的个人总积分
          preuserTotalPoint = self.personalCenterService.getPersonalSign()
          #获取抽奖该活动所需积分
          activitiesPoint = self.signupservice.getActivitiesPointByAid()
          #非即开活动抽奖正常提交
          userSignUpResultJson = self.signupservice.userSignupActivities()
          #检查返回格式及相关数据
          self.assertTrue(checkSignUpActivitiesResultFormat(userSignUpResultJson))
          #获取抽奖后个人总积分
          afterUserTotalPoint = self.personalCenterService.getPersonalSign()
          #检查抽奖后用户积分是否减少正确 
          self.assertTrue(preuserTotalPoint-activitiesPoint == afterUserTotalPoint)
          #检查我的活动列表是否存在该活动
          self.assertTrue(self.personalActiviesSer.checkActivitiesExsit(self.inputdata['activitiesId']))
          
      def tearDown(self):
          pass
    

if __name__ == '__main__':
    pass