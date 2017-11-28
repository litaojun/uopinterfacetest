'''
Created on 2017��11��20��

@author: li.taojun
'''
from opg.unit.testcaseRunMgr import runTestOneCls
from opg.unit.parametrized import ParametrizedTestCase
from com.uop.util.configurl import memeraddressurl,signUpOpenActUrl
from com.uop.util.jsonTransform import transUopHttpHears
from com.uop.weixin.user.activity.raffle.json.memberAddJonsParse import parseMemberDefalutAddJSON
from com.uop import transUserSignupActivitiesHttpJson,PersonalActiviesService
from com.uop.weixin.user.activity.raffle.cpr.userSignActivitiesCpr import checkSignUpActivitiesResultFormat
import requests
from com.uop.weixin.user.activity.raffle.service.signupActivitiesService import SignUpActivitiesService
from com.uop.weixin.user.center.personal.service.personalCenterService import MemberPerCenterService


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
          #���ڳ齱ǰ�ĸ����ܻ���
          preuserTotalPoint = self.personalCenterService.getPersonalSign()
          #��ȡ�齱�û�������
          activitiesPoint = self.signupservice.getActivitiesPointByAid()
          #�Ǽ�����齱�����ύ
          userSignUpResultJson = self.signupservice.userSignupActivities()
          #��鷵�ظ�ʽ���������
          self.assertTrue(checkSignUpActivitiesResultFormat(userSignUpResultJson))
          #��ȡ�齱������ܻ���
          afterUserTotalPoint = self.personalCenterService.getPersonalSign()
          #���齱���û������Ƿ������ȷ 
          self.assertTrue(preuserTotalPoint-activitiesPoint == afterUserTotalPoint)
          #����ҵĻ�б��Ƿ���ڸû
          self.assertTrue(self.personalActiviesSer.checkActivitiesExsit(self.inputdata['activitiesId']))
          
      def tearDown(self):
          pass
    

if __name__ == '__main__':
    pass