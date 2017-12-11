#!/usr/bin/env python
# -*- coding:utf-8 -*-
# File: http_get.py
'''
Created on 2017
import urllib2
@author: li.taojun
'''
# import urllib2,json
# import urllib
# def http_get(url="",param={},httpheaders={}):
#     if len(param.keys()) > 0 :
#         textmod = urllib.urlencode(param)
#         req = urllib2.Request(url = '%s%s%s' % (url,'?',textmod))
#     else:
#         req = urllib2.Request(url)
#     for key in httpheaders.keys():
#         req.add_header(key,httpheaders[key])
#     res = urllib2.urlopen(req)
#     res = res.read()
#     return res
# 
# def http_get_param_tranc(param = {}):
#     textmod = urllib.urlencode(param)
#     print(textmod)
#     return textmod
# 
# def http_get_url(httpurl=""):
#    # url='http://192.168.1.13:9999/test'   #页面的地址
#     response = urllib2.urlopen(httpurl)         #调用urllib2向服务器发送get请求
#     rspdata = response.read() 
#     return rspdata
# 
# def http_post(url="",param={},httpheadrs={}):
#     #url='http://192.168.1.13:9999/test'
#     #values = {'user':'Smith','passwd':'123456'}
#     jdata = json.dumps(param)             # 对数据进行JSON格式化编码
#     req = urllib2.Request(url, jdata)       # 生成页面请求的完整数据
#     req.add_header("Content-Type", "application/json;charset=utf8")
#     for key in httpheadrs.keys():
#         req.add_header(key,httpheadrs[key])
#     response = urllib2.urlopen(req)       # 发送页面请求
#     return response.read()                    # 获取服务器返回的页面信息


if __name__ == '__main__':
    pass
    #print http_get_url(httpurl="http://localhost:12306/hello")