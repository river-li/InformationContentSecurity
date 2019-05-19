# coding=utf-8
import requests
import re
from bs4 import BeautifulSoup

def main():
    url = "http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-24hours-0-0-1-1"
    r = requests.get(url)
    soup = BeautifulSoup(r.content,'html.parser')
    lis=soup.find('ul',attrs='bang_list').find_all('li')
    tplt = "{0:^4}\t{1:{3}^30}\t{2:^30}"
    pattern1 = re.compile('（.*）')
    pattern2 = re.compile('\(.*\)')

    with open('dangdang.txt','a') as f:
        f.write(tplt.format("排名","书名","作者",chr(12288))+'\n')
        for li in lis:
            rank = li.find('div',attrs='list_num').string
            name = li.find('div',attrs='name').a['title']
            idx = re.search(pattern1,name)
            if idx!=None:
                idx=idx.span()
                name = name.replace(name[idx[0]:len(name)],'')

            idx1 = re.search(pattern2,name)
            if idx1!=None:
                idx1=idx1.span()
                name = name.replace(name[idx1[0]:len(name)],'')


            author = li.find('div',attrs='publisher_info').a.string
            f.write(tplt.format(rank,name,author,chr(12288))+'\n')
main()
