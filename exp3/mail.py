import os
import re
import numpy as np
import jieba


def build_dict(spam_file,ham_file,pattern):
    # para:
    # spam_file:垃圾邮件文件
    # ham_file: 正常邮件文件
    # pattern: 要去除内容的正则表达式模式
    # 
    # return:
    # d : 词典
    d=[]
    if 'word_dict.utf8' in os.listdir('.'):
        with open('./word_dict.utf8','r',encoding='utf8') as f:
            lines = f.readlines()
            for line in lines:
                d.append(line.replace('\n',''))
            return d
            
    with open(spam_file,'r',encoding='utf8') as f:
        lines = f.readlines()
        for line in lines:
            line = re.sub(pattern,'',line)
            line_list = jieba.lcut(line)
            for word in line_list:
                if word not in d:
                    d.append(word)
    with open(ham_file,'r',encoding='utf8') as f:
        lines = f.readlines()
        for line in lines:
            line = re.sub(pattern,'',line)
            line_list = jieba.lcut(line)
            for word in line_list:
                if word not in d:
                    d.append(word)

    with open('word_dict.utf8','w',encoding='utf8') as f:
        for word in d:
            f.write(word)
            f.write('\n')

    return d

def train(spam_file,ham_file,word_dict,pattern):
    # para:
    # spam_file: 垃圾邮件文件训练集
    # ham_file: 正常邮件训练集
    # word_dict: build_dict得到的词典，是由所有词组成的列表
    # pattern: 要去除的正则表达式模式
    #
    # return:
    # spam_vec: 垃圾邮件的向量，长度为词典长度
    # ham_vec: 正常邮件的向量
    #
    with open(spam_file,'r',encoding='utf8') as f:
        lines=f.readlines()
        spam_vec = np.zeros((len(lines),len(word_dict)))
        for i in range(len(lines)):
            words = jieba.lcut(re.sub(pattern,'',lines[i]))
            for word in words:
                try:
                    spam_vec[i][word_dict.index(word)]=1
                except ValueError:
                    continue
    spam_vec=np.sum(spam_vec,axis=0)

    with open(ham_file,'r',encoding='utf8') as f:
        lines = f.readlines()
        ham_vec = np.zeros((len(lines),len(word_dict)))
        for i in range(len(lines)):
            words = jieba.lcut(re.sub(pattern,'',lines[i]))
            for word in words:
                try:
                    ham_vec[i][word_dict.index(word)]=1
                except ValueError:
                    continue
    ham_vec=np.sum(ham_vec,axis=0)

    return spam_vec,ham_vec


def verify(spam_vec,ham_vec,pattern,word_dict):
    # para:
    # spam_vec: 垃圾邮件的向量，长度为词典长度
    # ham_vec: 正常邮件的向量
    # pattern: 要去除的正则表达式模式
    # word_dict: build_dict得到的词典，是由所有词组成的列表
    #
    # output:
    # 对每一封测试的邮件输出正确或错误
    # 最终空两行输出误报率
    test_spams = os.listdir('./data/spam')
    test_hams = os.listdir('./data/ham')
    s=0
    a=0
    for spam in test_spams:
        test_vec=np.zeros(len(word_dict))
        with open('./data/spam/'+spam,'r',encoding='utf8') as f:
            content = f.readlines()
            words = jieba.lcut(re.sub(pattern,'',content[0]))
            for word in words:
                try:
                    test_vec[word_dict.index(word)]=1
                except ValueError:
                    continue
        p_spam=1
        p_ham=1
        for i in range(len(word_dict)):
            if test_vec[i]==1:
                if spam_vec[i]!=0:
                    p_spam=p_spam*spam_vec[i]/5000
                if ham_vec[i]!=0:
                    p_ham=p_ham*ham_vec[i]/5000
            else:
                p_spam=p_spam*(5000-spam_vec[i])/5000
                p_ham=p_ham*(5000-ham_vec[i])/5000
        
        if p_spam>p_ham:
            print("Right")
        else:
            print("Wrong")
            s=s+1
        a=a+1

    print('\n\n')
    print(s/a)


def main():
    pattern = re.compile('[\s+\.\!\/_,$%^*(+\"\'-]+|[+——！，。？、~@#￥%……&*（）<>]+')
    spam_file = './data/spam.utf8'
    ham_file = './data/ham.utf8'

    word_dict=build_dict(spam_file,ham_file,pattern)
    spam_vec,ham_vec=train(spam_file,ham_file,word_dict,pattern)

    verify(spam_vec,ham_vec,pattern,word_dict)

main()
