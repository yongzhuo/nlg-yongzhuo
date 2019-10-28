# -*- coding: UTF-8 -*-
# !/usr/bin/python
# @time     :2019/7/28 0:24
# @author   :Mo
# @function : base path of nlg-yongzhuo


import sys
import os


# base dir
path_root = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
projectdir = path_root.replace('\\', '/')
sys.path.append(projectdir)
print(projectdir)

# path of embedding
path_embedding_random_char = path_root + '/data/embeddings/term_char.txt'
path_embedding_random_word = path_root + '/data/embeddings/term_word.txt'
path_embedding_bert = path_root + '/data/embeddings/chinese_L-12_H-768_A-12/'
path_embedding_xlnet = path_root + '/data/embeddings/chinese_xlnet_mid_L-24_H-768_A-12/'
path_embedding_vector_word2vec_char = path_root + '/data/embeddings/w2v_model_wiki_char.vec'
path_embedding_vector_word2vec_word = path_root + '/data/embeddings/w2v_model_merge_short.vec'

# 模型目录
path_model_dir =  path_root + "/data/model/text_summarization/"
# 语料地址
path_model = path_root + '/data/model/text_summarization/model_fast_text.h5'
# 超参数保存地址
path_hyper_parameters =  path_root + '/data/model/text_summarization/hyper_parameters.json'
# embedding微调保存地址
path_fineture = path_root + "/data/model/text_summarization/embedding_trainable.h5"
