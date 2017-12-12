__all__ = ['parseMemberDefalutAddJSON', 'transUserSignupActivitiesHttpJson', 
           'checkSignUpActivitiesResultFormat', 'SignUpActivitiesService' ]  
# deprecated to keep older scripts who import this from breaking  
from uopweixin.center.address.ParseMemberAddJons import parseMemberDefalutAddJSON
from uopweixin.activity.raffle.ParseSignUpActivitiesJson import transUserSignupActivitiesHttpJson
from uopweixin.activity.raffle.userSignActivitiesCpr import checkSignUpActivitiesResultFormat
from uopweixin.activity.raffle.signupActivitiesService import SignUpActivitiesService