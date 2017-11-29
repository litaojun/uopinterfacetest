__all__ = ['parseMemberDefalutAddJSON', 'transUserSignupActivitiesHttpJson', 
           'checkSignUpActivitiesResultFormat', 'SignUpActivitiesService','parseActivitiesPointByRspJSON' ]  
# deprecated to keep older scripts who import this from breaking  
from com.uop.weixin.user.center.address.json.memberAddJonsParse import parseMemberDefalutAddJSON
from .json.signUpActivitiesJsonParse import transUserSignupActivitiesHttpJson
from .cpr.userSignActivitiesCpr import checkSignUpActivitiesResultFormat
from .service.signupActivitiesService import SignUpActivitiesService
from .json.activitiesInfoParse import parseActivitiesPointByRspJSON
#·Ç¼´¿ª³é½±