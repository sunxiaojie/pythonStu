import requests
from bs4 import BeautifulSoup

cookiess = {
    "JSESSIONID": "1500956D798AEE42A8DC25F5CA0C28ED",
    "pageNo": "3",
    "pageSize": "10"
}
payload = {'pageNo': 2}
continueStr = '21日'

url = "http://bpm.xdf.cn/studyservice/todo/list?subject=教师4＋1质检&orderByStr=expect_end_time%20desc&=2"
req = requests.get( url, cookies=cookiess, params=payload)
cookies = requests.cookies.RequestsCookieJar()
cookies.update(req.cookies)
soup = BeautifulSoup(req.text)
print(soup.find_all(class_="saucy"))
stus = soup.find_all(class_='Work_list1')
for stu in stus:
    startBtn = stu.find(class_='startBtn')
    if startBtn.string.find(continueStr)>0:
        continue
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
    classParam.pop('serviceType')
    classParam.setdefault('token', tokenDiv.attrs['value'])
    classParam.setdefault('lesson_type', '1')
    classParam.setdefault('homework_setting', '1')
    classParam.setdefault('inclass_test', '1')
    classParam.setdefault('homework_feedback', '1')
    classParam.setdefault('inclass_feedback', '1')
    classParam.setdefault('group_interaction', '1')
    classParam.setdefault('remark', '')
    finish = requests.get('http://bpm.xdf.cn/workflow/wechatFeedBackNew/finishWechatFeedBackNew', params=classParam, cookies=cookiess)
    print(finish)
    print(classParam)
    print("finish")
    # print(classParam)


    # print(classCode)

# print(soup)
# print(req.text)




