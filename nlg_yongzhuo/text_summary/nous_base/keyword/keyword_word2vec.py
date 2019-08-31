# -*- coding: UTF-8 -*-
# !/usr/bin/python
# @time     :2019/8/8 20:47
# @author   :Mo
# @function :keyword of word2vec


# 适配linux
import sys
import os
path_root = os.path.abspath(os.path.join(os.getcwd(), "../..")) # 获取上上级目录
sys.path.append(path_root)

from gensim.models.word2vec import LineSentence
from gensim.models import Word2Vec
import multiprocessing
import logging


def train_word2vec_by_word():
    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logging.info("running")

    inp = "cut_zhwiki_wiki_parse.txt"
    outp1 = "w2v_model_wiki.model"
    outp2 = "w2v_model_wiki_word.vec"

    print(multiprocessing.cpu_count())
    model = Word2Vec(LineSentence(inp), size=300, window=10,
                     # 这里用skip-heriber
                     min_count=1, sg=1, hs=1, iter=10, workers=multiprocessing.cpu_count())

    model.save(outp1)
    model.wv.save_word2vec_format(outp2, binary=False)


def predict_input():
    from collections import Counter
    import pandas as pd
    import numpy as np
    import gensim
    import jieba

    model = gensim.models.word2vec.Word2Vec.load('w2v_model_wiki_word')

    def keywords(s):
        """
            codes from 苏剑林. (2017, Apr 07). 《【不可思议的Word2Vec】 3.提取关键词 》[Blog post].Retrieved from https://www.spaces.ac.cn/archives/4316
        :param s: 
        :return: 
        """
        def predict_proba(oword, iword):
            iword_vec = model[iword]
            oword = model.wv.vocab[oword]
            oword_l = model.syn1[oword.point].T
            dot = np.dot(iword_vec, oword_l)
            lprob = -sum(np.logaddexp(0, -dot) + oword.code * dot)
            return lprob

        s = [w for w in s if w in model]
        ws = {w: sum([predict_proba(u, w) for u in s]) for w in s}
        return Counter(ws).most_common()

    s = u'地球是人类共同的家园, 是不是世界癌症。'
    print(pd.Series(keywords(jieba.cut(s))))
    while True:
        print("请输入: ")
        ques = input()
        k = pd.Series(keywords(jieba.cut(ques)))
        print(k)

if __name__ == '__main__':
    # 先训练, 然后再预测
    train_word2vec_by_word()
    predict_input()

# 本质是p(文本|关键词)，通俗来说，即求取对文本信息贡献最大的关键词
