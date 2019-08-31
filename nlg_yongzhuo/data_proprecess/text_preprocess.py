# -*- coding: UTF-8 -*-
# !/usr/bin/python
# @time     :2019/8/25 21:36
# @author   :Mo
# @function :data utils of nlg-yongzhuo


import jieba.posseg as pseg
import pandas as pd
import logging
import jieba
import json
import re
import os


jieba.setLogLevel(logging.INFO)


def jieba_tag_cut(text):
    """
        jieba cut and tagged
    :param text:str 
    :return: dict
    """
    words = pseg.cut(text)
    return dict(words)


def jieba_cut(text):
    """
      Jieba cut
    :param text: input sentence
    :return: list
    """
    return list(jieba.cut(text, cut_all=False, HMM=False))


def cut_sentence(sentence):
    """
        分句
    :param sentence:str
    :return:list
    """
    re_sen = re.compile('[:;!?。：；？！\n\r]')
    sentences = re_sen.split(sentence)
    sen_cuts = []
    for sen in sentences:
        if sen and str(sen).strip():
            sen_cuts.append(sen)
    return sen_cuts


def extract_chinese(text):
    """
      只提取出中文、字母和数字
    :param text: str, input of sentence
    :return: 
    """
    chinese_exttract = ''.join(re.findall(u"([\u4e00-\u9fa5A-Za-z0-9@. ])", text))
    return chinese_exttract


def txt_read(file_path, encode_type='utf-8'):
    """
      读取txt文件,默认utf8格式,
    :param file_path: str, 文件路径
    :param encode_type: str, 编码格式
    :return: list
    """
    list_line = []
    try:
        file = open(file_path, 'r', encoding=encode_type)
        list_line = file.readlines()
    except Exception as e:
        print(str(e))
    finally:
        return list_line


def txt_write(list_line, file_path, type='w', encode_type='utf-8'):
    """
      txt写入list文件
    :param listLine:list, list文件，写入要带"\n" 
    :param filePath:str, 写入文件的路径
    :param type: str, 写入类型, w, a等
    :param encode_type: 
    :return: 
    """
    try:
        file = open(file_path, type, encoding=encode_type)
        file.writelines(list_line)
        file.close()
    except Exception as e:
        print(str(e))


def delete_file(path):
    """
        删除一个目录下的所有文件
    :param path: str, dir path
    :return: None
    """
    for i in os.listdir(path):
        # 取文件或者目录的绝对路径
        path_children = os.path.join(path, i)
        if os.path.isfile(path_children):
            os.remove(path_children)
        else:# 递归, 删除目录下的所有文件
            delete_file(path_children)


def read_and_process(path):
    """
      读取文本数据并
    :param path: 
    :return: 
    """
    data = pd.read_csv(path)
    ques = data["ques"].values.tolist()
    labels = data["label"].values.tolist()
    line_x = [extract_chinese(str(line).upper()) for line in labels]
    line_y = [extract_chinese(str(line).upper()) for line in ques]
    return line_x, line_y


def save_json(jsons, json_path):
    """
      保存json，
    :param json_: json 
    :param path: str
    :return: None
    """
    with open(json_path, 'w', encoding='utf-8') as fj:
        fj.write(json.dumps(jsons))
    fj.close()


def load_json(path):
    """
      获取json，只取第一行
    :param path: str
    :return: json
    """
    with open(path, 'r', encoding='utf-8') as fj:
        model_json = json.loads(fj.readlines()[0])
    return model_json


def gram_uni_bi_tri(text):
    """
        获取文本的unigram, trugram, bigram等特征
    :param text: str
    :return: list
    """
    len_text = len(text)
    gram_uni = []
    gram_bi = []
    gram_tri = []
    for i in range(len_text):
        if i + 3 <= len_text:
            gram_uni.append(text[i])
            gram_bi.append(text[i:i+2])
            gram_tri.append(text[i:i+3])
        elif i + 2 <= len_text:
            gram_uni.append(text[i])
            gram_bi.append(text[i:i+2])
        elif i + 1 <= len_text:
            gram_uni.append(text[i])
        else:
            break
    return gram_uni, gram_bi, gram_tri



if __name__ == '__main__':
    text = "你喜欢谁,小老弟,你好烦哇。"
    gg = jieba_tag_cut("我喜欢你,yx")
    grams = gram_uni_bi_tri(text)
    print(gg)
    print(grams)