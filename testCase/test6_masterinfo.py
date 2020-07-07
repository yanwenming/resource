#!/usr/bin/env python
# -*-coding:utf-8-*-

# author:Yan Wenming
# create time:2019-12-09

import requests
import unittest
import json
from testCase import test3_createorder
from testCase import createorder
from time import sleep
import pymysql
import time
import datetime
import sys


class master_info(unittest.TestCase):
    '''获取工程师信息'''
    def test6_masterinfo( self ):
        token=createorder.login.test2_getToken( self )
        global order_id
        order_id=test3_createorder.createorder.test3_getOrderid(self)
        sleep(1)
        url='https://api-user-test.uyess.com/v2/order/detail'
        param = {"city_id": 1987, "order_id": order_id, "qd_no": "uyes_gzh",'district_id':1997,'access_token':token}
        r = requests.get( url , param )
        response1 = r.text
        c=json.loads(response1)
        global mastermobile
        mastermobile=c["data"]["master"]["mobile"]#获取订单中的工程师手机号码
        print(mastermobile)
        # with open('masterinfo.txt','r') as f:
        #     f.write(mastermobile)

        sleep(1)

    # @unittest.skip ( "忽略签到订单2" )
    def test7_sql(self):
        '''后台操作数据库'''
        conn = pymysql.connect( host='112.74.112.54', user = 'ptj', password = 'ptj123' , database = 'uyes_standard' , charset = 'utf8' )
        cursor = conn.cursor()
        sql_update="update work set book_day='%s',book_start_time='%s',book_end_time='%s' where order_id='%s'" #更新订单预约上门时间为今天下午14:00-17:00，目前时间写死了
        sql_query1="select access_token from master where mobile=%d"
        sql_query2="select work_id from work where order_id='%s'"
        sql_query3="select finish_verify_code from `order` where order_id='%s'"
        cursor.execute( sql_query1 %(int(mastermobile)))
        rows1 = cursor.fetchone()
        global mastertoken
        mastertoken=rows1[0]
        print(mastertoken)
        sleep(1)

        cursor.execute(sql_query2 %order_id)
        rows2 = cursor.fetchone ()
        global work_id1
        work_id1=rows2[0]
        print(work_id1)
        sleep (1)

        cursor.execute(sql_query3 %order_id)
        rows3=cursor.fetchone()
        global finish_verify1
        finish_verify1=rows3[0]
        sleep (1)
        try:
            for x in range ( 24 ) :
                if x==0:
                    a = datetime.datetime.now ().strftime ( "%Y-%m-%d" ) + " %2d:00:00" % x
                    timeArray = time.strptime ( a , "%Y-%m-%d %H:%M:%S" )
                    timeStamp = int ( time.mktime ( timeArray ) )
                    book_day=timeStamp
                elif x==14:
                    a = datetime.datetime.now ().strftime ( "%Y-%m-%d" ) + " %2d:00:00" % x
                    timeArray = time.strptime ( a , "%Y-%m-%d %H:%M:%S" )
                    timeStamp = int ( time.mktime ( timeArray ) )
                    book_start_time = timeStamp
                elif x==17:
                    a = datetime.datetime.now ().strftime ( "%Y-%m-%d" ) + " %2d:00:00" % x
                    timeArray = time.strptime ( a , "%Y-%m-%d %H:%M:%S" )
                    timeStamp = int ( time.mktime ( timeArray ) )
                    book_end_time = timeStamp
                else:
                    continue
            cursor.execute( sql_update % (book_day , book_start_time , book_end_time , order_id) )  # 向sql语句传递参数
            conn.commit()
        except Exception as e :
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

    # @unittest.skip ("忽略签到订单")
    def test8_qiandao ( self ) :
        '''签到订单'''
        url='http://api-master-test.uyess.com/v3/work/set-workstatus?version_code=4.6.0.0&access_token='+mastertoken
        data={'work_id':work_id1,'address':'中国广东省深圳市南山区边检路','latitude':22.578933,'remark':'系统自动签到20191211','work_status':202,'type':2,'longitude':113.93286}
        re=requests.post(url,data)
        sleep(1)
        r = re.text
        print(r)
        status = json.loads ( r )["status"]
        self.assertEqual ( status , 200 )

    # @unittest.skip ( "忽略签到订单1" )
    def test9_hexiao ( self ) :
        '''核销订单'''
        url='http://api-master-test.uyess.com/v3/work/finish-work?version_code=4.6.0.0&access_token='+mastertoken
        data={'work_id':work_id1,'verify_code':finish_verify1,'work_status':302,'order_id':order_id}
        re=requests.post(url,data)
        r1 = re.text
        print(r1)
        status = json.loads ( r1 )["status"]
        self.assertEqual ( status , 200 )
