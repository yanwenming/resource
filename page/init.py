#! usr/bin/env python
# -*-coding:utf-8-*-

# author:yanwenming


import unittest
import requests
from selenium import webdriver


class Init(unittest.TestCase):
    def setUp(self):
        self.mobile = '13651429040'  # 工程师登录账号
        self.master_no = 'G180922344'  # 工程师编号
        self.code = '1234'
        self.version_code = '4.5.3.0'  # 工程师 app 版本号
        self.default_url = 'http://api-master-test.uyess.com/'  # 工程师app
        self.work_id = 'TASK15912603311243' #需要进行异常反馈的工单号
        self.mobile1 = '17717458050'  # 用户登录服务号手机号码
        self.default_url1 = 'https://api-user-test.uyess.com/'  # 服务号地址
        self.qd_no = "uyes_gzh"  # 渠道为公众号
        self.qd_no1 = "uyes_wxopen"  # 渠道为小程序
        # self.qd_no1 = "uyes_gzh"
        self.tag = 0  # 0表示家电模块，1表示家政模块

    # def getToken(self):
    #    with open("tokenvalue.txt",'r') as f:
    #        token=f.read()
    #        return token

