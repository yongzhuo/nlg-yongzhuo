# -*- coding: UTF-8 -*-
# !/usr/bin/python
# @time     :2019/8/29 9:39
# @author   :Mo
# @function :textrank of textrank4zh, sklearn or gensim


from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from gensim.summarization.summarizer import summarize
from textrank4zh import TextRank4Sentence
import networkx as nx
import jieba
import re


# textrank of textrank4zh
tr4s = TextRank4Sentence()


# textrank of sklearn
def cut_sentence(sentence):
    """
        分句
    :param sentence:str
    :return:list
    """
    re_sen = re.compile('[.。？！?!\n\r]')
    sentences = re_sen.split(sentence)
    return sentences
def tdidf_sim(sentences):
    """
       tfidf相似度
    :param sentences: 
    :return: 
    """
    # tfidf计算
    model = TfidfVectorizer(tokenizer=jieba.cut,
                            ngram_range=(1, 2), # 3,5
                            stop_words=[' ', '\t', '\n'],  # 停用词
                            max_features=10000,
                            token_pattern=r"(?u)\b\w+\b",  # 过滤停用词
                            min_df=1,
                            max_df=0.9,
                            use_idf=1,  # 光滑
                            smooth_idf=1,  # 光滑
                            sublinear_tf=1, )  # 光滑
    matrix = model.fit_transform(sentences)
    matrix_norm = TfidfTransformer().fit_transform(matrix)
    return matrix_norm
def textrank_tfidf(sentences, topk=6):
    """
        使用tf-idf作为相似度, networkx.pagerank获取中心句子作为摘要
    :param sentences: str, docs of text
    :param topk:int
    :return:list
    """
    # 切句子
    sentences = list(cut_sentence(sentences))
    # tf-idf相似度
    matrix_norm = tdidf_sim(sentences)
    # 构建相似度矩阵
    tfidf_sim = nx.from_scipy_sparse_matrix(matrix_norm * matrix_norm.T)
    # nx.pagerank
    sens_scores = nx.pagerank(tfidf_sim)
    # 得分排序
    sen_rank = sorted(sens_scores.items(), key=lambda x: x[1], reverse=True)
    # 保留topk个, 防止越界
    topk = min(len(sentences), topk)
    # 返回原句子和得分
    return [(sr[1], sentences[sr[0]]) for sr in sen_rank][0:topk]


class textrank:
    def __init__(self):
        self.algorithm = 'textrank'

    def summarize(self, doc, num=6, model_type="textrank_textrank4zh"):
        if model_type=="textrank_textrank4zh":
            tr4s.analyze(text=doc, lower=True, source='all_filters')
            key_tr4s = tr4s.get_key_sentences(num=num)
            res = []
            for item in key_tr4s:
                res.append((item.weight, item.sentence))
        elif model_type=="text_rank_sklearn":
            res = textrank_tfidf(doc, topk=num)
        elif model_type=="textrank_gensim":
            res = summarize(doc, ratio=0.3, split=True)
        else:
            raise RuntimeError(" model_type must be 'textrank_textrank4zh', 'text_rank_sklearn' or 'textrank_gensim' ")

        return res


if __name__ == '__main__':

    doc = "文本生成NLG，不同于文本理解NLU（例如分词、词向量、分类、实体提取），" \
          "是重在文本生成的另一种关键技术（常用的有翻译、摘要、同义句生成等）。" \
          "传统的文本生成NLG任务主要是抽取式的，生成式的方法看起来到现在使用也没有那么普遍。" \
          "现在，我记录的是textrank，一种使用比较广泛的抽取式关键句提取算法。" \
          "版权声明：本文为CSDN博主「大漠帝国」的原创文章，遵循CC 4.0 by-sa版权协议，" \
          "转载请附上原文出处链接及本声明。原文链接：https://blog.csdn.net/rensihui" \
          "/article/details/98530760"

    doc = doc.encode('utf-8').decode('utf-8')

    tr = textrank()

    score_ques = tr.summarize(doc, model_type="textrank_textrank4zh")# "text_rank_sklearn")
    for sq in score_ques:
        print(sq)
