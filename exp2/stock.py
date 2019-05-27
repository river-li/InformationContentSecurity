import requests
from bs4 import BeautifulSoup

stock_list=[]
url = 'http://www.yz21.org/stock/info/stocklist_'
affix='.html'

r = requests.get('http://www.yz21.org/stock/info/')
soup = BeautifulSoup(r.content,'html.parser')
page_list = soup.find_all('a',attrs='content')
for j in range(len(page_list)):
    if j%3==0:
        s=page_list[j]['href'].replace('/','').replace('.','')
        stock_list.append(s)

for i in range(2,185):
    r=requests.get(url+str(i)+affix)
    soup=BeautifulSoup(r.content,'html.parser')
    page_list = soup.find_all('a',attrs='content')
    for j in range(len(page_list)):
        if j%3==0:
            s=page_list[j]['href'].replace('/','').replace('.','')
            stock_list.append(s)
    
url = "https://gupiao.baidu.com/stock/"
for stock in stock_list:
    r = requests.get(url+stock+affix)
    
    soup = BeautifulSoup(r.content,'html.parser')
    stockinfo=soup.find('div',attrs='stock-bets')
    if stockinfo==None:
        continue
    infoDict={}
    name = stockinfo.find_all(attrs='bets-name')[0]
    infoDict.update({'股票名称':name.text.split()[0]})
    KeyList = stockinfo.find_all('dt')
    valueList = stockinfo.find_all('dd')
    for i in range(len(KeyList)):
        key = KeyList[i].text
        val=valueList[i].text
        infoDict[key] = val
    with open('stock.txt','a',encoding='utf-8') as f:
        f.write(str(infoDict)+'\n')


