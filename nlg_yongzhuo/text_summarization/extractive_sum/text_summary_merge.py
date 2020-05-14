# !/usr/bin/python
# -*- coding: utf-8 -*-
# @time    : 2020/3/17 9:32
# @author  : Mo
# @function: text-summary of merge of multi-processing or serial


from nlg_yongzhuo import text_pronouns, text_teaser, mmr, text_rank, lead3, lda, lsi, nmf
from multiprocessing import Manager, Process
import multiprocessing
import platform
if platform.system()=='Windows':
    multiprocessing.freeze_support()
    multiprocessing.set_start_method("spawn", force=True)


# 共享变量
def worker(i, text, num, fs, return_dict):
    """
        worker function
    :param i: int
    :param text: str
    :param fs: list
    :param return_dict: list<list> 
    :return: None
    """
    return_dict[i] = fs[i].summarize(text=text, num=num)


def summary_multi_preprocess(doc, num=None, fs=[text_pronouns, text_teaser, mmr, text_rank, lead3, lda, lsi, nmf]):
    """
        len(fs) 个进程
    :param doc: str
    :return: list
    """
    manager = Manager()
    return_dict = manager.dict()
    jobs = []
    for i in range(len(fs)):
        p = Process(target=worker, args=(i, doc, num, fs, return_dict))
        jobs.append(p)
        p.start()
    for proc in jobs:
        proc.join()
    return list(return_dict.values())


def summary_serial(doc, num=None, fs=[text_pronouns, text_teaser, mmr, text_rank, lead3, lda, lsi, nmf]):
    """
        单独串行跑所有
    :param doc: str
    :return: list
    """
    res = []
    for fs_ in fs:
        res_fs = fs_.summarize(text=doc, num=num)
        res.append(res_fs)
    return res


def summary_post_preprocess(reses):
    """
        后处理
    :param reses: list<list>
    :return: list
    """
    res_dict = {}
    for res in reses:
        r_dict = {}
        sum_score = sum([r[0] for r in res])
        for score, sent in res:
            r_dict[sent] = score/sum_score
            if sent in res_dict:
                res_dict[sent] = res_dict[sent] + r_dict[sent]
            else:
                res_dict[sent] = r_dict[sent]
    score_sen = [(rc[1], rc[0]) for rc in sorted(res_dict.items(),
                                                 key=lambda d: d[1], reverse=True)]
    return score_sen


def text_summarize(doc, num=None, multi_process=False,
                   fs=[text_pronouns, text_teaser, mmr, text_rank, lead3, lda, lsi, nmf]):
    """
        抽取式文本摘要, 汇总, 使用几个方法
    :param doc: str or list, 用户输入
    :param num: int, 返回的句子个数
    :param multi_process: bool, 是否使用多进程
    :return: res_score: list, sentences of doc with score
    """
    if type(doc)==list:
        doc = "。".join(doc)
    elif not doc or (type(doc) != str):
        raise RuntimeError(" type of doc must be 'list' or 'str' ")
    if not num:
        from nlg_yongzhuo.data_preprocess.text_preprocess import cut_sentence
        num = len(cut_sentence(doc))
    # 是否使用多进程, 注意: 当cpu数量不足或性能较差时, 多进程不一定比串行快
    if multi_process:
        res = summary_multi_preprocess(doc, num, fs)
    else:
        res = summary_serial(doc, num, fs)
    # 后处理
    res_score = summary_post_preprocess(res)
    return res_score


if __name__ == '__main__':
    doc = """PageRank算法简介。" \
          "是上世纪90年代末提出的一种计算网页权重的算法! " \
          "当时，互联网技术突飞猛进，各种网页网站爆炸式增长。 " \
          "业界急需一种相对比较准确的网页重要性计算方法。 " \
          "是人们能够从海量互联网世界中找出自己需要的信息。 " \
          "百度百科如是介绍他的思想:PageRank通过网络浩瀚的超链接关系来确定一个页面的等级。 " \
          "Google把从A页面到B页面的链接解释为A页面给B页面投票。 " \
          "Google根据投票来源甚至来源的来源，即链接到A页面的页面。 " \
          "和投票目标的等级来决定新的等级。简单的说， " \
          "一个高等级的页面可以使其他低等级页面的等级提升。 " \
          "具体说来就是，PageRank有两个基本思想，也可以说是假设。 " \
          "即数量假设：一个网页被越多的其他页面链接，就越重）。 " \
          "质量假设：一个网页越是被高质量的网页链接，就越重要。 " \
          "总的来说就是一句话，从全局角度考虑，获取重要的信。 """.replace(" ", "").replace('"', '')

    # fs可以填其中一个或几个 text_pronouns, text_teaser, mmr, text_rank, lead3, lda, lsi, nmf
    res_score = text_summarize(doc, multi_process=True, fs=[text_pronouns, text_teaser, mmr, text_rank, lead3, lda, lsi, nmf])
    for rs in res_score:
        print(rs)

