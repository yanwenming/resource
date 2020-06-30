#! usr/bin/env python
# -*-coding:utf-8-*-

# author:yanwenming


import unittest
from page.init import *
import requests
from selenium import webdriver
import time as t
import json
import os
import sys

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
print(sys.path)


class YiChangBaobei(Init):
    def test01_Login(self):
        '''工程师正常登录'''
        print ( '执行case1' )
        url = self.default_url1+'v1/app/login'
        param = {"mobile": self.mobile13, "code" : self.code}
        r = requests.post(url, param,verify=False)
        t.sleep(2)
        response1 = r.json()
        self.token = response1['data']['access_token']
        self.assertEqual(response1['status'],200)

        with open('token.txt','w') as f:
            f.write(response1['data']['access_token'])
        t.sleep(1)

    def getToken(self):
        '''读取token文件内容'''
        with open('token.txt','r') as f:
            return f.read()

    def test02_GetExceptionType( self ):
        '''获取异常报备类型数据'''
        print( '\n 执行case2' )
        url = self.default_url1+'v3/work-exception/get-exception-type'
        param = {"access_token" : self.getToken(), "version_code" : '4.5.3.0', "master_no" : 'G180922347'}
        r = requests.get(url, param, verify = False)
        t.sleep( 2 )
        response2 = r.json()
        d = response2['data']
        global b  #存取异常父类ID
        b = []
        for key in d.keys():
            b.append(key)
        print('父类b is :%s' % response2)
        self.assertEqual(response2['message'],'获取成功')

    def test03_GetExceptionChildType (self):
        '''获取异常报备子类数据'''
        print ( '执行case3' )
        for typeid in b:#获取子类ID
            url = self.default_url1 + 'v3/work-exception/get-exception-child-type'
            param = {"access_token": self.getToken (), "version_code" : '4.5.3.0' , "master_no" : 'G180922347',"type": typeid}
            r = requests.get (url, param, verify = False)
            t.sleep (2)
            response3 = r.json()
            zilei = response3['data']
            print('父类 是 %s'% typeid)
            global c
            c = [] #存取异常类型子类ID
            if zilei is not None:
                for m in zilei.keys():
                    c.append(m)
                    self.version_code = '4.5.3.0'
                    url = self.default_url1 + 'v3/work-exception/exception-add?access_token=' + self.getToken () + '&version_code=' + self.version_code
                    param = {'content' : 'Hi, welcome to Beijing 2020' , 'type' : typeid,'work_id' : 'TASK15912603310430' , 'child_type' : m}
                    r = requests.post(url , param , verify = False)
                    t.sleep ( 5 )
                    response4 = r.json()
                    print ( response4 )
                    self.assertEqual ( response4['message'] , 'success' )
                print(typeid+'包含具体的子类型是 %s'% c)


if __name__ == '__main__':
    unittest.main(verbosity = 2)