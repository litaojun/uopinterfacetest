#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017

@author: li.taojun
'''
from com.uop.util.schemajson import check_rspdata,Validator
import json
from jsonschema import validate

userCenterScma = {
                        "type":"object",
                         "properties":{
                                        "code": {"type":"string"},
                                        "message": {"type":"string"},
                                        "data": {
                                                   "type":"object",
                                                    "properties":{
                                                                    "start": {"type":"number"},
                                                                    "pageSize":  {"type":"number"},
                                                                    "currentPage":  {"type":"number"},
                                                                    "recordsTotal":  {"type":"number"},
                                                                    "data": {
                                                                             "type":"array",
                                                                            'items': {  
                                                                                     "type":"object",
                                                                                      "properties":{
                                                                                                        "id": {"type":"string"},
                                                                                                        "orderNo": {"type":"string"},
                                                                                                         #"memberId": {"type":"string"},
                                                                                                         #"orderPrice": {"type":"number"},
                                                                                                         #"payPrice":{"type":"number"},
                                                                                                          #"createTime": {"type":"number"},
    #                                                                                                     "updateTime": null,
    #                                                                                                     "payTime": null,
    #                                                                                                     "deliveryTime": null,
    #                                                                                                     "finishTime": null,
                                                                                                        "orderStatus": {"type":"string"},
                                                                                                        #"memberMsg": {"type":"string"},
                                                                                                        #"receiveAddressId": {"type":"string"},
                                                                                                        "receiveAddress": {"type":"string"},
                                                                                                        "orderType": {"type":"string"},
    #                                                                                                     "remark": null,
                                                                                                        "details": {
                                                                                                                     "type":"array",
                                                                                                                    'items': {  
                                                                                                                             "type":"object",
                                                                                                                              "properties":{
                                                                                                                                                "id": {"type":"string"},
                                                                                                                                                "orderId": {"type":"string"},
                                                                                                                                                "itemId": {"type":"string"},
                                                                                                                                                "buyCount": {"type":"number"},
                                                                                                                                                #"itemTitle": {"type":"string"},
                                                                                                                                                #"itemPrice": {"type":"number"},
    #                                                                                                                                             "itemOriginalPrice": null,
    #                                                                                                                                             "itemCostPrice": null,
                                                                                                                                                "skuId": {"type":"string"},
                                                                                                                                                "picPath": {"type":"string"},
    #                                                                                                                                             "skuDesc": null,
    #                                                                                                                                             "distribution": null,
                                                                                                                                                #"activityAddress":{"type":"string"},
                                                                                                                                                "point": {"type":"number"},
    #                                                                                                                                             "memberId": null,
    #                                                                                                                                             "prizeId": null,
    #                                                                                                                                             "prizeTitle": null,
    #                                                                                                                                             "prizePic": null,
    #                                                                                                                                             "raffleResultId": null
    
                                                                                                                                            },
                                    #                                                                                                     "memberName": null,
                                    #                                                                                                     "phone": null,
                                                                                                                                        "createTimeStr":{"type":"string"},
                                    #                                                                                                     "expressCompany": null,
                                    #                                                                                                     "expressNo": null,
                                    #                                                                                                     "ticketNo": null,
                                    #                                                                                                     "activityTimeDesc": null,
                                    #                                                                                                     "activityAddress": null,
                                    #                                                                                                     "updateTimeStr": null,
                                    #                                                                                                     "payTimeStr": null,
                                    #                                                                                                     "deliveryTimeStr": null,
                                    #                                                                                                     "payExpiryTimeStr": null,
                                    #                                                                                                     "deliveryType": null,
                                                                                                                                        "totalPoints": {"type":"number"}
                                                                                                                                   }
                                                                                            
                                                                                                                                        },
                                            #                                                                 "draw": null,
                                                                                                            "recordsFiltered": {"type":"number"},
                                                                                                            "pageNum":{"type":"number"},
                                                                                                            "startRow": {"type":"number"},
                                                                                                            "pages": {"type":"number"},
                                                                                                            "endRow":{"type":"number"},
                                                                                                            "startIndex": {"type":"number"}
                                                                                                        }
                                                                                            }
                                                                                }
                                                                    }
                                                        }
                                                }
                            }

validator = Validator(userCenterScma)
#
@check_rspdata(validator)
def parseUserPointByRspJSON(response=None):
    #addressjson = response.TEXT\
    print "response=%s" % str(response)
    actvidlist = []
    return response
    


if __name__ == '__main__':
    curjson = {
                        "code": "000000",
                        "message": "成功",
                        "data": {
                                    "start": 0,
                                    "pageSize": 10,
                                    "currentPage": 1,
                                    "recordsTotal": 3,
                                    "data": [
                                                {
                                                    "id": "891787e0-395a-474c-9c03-89946fa5a2df",
                                                    "orderNo": "20171122202514930",
                                                    "memberId": "997da560-6de2-4056-8614-e7cd95dd967b",
                                                    "orderPrice": 0.00,
                                                    "payPrice": 0.00,
                                                    "createTime": 1511353518000,
                                                    "updateTime": None,
                                                    "payTime": None,
                                                    "deliveryTime": None,
                                                    "finishTime": None,
                                                    "orderStatus": "11",
                                                    "memberMsg": "",
                                                    "receiveAddressId": "77b7914a-cdd3-11e7-aa44-02cab2901bce",
                                                    "receiveAddress": "李涛军,18916899938,北京市市辖区东城区今年",
                                                    "orderType": "02",
                                                    "remark": None,
                                                    "details": [
                                                                    {
                                                                        "id": "a810ed37-20d5-4baa-8bf3-e984b0f8870e",
                                                                        "orderId": "891787e0-395a-474c-9c03-89946fa5a2df",
                                                                        "itemId": "3a08b22d-bf96-4a7c-8229-b4c69b78ace6",
                                                                        "buyCount": 1,
                                                                        "itemTitle": "曹华楠商品购买测试1",
                                                                        "itemPrice": 0.00,
                                                                        "itemOriginalPrice": None,
                                                                        "itemCostPrice": None,
                                                                        "skuId": "954e9e90-1a8f-4cd0-b236-26f9c7306a9c",
                                                                        "picPath": "http://dev-uop-wx.opg.cn/_static/images/item/3a08b22d-bf96-4a7c-8229-b4c69b78ace6/20171120171413_296873.jpg",
                                                                        "skuDesc": None,
                                                                        "distribution": None,
                                                                        "activityAddress": "测试用的",
                                                                        "point": 1,
                                                                        "memberId": None,
                                                                        "prizeId": None,
                                                                        "prizeTitle": None,
                                                                        "prizePic": None,
                                                                        "raffleResultId": None
                                                                    }
                                                                ],
                                                    "memberName": None,
                                                    "phone": None,
                                                    "createTimeStr": "2017-11-22 20:25:18",
                                                    "expressCompany": None,
                                                    "expressNo": None,
                                                    "ticketNo": None,
                                                    "activityTimeDesc": None,
                                                    "activityAddress": None,
                                                    "updateTimeStr": None,
                                                    "payTimeStr": None,
                                                    "deliveryTimeStr": None,
                                                    "payExpiryTimeStr": None,
                                                    "deliveryType": None,
                                                    "totalPoints": 1
                                                },
                                        {
                                            "id": "cb91a1cf-b1dc-49c2-9088-12f2815569ef",
                                            "orderNo": "20171122192710131",
                                            "memberId": "997da560-6de2-4056-8614-e7cd95dd967b",
                                            "orderPrice": None,
                                            "payPrice": None,
                                            "createTime": 1511350030000,
                                            "updateTime": 1511350049000,
                                            "payTime": 1511350030000,
                                            "deliveryTime": None,
                                            "finishTime": None,
                                            "orderStatus": "12",
                                            "memberMsg": None,
                                            "receiveAddressId": "77b7914a-cdd3-11e7-aa44-02cab2901bce",
                                            "receiveAddress": "李涛军,18916899938,北京市市辖区东城区今年",
                                            "orderType": "03",
                                            "remark": None,
                                            "details": [
                                                            {
                                                                "id": "ec61e265-f23e-4bdd-b45c-b615203b2597",
                                                                "orderId": "cb91a1cf-b1dc-49c2-9088-12f2815569ef",
                                                                "itemId": "e9b5f4f3-a9a7-474d-a04c-070bdcc61d52",
                                                                "buyCount": 1,
                                                                "itemTitle": "曹华楠 刮刮乐测试1",
                                                                "itemPrice": None,
                                                                "itemOriginalPrice": None,
                                                                "itemCostPrice": None,
                                                                "skuId": "6b7ff045-d643-4234-9f36-6512288a129d",
                                                                "picPath": "http://dev-uop-wx.opg.cn/_static/images/raffle/20171121111440_257506.jpg",
                                                                "skuDesc": None,
                                                                "distribution": None,
                                                                "activityAddress": None,
                                                                "point": 0,
                                                                "memberId": None,
                                                                "prizeId": "2f938949-232b-4dfb-8350-6d27a22ca2f9",
                                                                "prizeTitle": "曹华楠 刮刮乐测试1",
                                                                "prizePic": "http://dev-uop-wx.opg.cn/_static/images/raffle/20171121111349_294376.jpg",
                                                                "raffleResultId": "4237ee61-d0e1-4bb2-b030-9eb6348a749c"
                                                            }
                                                    ],
                                            "memberName": None,
                                            "phone": None,
                                            "createTimeStr": "2017-11-22 19:27:10",
                                            "expressCompany": None,
                                            "expressNo": None,
                                            "ticketNo": None,
                                            "activityTimeDesc": None,
                                            "activityAddress": None,
                                            "updateTimeStr": None,
                                            "payTimeStr": None,
                                            "deliveryTimeStr": None,
                                            "payExpiryTimeStr": None,
                                            "deliveryType": None,
                                            "totalPoints": 0
                                        },
                                        {
                                            "id": "1b37b8e3-4554-44b4-8ea6-02a1a7c67b6c",
                                            "orderNo": "20171122102137111",
                                            "memberId": "997da560-6de2-4056-8614-e7cd95d548d967b",
                                            "orderPrice": None,
                                            "payPrice": None,
                                            "createTime": 1511317297000,
                                            "updateTime": None,
                                            "payTime": 1511317297000,
                                            "deliveryTime": None,
                                            "finishTime": None,
                                            "orderStatus": "10",
                                            "memberMsg": None,
                                            "receiveAddressId": None,
                                            "receiveAddress": "None,None,None",
                                            "orderType": "03",
                                            "remark": None,
                                            "details": [
                                                            {
                                                                "id": "40ef7e2b-331d-4180-a42e-77ac62e1a6ea",
                                                                "orderId": "1b37b8e3-4554-44b4-8ea6-02a1a7c67b6c",
                                                                "itemId": "8754fe84-8e78-4a95-a224-a8a6d7b9768f",
                                                                "buyCount": 1,
                                                                "itemTitle": "大转盘活动",
                                                                "itemPrice": None,
                                                                "itemOriginalPrice": None,
                                                                "itemCostPrice": None,
                                                                "skuId": "8b3f36cf-88c6-4df9-a507-70364080f6df",
                                                                "picPath": "http://dev-uop-wx.opg.cn/_static/images/raffle/20171121103547_413371.jpg",
                                                                "skuDesc": None,
                                                                "distribution": None,
                                                                "activityAddress": None,
                                                                "point": 0,
                                                                "memberId": None,
                                                                "prizeId": "d9b25f46-d02f-41b8-acae-43e0e5a59f02",
                                                                "prizeTitle": "文字",
                                                                "prizePic": "http://dev-uop-wx.opg.cn/_static/images/raffle/20171121105708_966181.jpg",
                                                                "raffleResultId": "5da6dd2c-36ca-4ad6-81e0-f6b2189f3df1"
                                                            }
                                                      ],
                                            "memberName": None,
                                            "phone": None,
                                            "createTimeStr": "2017-11-22 10:21:37",
                                            "expressCompany": None,
                                            "expressNo": None,
                                            "ticketNo": None,
                                            "activityTimeDesc": None,
                                            "activityAddress": None,
                                            "updateTimeStr": None,
                                            "payTimeStr": None,
                                            "deliveryTimeStr": None,
                                            "payExpiryTimeStr": None,
                                            "deliveryType": None,
                                            "totalPoints": 0
                                        }
                                    ],
                                    "draw": None,
                                    "recordsFiltered": 1,
                                    "pageNum": 1,
                                    "startRow": 0,
                                    "pages": 1,
                                    "endRow": 9,
                                    "startIndex": 0
                        }
                    }
    #a = parseUserPointByRspJSON(response=curjson)
    validate(curjson,userCenterScma)
    list()