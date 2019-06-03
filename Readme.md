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

## exp3
实验三 词向量和朴素贝叶斯分类
- sogou.py 对搜狗新闻进行分词处理并生成本地文件的脚本
- result/_dict.txt sogou.py的结果，其中每一个词后面有一个空格
- gen/_vec.py 使用前面分词的结果生成词向量的脚本，建议使用ipython运行后进一步实验word2vector的相关功能以加深理解
- mail.py 贝叶斯分类对中文邮件处理的脚本

数据部分在data目录下
- word/ 文件夹中每一个文件是一篇搜狗新闻，用作生成词向量的语料库
- spam.utf8 邮件分类器的垃圾邮件训练集，每一行是一封垃圾邮件
- ham.utf8 邮件分类器的正常邮件训练集，每一行是一封正常邮件
- word/_dict.utf8 mail.py生成的中间结果,用于存储字典
- spam/ 邮件分类器的垃圾邮件测试集
- ham/ 邮件分类器的正常邮件测试集(未用到)
