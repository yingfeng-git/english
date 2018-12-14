from bs4 import BeautifulSoup as bs
import requests

count = 0

data = bs(requests.get('http://www.etymon.cn/yingyucigen/list_1_1.html').content, 'lxml')
for i in data.find_all('dt'):
    print(i.get_text())
    print(i.find('a')['href'])




