import requests
from bs4 import BeautifulSoup
import re
import json
import math

def load_pic(url):
    response = requests.get(url)
    return response.content

# res = requests.get('http://www.nipic.com/topic/show_27202_1.html')

# maxPage = 9
# while maxPage>=1:
#     print(maxPage)
#     maxPage-=1

print(1.0+1)
print(1+1)
print(1-2)
print(1.0-2)
print(1.0*2)
print(1.0/2)
print(int(1/2))
print(math.ceil(3.0/2))
print(math.ceil(22/10))