#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Created on 2017

@author: li.taojun
'''
# custom HTTPS opener, banner's oracle 10g server supports SSLv3 only
import httplib, ssl, urllib2, socket
import requests,json
class HTTPSConnectionV3(httplib.HTTPSConnection):
    def __init__(self, *args, **kwargs):
        httplib.HTTPSConnection.__init__(self, *args, **kwargs)
        
    def connect(self):
        sock = socket.create_connection((self.host, self.port), self.timeout)
        if self._tunnel_host:
            self.sock = sock
            self._tunnel()
        try:
            self.sock = ssl.wrap_socket(sock, self.key_file, self.cert_file, ssl_version=1)
        except ssl.SSLError, e:
            print("Trying SSLv3.")
            self.sock = ssl.wrap_socket(sock, self.key_file, self.cert_file, ssl_version=2)
            
class HTTPSHandlerV3(urllib2.HTTPSHandler):
    def https_open(self, req):
        return self.do_open(HTTPSConnectionV3, req)
# install opener
urllib2.install_opener(urllib2.build_opener(HTTPSHandlerV3()))

if __name__ == "__main__":
#     r = urllib2.urlopen("https://ui2web1.apps.uillinois.edu/BANPROD1/bwskfcls.P_GetCrse")
#     print(r.read())
      url = 'https://uat-uop-api.opg.cn/activities-service/raffle/getRaffleAllInfoByRaffleId'
      hearder = {
                 'memberId':'d3fa3fee-0f89-4f9a-bf38-75fedb8c8f95',
                 'openid':'oLTtnwcieZIRRFe0lT8B8VkFaRAk'
                }
      data = {
              "memberId":"d3fa3fee-0f89-4f9a-bf38-75fedb8c8f95",
              "raffleId":"1ab56994-5b22-413e-933f-b7a7b59e264d"
             }
      #requests.get()
      print "1"
      r = requests.post(url=url,json=data,headers=hearder)
      print "2"
      print r.text
      