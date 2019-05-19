import requests
from bs4 import BeautifulSoup

url = "http://top.baidu.com"

r= requests.get(url)
soup = BeautifulSoup(r.content,'html.parser')
uls = soup.find_all('ul',attrs='list')

with open('baidu.txt','a') as f:
    f.write('实时热点\n')
    for i in uls[0].find_all('li'):
        f.write(str(i.text.replace('\n',' ').replace('search',''))+'\n')

    f.write('\n七日热点\n')
    for i in uls[1].find_all('li'):
        f.write(str(i.text.replace('\n',' ').replace('search',''))+'\n')

