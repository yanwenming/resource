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

    # def getToken(self):
    #    with open("tokenvalue.txt",'r') as f:
    #        token=f.read()
    #        return token

