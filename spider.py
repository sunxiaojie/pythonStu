import requests
import re
import json

def load_pic(url):
    response = requests.get(url)
    return response.content

res = requests.get('http://www.nipic.com/topic/show_27202_1.html')

reg = r'src="(.+?\.jpg)" alt="'
imgre = re.compile(reg)
imglist = re.findall(imgre, res.text)

num=1
for a in imglist:
    image = load_pic(a)
    with open('E:/pythonCode/data/%s.jpg' % num, 'wb') as fp:
        fp.write(image)
        num = num + 1
    print(a)
print('下载完成')
print(res.text)
