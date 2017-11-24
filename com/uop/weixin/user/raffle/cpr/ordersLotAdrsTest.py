from selenium import webdriver
from opg.unit.parametrized import ParametrizedTestCase
from com.uop.util.configurl import homepageurl,userOrderLottleAddress
from com.uop.util.httpRequest import  http_get,http_post
from opg.unit.testcaseRunMgr import runTestOneCls
class userlotteAddressTest(ParametrizedTestCase):
    """
                     中奖后提交地址
    """
    __interfaceName__ = "/order-service/orders/lottery/address"
    def userRaffleCollect(self):
        inputdata =  self.getInputData()
        homeresp = http_post(userOrderLottleAddress,param=inputdata)
        self.assertTrue(1<2, self.getInputData())
        
    def getInputData(self):
        data = super(userlotteAddressTest,self).getInputData()
        itemdata = data.split("\n")
        jsonstr = "{"+",".join(itemdata) + "}"
        dicdata =  eval(jsonstr)
        test = dicdata["memberId"]
        return dicdata
    
if __name__ == '__main__':
    runTestOneCls(casefilepath='D:\\litaojun\\workspace\\uopweixinInterface\\uop\\weixin\\homepage\\userraffleluck.xlsx', testclse=userlotteAddressTest, moduleabspath="D:\\litaojun\\workspace\\uopweixinInterface")