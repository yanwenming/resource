#!/usr/bin/env python
# -*-coding:utf-8-*-

# author:Yan Wenming
# create time:2020-07-17

import requests
import unittest
from time import sleep
from page.init import *
import random
import json
import datetime


class JiaDianOrder ( Init ) :
    '''用户从服务号登录，到预约订单'''

    def test1_tologin ( self ) :
        '''用户登录小程序/服务号'''
        url = self.default_url1 + "v2/user/login"
        param = {"mobile" : self.mobile1 , "code" : self.code , "qd_no" : self.qd_no1}
        r = requests.get ( url , param , verify = False)
        response1 = r.json()
        # print('我是：',response1['data']['user_access_token'])
        with open( 'token.txt' , 'w' ) as f :
            f.write ( response1['data']['user_access_token'] )
        sleep ( 1 )

    def getToken( self ):
        '''读取token文件内容'''
        with open( 'token.txt' , 'r' )as f:
            return f.read()

    def test2_OutputAddressid( self ):
        '''列出用户服务地址'''
        url = self.default_url1 + "v2/user/get-address-list?"
        param = {"access_token" : self.getToken () , "qd_no" : self.qd_no1}
        response = requests.get( url , param , verify = False )
        r = response.text
        total = len(json.loads(r)["data"])
        if total==0:
            def addaddress( self ) :
                '''用户创建服务地址'''
                url = self.default_url1 + "v2/user/add-address?" + "qd_no=" + self.qd_no1 + "&district_id=1990&access_token=" + self.getToken ()
                form_data = {'username' : '研发' + random.choice ( "深圳欢迎您南山宝安福田罗湖龙岗株洲长沙" ) , 'sex' : '' ,
                             'phone' : self.mobile1 , 'province_id' : 1895 , 'city_id' : 1987 ,
                             'district_id' : 1990 , 'address' : '梅沙街道办事处行政服务大厅' , 'house_num' : '2栋202' ,
                             'sys_province_id' : 1895 ,
                             'sys_city_id' : 1987 , 'sys_district_id' : 1990 , 'sys_street_code' : 440308001 ,
                             'street_code' : 440308001 , 'qd_no' : self.qd_no1}
                data = form_data
                # print(url)
                response = requests.post( url , data , verify = False )
                r = response.text
                address_id = json.loads(r)["data"]["id"]
                print(address_id)

                with open('addressid.txt' , 'w') as f :
                    f.write(str(address_id))
                sleep(1)

        elif total == 1:
            address_id=json.loads(r)["data"][0]["id"]
            with open ('addressid.txt', 'w' ) as f :
                f.write (str(address_id))

        else :
            a = []
            for i in range(total):
                a.append(json.loads(r)["data"][i]["id"])
                # print(a)
            url = self.default_url1 + "v2/user/delete-address?" + "qd_no=" + self.qd_no1 + "&district_id=1997&access_token=" + self.getToken ()
            for b in range(len(a)-1):
                param = {"access_token" : self.getToken () , "qd_no" : self.qd_no1,"id":a[b],"district_id":1990}
                response = requests.get( url , param , verify = False )
            address_id = a[0]
            with open ('addressid.txt', 'w' ) as f :
                f.write (str(address_id))

    def getAddressid( self ) :
        with open("addressid.txt",'r') as f:
           return f.read()

    def ReadAddressid ( self ) :
        addressid = self.getAddressid ()
        print('addressid is '+addressid)

    def test3_createorder(self):
        '''用户购买服务商品'''
        # now_time=datetime.datetime.now()
        # book_day=(now_time+datetime.timedelta(days=+25)).strftime("%Y-%m-%d")#设置预约时间
        addressid = self.getAddressid()
        url = self.default_url1 + "v2/order/add-order?qd_no="+self.qd_no1+"&district_id=1990&access_token=" + self.getToken()
        if self.tag == 1:
            # 此处的form data为家政单品
            form_data = {"address_id": int(addressid), "order_source": 2, "carts": [], "goods": [
            {"goods_no": "793511395600", "activity_id": 0, "num": 1, "item_id": "311", "price": "0.01",
             "goods_item_id": "311", "ref_no": "sku05395949177948"}] , "redpacket_id": "",
                     "book_day": "", "book_period": "", "user_remark": "订单备注",
                     "mix_goods" : "" , "mix_book_day" : "" , "mix_book_period" : ""}
        else:
            # 此处的form data为家电单品
            form_data = {"address_id": int(addressid), "order_source": 2, "carts": [], "goods": [
            {"goods_no": "169857542500", "activity_id": 0, "num" : 1, "item_id" : "381", "price": "0.02",
             "goods_item_id": "381", "ref_no": "sku05278549732225"}], "redpacket_id": "",
                     "book_day": "", "book_period": "", "user_remark": "订单备注",
                     "mix_goods": "" , "mix_book_day": "" , "mix_book_period" : ""}
        data2 = json.dumps(form_data)
        data = {'data': data2,'qd_no':self.qd_no1, 'referee_no':''}
        respone = requests.post(url ,data,verify = False)
        # global order_id
        r = respone.text  # new
        print(r)
        order_id = json.loads ( r )["data"]["order_id"]
        with open('orderid.txt','w') as f:
            f.write(order_id)
        sleep(1)
        message1 = json.loads ( r )["message"]
        self.assertEqual ( message1 , "SUCCESS" )

    def getOrderid( self ) :
        with open('orderid.txt','r') as f:
           return f.read()

    # @unittest.skip ( "忽略支付" )
    def test4_topayorder( self ):
        '''用户支付订单'''
        order_id = self.getOrderid()
        sleep ( 2 )
        url = self.default_url1 + 'payment/unified-pay/pay'
        param = {"pay_type" : "wallet" , "trade_type" : "order" , "qd_no" : self.qd_no1, 'district_id' : 1990 ,
                 'access_token' : self.getToken(), 'trade_id' : order_id}
        response = requests.get(url , param, verify = False)
        print (response)
        r = response.text
        status = json.loads(r)["status"]
        self.assertEqual ( status , 200 )

    def test5_booktime( self ) :
        '''用户预约上门服务时间'''
        sleep( 2 )
        url = self.default_url1 + '/v2/order/modify-date?access_token=' + self.getToken() + '&qd_no=' + self.qd_no1 + '&district_id=1990'
        param = {"order_id" : self.getOrderid(), "date" : "2020-07-24" , "time" : "09:00-12:00" , 'type' : "" ,
                 'confirm_type' : "", 'qd_no' : self.qd_no1}
        response = requests.post(url , param, verify = False)
        print (response)
        r = response.text
        status = json.loads(r)["status"]
        self.assertEqual( status , 200 )


if __name__ == '__main__' :
    unittest.main ( verbosity = 2 )
