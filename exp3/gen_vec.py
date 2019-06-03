from gensim.models import word2vec
import logging

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',level=logging.INFO)


def main():

    sentences = word2vec.Text8Corpus('./result_dict.txt')
    model = word2vec.Word2Vec(sentences,size=200)
    #size是神经网络中隐藏层中神经元的个数
    #model.save('word.model')

main()
