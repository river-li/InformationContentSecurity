# README
该repo是武汉大学信息内容安全实验课的作业

## exp1
实验一 简单的爬虫
内容均为文字爬虫
- baidu.py 爬取百度搜索风云榜的热点
- university.py 中国最好大学的排名，名称以及得分
- world.py 将爬取网站修改为世界大学的排名的爬虫
- dangdang.py 爬取当当图书畅销榜的爬虫

## exp2
实验二 正则表达式和scrapy
- douban scrapy的工程目录，里面有scarpy爬取豆瓣movie top250的代码
- regular.py 正则表达式的例子，匹配邮箱以及IP地址
- stock.py 从百度股市通获取股票行情的文件

douban 的用法
```bash
cd douban
scrapy spider movie -o output.csv
```

