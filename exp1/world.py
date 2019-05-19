import requests
from bs4 import BeautifulSoup

def main():
    url = "http://www.zuihaodaxue.cn/ARWU2018.html"
    r = requests.get(url)
    soup = BeautifulSoup(r.content,'html.parser')
    items = soup.find_all('tr')
    tplt = "{0:^4}\t{1:{3}^50}\t{2:^10}"
    
    with open('world.txt','a') as f:
        f.write(tplt.format("排名","学校名称","总分",chr(12288))+'\n')
        items.remove(items[0])
        count=0
        for item in items:
            if count>99:
                break
            f.write(tplt.format(item.find_all('td')[0].string,item.find_all('td')[1].string,item.find_all('td')[4].string,chr(12288))+'\n')
            count+=1

main()
