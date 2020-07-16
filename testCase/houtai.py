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
from bs4 import BeautifulSoup
from lxml import etree

curPath = os.path.abspath ( os.path.dirname ( __file__ ) )
rootPath = os.path.split( curPath )[0]
sys.path.append ( rootPath )
# print ( sys.path )


url = 'http://ptj-test.uyess.com/'
r = requests.get(url)
# print(r.text)

with open('index.html', mode='w', encoding='gbk') as f:
            f.write(r.text)


def parse_data():
    with open('index.html', mode='r', encoding='gbk') as f:
        html = f.read()
        #  创建BeautifulSoup实例，解析html数据
        # 指定使用html解析器parser
        bs = BeautifulSoup(html, 'html.parser')

        #查找数据
        # 1.find()方法，获取第一个匹配的标签
        # div = bs.find('div')
        # print(div)
        # print(type(div))  # Tag类型

        # 2.find_all()方法，获取所有匹配的标签
        metas = bs.find_all('meta')  # 返回的是集合
        print(metas)
        # print(bs.find_all(id='hello'))  # 根据id获取，返回的是集合
        # print(bs.find_all(class_='itany'))  # 根据class获取

        # 3.select()方法，使用CSS选择器来获取元素
        # print(bs.select('#hello'))
        # print(bs.select('.itany'))
        # print(bs.select('p#world span'))
        # print(bs.select('[title]'))

        # 4.get_text()方法，获取Tag中的文本
        # value = bs.select('#hello')[0].get_text()
        # # print(len(value))
        # print(value)

# client = requests.session()
# client.get(url)
# if '_csrf' in client.cookies:
#     csrftoken = client.cookies['_csrf']
# else:
#     csrftoken = client.cookies['_csrf']
# print (csrftoken)