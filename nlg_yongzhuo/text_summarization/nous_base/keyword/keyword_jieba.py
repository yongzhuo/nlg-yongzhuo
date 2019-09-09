# -*- coding: UTF-8 -*-
# !/usr/bin/python
# @time     :2019/8/8 21:02
# @author   :Mo
# @function :keyword of jieba


# 适配linux
import sys
import os
# path_root = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)) # 获取上级目录
path_root = os.path.abspath(os.path.join(os.getcwd(), "../..")) # 获取上上级目录
sys.path.append(path_root)

import jieba.analyse as analyse
import logging
import jieba


# 设置jieba日志为info
jieba.setLogLevel(logging.INFO)
# 引入TF-IDF关键词抽取接口
tfidf = analyse.extract_tags
# 引入TextRank关键词抽取接口
textrank = analyse.textrank


def keyword_tfidf(sentence, rate=1.):
    """
        使用tf-dif获取关键词构建
    :param sentence: str, input sentence
    :param rate: float, 0-1
    :return: str
    """
    sen_words = jieba._lcut(sentence)
    top_k = int(len(sen_words) * rate)
    keyword = tfidf(sentence, topK=top_k, withWeight=False, withFlag=False)
    keyword_sort = [k if k in keyword else '' for k in sen_words]
    return ''.join(keyword_sort)


def keyword_textrank(sentence, rate=1.,
                              allow_pos=('an', 'i', 'j', 'l', 'r', 't',
                                         'n', 'nr', 'ns', 'nt', 'nz',
                                         'v', 'vd', 'vn')):
    """
        使用text-rank获取关键词构建
    :param sentence:  str, input sentence, 例: '大漠帝国是谁呀，你知道吗'
    :param rate: float, 0-1 , 例: '0.6'
    :param allow_pos: list, 例: ('ns', 'n', 'vn', 'v')
    :return: str, 例: '大漠帝国'
    """
    sen_words = jieba._lcut(sentence)
    top_k = int(len(sen_words) * rate)
    keyword = textrank(sentence, topK=top_k, allowPOS=allow_pos, withWeight=False, withFlag=False)
    keyword_sort = [k if k in keyword else '' for k in sen_words]
    return ''.join(keyword_sort)




if __name__ == '__main__':
    # sen = "大漠帝国是谁呀，你知道吗，蔚蓝色星球"
    sen = "自然语言理解（NLU，Natural Language Understanding）: 使计算机理解自然语言（人类语言文字）等，重在理解。具体来说，就是理解语言、文本等，提取出有用的信息，用于下游的任务。它可以是使自然语言结构化，比如分词、词性标注、句法分析等；也可以是表征学习，字、词、句子的向量表示(Embedding)，构建文本表示的文本分类；还可以是信息提取，如信息检索（包括个性化搜索和语义搜索，文本匹配等），又如信息抽取（命名实体提取、关系抽取、事件抽取等）。" \
          "自然语言生成（NLG，Natural Language Generation）: 提供结构化的数据、文本、图表、音频、视频等，生成人类可以理解的自然语言形式的文本。NLG又可以分为三大类，文本到文本（text-to-text），如翻译、摘要等、文本到其他（text-to-other），如文本生成图片、其他到文本（other-to-text），如视频生成文本。"
    sen_tf = keyword_tfidf(sentence=sen, rate=0.1)
    sen_rank = keyword_textrank(sentence=sen, rate=0.6)
    print(sen_tf)
    print(sen_rank)


