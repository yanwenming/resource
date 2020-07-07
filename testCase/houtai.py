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
# print ( sys.path )


url = 'http://ptj-test.uyess.com/'
client = requests.session()
client.get(url)
if '_csrf' in client.cookies:
    csrftoken = client.cookies['_csrf']
else:
    csrftoken = client.cookies['_csrf']
print (csrftoken)