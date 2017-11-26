'''
Created on 2017��11��20��

@author: li.taojun
'''
from opg.unit.testcaseRunMgr import runTestOneCls
from opg.unit.parametrized import ParametrizedTestCase
from com.uop.util.configurl import memeraddressurl,signUpOpenActUrl
from com.uop.util.jsonTransform import transUopHttpHears
from com.uop.weixin.user.activity.raffle.json.memberAddJonsParse import parseMemberDefalutAddJSON
from com.uop import transUserSignupActivitiesHttpJson
from com.uop.weixin.user.activity.raffle.cpr.userSignActivitiesCpr import checkSignUpActivitiesResultFormat
import requests
from com.uop.weixin.user.activity.raffle.service.signupActivitiesService import SignUpActivitiesService
from com.uop.weixin.user.center.personal.service.personalCenterService import MemberPerCenterService

class SignUpActivities(ParametrizedTestCase):
      __interfaceName__ = "/activities-service/raffleResult/signUpNonOpenActivities"
      
      def __init__(self):
          inputdata =  self.getInputData()
          #memberId,openid,activitiesId
          self.signupservice = SignUpActivitiesService(inputdata['memberId'],
                                                       inputdata['openid'],
                                                       inputdata['activitiesId'])
          self.personalCenterService = MemberPerCenterService(inputdata['memberId'],
                                                              inputdata['openid'])
          self.defaultAddress = memeraddressurl
          self.userSignupActivities = signUpOpenActUrl
         
      def userSignUpActivities(self):
          #
          preuserTotalPoint = self.personalCenterService.getPersonalSign()
          activitiesPoint = self.signupservice.getActivitiesPointByAid()
          userSignUpResultJson = self.signupservice.userSignupActivities()
          self.assertTrue(checkSignUpActivitiesResultFormat(userSignUpResultJson))
          
          
          
if __name__ == '__main__':
    pass