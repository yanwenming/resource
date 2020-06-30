#! usr/bin/env python
# -*-coding:utf-8-*-

# author:yanwenming


import unittest
import requests
from selenium import webdriver


class Init(unittest.TestCase):
    def setUp( self ):
        self.mobile1 = '13510642540'  # 单品用户
        self.mobile2 = '13510642541'  # 单品用户
        self.mobile3 = '13510642542'  #台卡用户
        self.mobile4 = '13510646060'  #测试家电订单派指定服务商
        self.mobile5 = '13510646061'  # 测试家电订单派指定服务商
        self.mobile6 = '13510646062'  # 测试家电订单派指定服务商
        self.mobile7 = '13510644040'   #包年96次用户
        self.mobile8 = '13510644041'   #包年48次用户
        self.mobile9 = '13510644042'  # 包年24次用户
        self.mobile10 = '13510644043'  # 包年12次用户
        self.mobile11 = '13510644044'  # 家政初体验用户
        self.mobile12 = '13510644045'  # 家政单次用户
        self.mobile13 = '15014040016'
        self.code = '1234'
        self.qd_no = 'uyes_gzh'
        self.district_id = '1997' #南山区
        self.district_id1 = '1994'  # 福田区 测试家电订单派指定服务商
        self.district_id2 = '1990' #盐田区
        self.default_url='https://api-user-test.uyess.com/'
        self.default_url1 = 'http://api-master-test.uyess.com/' #工程师app
        self.province_id = '1895' #广东省
        self.city_id = '1987'  #深圳市
        self.street_code1 = '440305009' #西丽街道  单品
        self.street_code2 = '440305007' #粤海街道  套餐
        self.street_code3 = '440305007' #沙河街道  台卡
        self.street_code4 = '440305002' #测试家电订单派指定服务商 南山街道
        self.street_code5 = '440304001'  # 测试家电订单派指定服务商 南园街道
        self.street_code6 = '440308001' #梅沙街道
        self.pay_type = 'wallet' #钱包支付
        self.trade_type = 'order'
        self.date = '2020-07-06' # 预约上门时间，日期
        self.time = '09:00-12:00' #预约上门时间，具体上门时间点
        self.date1 = '2020-07-06'  #测试家电订单派指定服务商
        self.time1 = '14:00-17:00'  # 预约上门时间，具体上门时间点 测试家电订单派指定服务商
        self.time2 = '18:00-21:00' #晚上

    # def getToken(self):
    #    with open("tokenvalue.txt",'r') as f:
    #        token=f.read()
    #        return token

