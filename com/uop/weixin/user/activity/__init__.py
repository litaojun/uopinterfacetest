__all__ = ['parseMemberDefalutAddJSON', 'transUserSignupActivitiesHttpJson', 
           'checkSignUpActivitiesResultFormat', 'SignUpActivitiesService' ]  
# deprecated to keep older scripts who import this from breaking  
from com.uop.weixin.user.center.address.json.memberAddJonsParse import parseMemberDefalutAddJSON
from .raffle.json.signUpActivitiesJsonParse import transUserSignupActivitiesHttpJson
from .raffle.cpr.userSignActivitiesCpr import checkSignUpActivitiesResultFormat
from .raffle.service.signupActivitiesService import SignUpActivitiesService