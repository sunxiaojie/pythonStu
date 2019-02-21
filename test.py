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
payload = {'serviceType':'51','workObjectNumber':'d0c79a34b0104fbdbf7118f07973559b','workflowNumber':'d0c79a34b0104fbdbf7118f07973559b','stuCode':'BJ2056545','classCode':'VIPTVS190045','subject':'微信群4＋1服务动作反馈'}
url = "http://bpm.xdf.cn/studyservice/todo/toItemPage"
req = requests.get(url, cookies=cookiess, params=payload)
soup = BeautifulSoup(req.text, "html.parser")
token = soup.find(type="hidden")
print(token.attrs['value'])