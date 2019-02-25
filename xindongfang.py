import requests
from bs4 import BeautifulSoup
import math
import re
import time

# todo 1、增加登录 2、登录后设置session  3、cookies访问传递
COOKIES = {
    "JSESSIONID": "5A075039C031B23558C0FB49B3B19895"
}
pageUrl = "http://bpm.xdf.cn/studyservice/todo/list?subject=教师4＋1质检&orderByStr=expect_end_time%20desc&=2"
pageParam = {'pageNo': 1}


def classinfo(page):
    pageParam['pageNo'] = page
    req = requests.get(pageUrl, cookies=COOKIES, params=pageParam)
    response = BeautifulSoup(req.text)
    stus = response.find_all(class_='Work_list1')
    for stu in stus:
        date_str = re.split(r'[年|月|日]', stu.find(class_='startBtn').string)
        class_date = '{year}-{month}-{day}'.format(year=date_str[0], month=date_str[1], day=date_str[2])
        now_date = time.strftime("%Y-%m-%d", time.localtime(int(time.time())))
        if class_date >= now_date:
            print('{class_date}课程Pass!!!!!!!!!!!!!!!'.format(class_date=class_date))
            continue
        print('{class_date}课程开始处理......'.format(class_date=class_date))
        classInfo = stu.find(href="javascript:void(0);")
        str = classInfo['onclick'].replace('\'', '').split(',')
        serviceType = str[0].replace('dealwith(', '')
        workObjectNumber = str[1]
        workflowNumber = str[2]
        stuCode = str[3]
        classCode = str[4]
        classParam = {'serviceType': serviceType, 'workObjectNumber': workObjectNumber,
                      'workflowNumber': workflowNumber, 'stuCode': stuCode, 'classCode': classCode}
        print(classParam)
        # classDetail = requests.get('http://bpm.xdf.cn/studyservice/todo/toItemPage', params=classParam, cookies=cookiess)
        # classDetailSoup = BeautifulSoup(classDetail.text, "html.parser")
        # tokenDiv = classDetailSoup.find(type="hidden")
        # classParam.pop('serviceType')
        # classParam.setdefault('token', tokenDiv.attrs['value'])
        # classParam.setdefault('lesson_type', '1')
        # classParam.setdefault('homework_setting', '1')
        # classParam.setdefault('inclass_test', '1')
        # classParam.setdefault('homework_feedback', '1')
        # classParam.setdefault('inclass_feedback', '1')
        # classParam.setdefault('group_interaction', '1')
        # classParam.setdefault('remark', '')
        # finish = requests.get('http://bpm.xdf.cn/workflow/wechatFeedBackNew/finishWechatFeedBackNew', params=classParam, cookies=cookiess)
        # print(finish)
        # print(classParam)
        # print("finish")


pageList = requests.get(pageUrl, cookies=COOKIES, params=pageParam)
cookies = requests.cookies.RequestsCookieJar()
cookies.update(pageList.cookies)
soup = BeautifulSoup(pageList.text)
searchNum = int(soup.find(class_="searchNum").string)
maxPage = math.ceil(searchNum/10)
print('总共有', searchNum, '条，', maxPage, '页数据待处理。。。。。。。。。。。。。。。。。。')
while maxPage >= 1:
    classinfo(maxPage)
    print('处理第', maxPage, '页成功！！！！！！！！！！！！！！！！！！！')
    maxPage -= 1









