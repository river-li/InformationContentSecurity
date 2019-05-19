import requests
from bs4 import BeautifulSoup

def main():
    url = "http://www.zuihaodaxue.cn/zuihaodaxuepaiming2018.html"
    r = requests.get(url)
    soup = BeautifulSoup(r.content,'html.parser')
    items = soup.find_all('tr',attrs='alt')
    tplt = "{0:^4}\t{1:{3}^12}\t{2:^10}"
    
    with open('university.txt','a') as f:
        f.write(tplt.format("排名","学校名称","总分",chr(12288))+'\n')
        for item in items:
            f.write(tplt.format(item.find_all('td')[0].string,item.find_all('td')[1].string,item.find_all('td')[3].string,chr(12288))+'\n')

main()
