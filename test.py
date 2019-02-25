import requests
from bs4 import BeautifulSoup
import re
import json
import math
from DateTime import  DateTime
import time
import re

cookies = requests.cookies.RequestsCookieJar()
cookies['1'] = '1111111111'
pageUrl = "http://bpm.xdf.cn/i/u7/index.aspx"
pagePage = requests.get(pageUrl)
cookies.update(pagePage.cookies)
print(cookies)
# print(pagePage.text)
soup = BeautifulSoup(pagePage.text)
print(soup.find(id="__VIEWSTATE").attrs['value'])
print(soup.find(id="__VIEWSTATEGENERATOR").attrs['value'])
param = {}
param.setdefault('__VIEWSTATE', soup.find(id="__VIEWSTATE").attrs['value'])
param.setdefault('__VIEWSTATEGENERATOR', soup.find(id="__VIEWSTATEGENERATOR").attrs['value'])
param.setdefault('txtUser', 'zhaoxia4@xdf.cn')
param.setdefault('txtPwd', 'xia*0020')
param.setdefault('txtVCode', '')
param.setdefault('btnLogin', '登录中...')
homePage = requests.post('http://passport.xdf.cn/i/u7/index.aspx', data=param)
cookies.update(homePage.cookies)
print(cookies)
# print(homePage.text)
print(homePage.cookies['JSESSIONID'])