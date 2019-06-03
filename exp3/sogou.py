import jieba
prefix = './data/word/'
affix='.txt'
with open('result_dict.txt','a') as f:
    for i in range(10,2000):
        s=''
        with open(prefix+str(i)+affix,'r',encoding='gb18030') as fp:
            l=fp.readlines()
            for j in l:
                s=s+j.replace('\u3000','')
            result=jieba.lcut(s)
            for r in result:
                f.write(r)
                f.write(' ')
