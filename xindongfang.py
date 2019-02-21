import requests
from bs4 import BeautifulSoup
import re
import json

def load_pic(url):
    response = requests.get(url)
    return response.content

# res = requests.get('http://www.nipic.com/topic/show_27202_1.html')

cookiess = {
    "JSESSIONID": "A29CDB2595A07B0F04BACA5265D5730A",
    "pageNo": "3",
    "pageSize": "10"
}
ssrequest = requests.session()
# requests.utils.add_dict_to_cookiejar(ssrequest.cookies, cookiess)
url = "http://bpm.xdf.cn/studyservice/todo/list?subject=教师4＋1质检&orderByStr=expect_end_time%20desc&=2"
payload = {'pageNo': 2}
req = requests.get( url, cookies=cookiess, params=payload)
cookies = requests.cookies.RequestsCookieJar()
cookies.update(req.cookies)
soup = BeautifulSoup(req.text)
print(soup.find_all(class_="saucy"))
# print(soup.find_all(string='下一页'))
stus = soup.find_all(class_='Work_list1')
for stu in stus:
    startBtn = stu.find(class_='startBtn')
    print(startBtn.string)
    classInfo = stu.find(href="javascript:void(0);")
    str = classInfo['onclick'].replace('\'', '').split(',')
    serviceType = str[0].replace('dealwith(','')
    workObjectNumber = str[1]
    workflowNumber = str[2]
    stuCode = str[3]
    classCode = str[4]
    classParam = {'serviceType':serviceType, 'workObjectNumber':workObjectNumber, 'workflowNumber':workflowNumber, 'stuCode':stuCode, 'classCode':classCode}
    print(classParam)
    classDetail = requests.get('http://bpm.xdf.cn/studyservice/todo/toItemPage', params=classParam, cookies=cookiess)
    classDetailSoup = BeautifulSoup(classDetail.text, "html.parser")
    tokenDiv = classDetailSoup.find(type="hidden")
    print(tokenDiv)
    print(tokenDiv.attrs['value'])

    # print(classCode)

# print(soup)
# print(req.text)




