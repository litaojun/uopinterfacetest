#!/usr/bin/env python
# -*- coding:utf-8 -*-
# File: http_get.py
'''
Created on 2017

@author: li.taojun
'''
import json
import requests
#http://docs.python-requests.org/zh_CN/latest/user/quickstart.html#post
def getopr():
    r = requests.get('https://github.com/timeline.json')
    r = requests.post("http://httpbin.org/post")
    
    payload = {'key1': 'value1', 'key2': 'value2'}
    r = requests.get("http://httpbin.org/get", params=payload)
    print(r.url)
    
    payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
    r = requests.get('http://httpbin.org/get', params=payload)
    print(r.url)
    
    r = requests.get('https://github.com/timeline.json')
    print(r.text)
    print(r.encoding)
    
    print(r.content) #你也能以字节的方式访问请求响应体，对于非文本请求：
    
    r = requests.get('https://github.com/timeline.json')
    print r.status_code       #JSON 响应内容
    print r.json()
    
    #定制请求头
    url = 'https://api.github.com/some/endpoint'
    headers = {'user-agent': 'my-app/0.0.1'}
    r = requests.get(url, headers=headers)
    
    payload = {'key1': 'value1', 'key2': 'value2'}
    r = requests.post("http://httpbin.org/post", data=payload)
    print(r.text)
    
    
    payload = (('key1', 'value1'), ('key1', 'value2'))
    r = requests.post('http://httpbin.org/post', data=payload)
    print(r.text)
    
    url = 'https://api.github.com/some/endpoint'
    payload = {'some': 'data'}
    r = requests.post(url, data=json.dumps(payload))
    r = requests.post(url, json=payload)
    
    url = 'http://httpbin.org/post'
    files = {'file': open('report.xls', 'rb')}
    r = requests.post(url, files=files)
    print r.text
    
    files = {'file': ('report.xls', open('report.xls', 'rb'), 'application/vnd.ms-excel', {'Expires': '0'})}
    r = requests.post(url, files=files)
    
    #抛出异常
    r.raise_for_status()
    

if __name__ == '__main__':
    pass