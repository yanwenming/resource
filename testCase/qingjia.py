#! usr/bin/env python
# -*-coding:utf-8-*-

# author:yanwenming
# date:2020-06-30


import unittest
from page.init import *
import requests
import time as t
import os
import sys

curPath = os.path.abspath ( os.path.dirname ( __file__ ) )
rootPath = os.path.split ( curPath )[0]
sys.path.append ( rootPath )
print ( sys.path )


class YiChangBaobei ( Init ) :
    '''
    用于工程师在APP上进行请假操作
    '''

    def test01_Login ( self ) :
        '''工程师正常登录'''
        print ( '执行case1' )
        url = self.default_url + 'v1/app/login'
        param = {"mobile" : self.mobile , "code" : self.code}
        r = requests.post ( url , param , verify = False )
        t.sleep ( 2 )
        response1 = r.json ()
        self.token = response1['data']['access_token']
        self.assertEqual( response1['status'] , 200 )

        with open ( 'token.txt' , 'w' ) as f :
            f.write ( response1['data']['access_token'] )
        t.sleep ( 1 )

    def getToken ( self ) :
        '''读取token文件内容'''
        with open ( 'token.txt' , 'r' ) as f :
            return f.read ()

    def test02_GetWeek ( self ) :
        '''获取异常报备类型数据'''
        print( '\n 执行case2' )
        url = self.default_url + 'v4/worker-plan/get-week'
        param = {"access_token" : self.getToken () , "version_code" : self.version_code , "master_no" : self.master_no}
        r = requests.get(url , param , verify = False)
        t.sleep ( 2 )
        response2 = r.json ()
        print ( response2 )
        d = response2['data']
        # res = [item[key] for item in d for key in item]
        # print(res)
        global b  #存取前端展示的日期
        b = []
        for value in d.values():
            b.append(value.split('（')[0])
        print('b is :%s' % b)
        self.assertEqual ( response2['message'] , '获取成功' )




    def test03_LeaveApplication ( self ) :
        '''获取异常报备类型数据'''
        print ( '\n 执行case3' )
        for riqing in b:
            url = self.default_url + 'v4/worker-plan/leave-application?access_token=' + self.getToken () + '&version_code=' + self.version_code + '&master_no=' + self.master_no
            param = {"master_no" : self.master_no , "date_time" : riqing, "content" : '我要请假'}
            r = requests.post( url , param , verify = False )
            t.sleep ( 2 )
            response3 = r.json ()
            print ( response3 )


if __name__ == '__main__':
    unittest.main(verbosity = 2)