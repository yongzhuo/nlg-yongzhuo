# -*- coding: UTF-8 -*-
# !/usr/bin/python
# @time     :2019/9/2 14:03
# @author   :Mo
# @function :topic model of LSI
# @paper    :Text summarization using Latent Semantic Analysis


#
from nlg_yongzhuo.data_proprecess.text_preprocess import extract_chinese
from nlg_yongzhuo.data_proprecess.text_preprocess import cut_sentence
from nlg_yongzhuo.data_proprecess.text_preprocess import jieba_cut
from nlg_yongzhuo.data.stop_words.stop_words import stop_words
# sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD


def tfidf_fit(sentences):
    """
       tfidf相似度
    :param sentences: 
    :return: 
    """
    # tfidf计算
    model = TfidfVectorizer(ngram_range=(1, 2), # 3,5
                            stop_words=[' ', '\t', '\n'],  # 停用词
                            max_features=10000,
                            token_pattern=r"(?u)\b\w+\b",  # 过滤停用词
                            min_df=1,
                            max_df=0.9,
                            use_idf=1,  # 光滑
                            smooth_idf=1,  # 光滑
                            sublinear_tf=1, )  # 光滑
    matrix = model.fit_transform(sentences)
    return matrix


class LSISum:
    def __init__(self):
        self.stop_words = stop_words.values()
        self.algorithm = 'lsi'

    def summarize(self, text, num=8, topic_min=3):
        """
            
        :param text: 
        :param num: 
        :return: 
        """
        # 切句
        if type(text) == str:
            self.sentences = cut_sentence(text)
        elif type(text) == list:
            self.sentences = text
        else:
            raise RuntimeError("text type must be list or str")
        # 切词
        sentences_cut = [[word for word in jieba_cut(extract_chinese(sentence))
                          if word.strip()] for sentence in self.sentences]
        # 去除停用词等
        self.sentences_cut = [list(filter(lambda x: x not in self.stop_words, sc)) for sc in sentences_cut]
        self.sentences_cut = [" ".join(sc) for sc in self.sentences_cut]
        # 计算每个句子的tfidf
        sen_tfidf = tfidf_fit(self.sentences_cut)
        # 主题数, 经验判断
        topic_num = min(topic_min, int(len(sentences_cut)/2))  # 设定最小主题数为3
        svd_tfidf = TruncatedSVD(n_components=topic_num, n_iter=32)
        res_svd = svd_tfidf.fit_transform(sen_tfidf)

        res_combine = {}
        for i in range(topic_num):
            res_row_i = res_svd[:, i]
            x_sort = res_row_i.argsort() # numpy中默认快速排序[即快排],获取最大的数字
            x_sort_max = x_sort[-len(sentences_cut)-1:]  # numpy中默认快速排序[即快排],获取最大的数字
            for xsm in x_sort_max:
                if self.sentences[xsm] not in res_combine:
                    res_combine[self.sentences[xsm]] = res_row_i[xsm]
                else:
                    if res_row_i[xsm] > res_combine[self.sentences[xsm]]:
                        res_combine[self.sentences[xsm]] = res_row_i[xsm]
        score_sen = [(rc[1], rc[0]) for rc in sorted(res_combine.items(), key=lambda d: d[1], reverse=True)]

        return score_sen

if __name__ == '__main__':
    lsi = LSISum()
    doc = "多知网5月26日消息，今日，方直科技发公告，拟用自有资金人民币1.2亿元，" \
          "与深圳嘉道谷投资管理有限公司、深圳嘉道功程股权投资基金（有限合伙）共同发起设立嘉道方直教育产业投资基金（暂定名）。" \
          "该基金认缴出资总规模为人民币3.01亿元。" \
          "基金的出资方式具体如下：出资进度方面，基金合伙人的出资应于基金成立之日起四年内分四期缴足，每期缴付7525万元；" \
          "各基金合伙人每期按其出资比例缴付。合伙期限为11年，投资目标为教育领域初创期或成长期企业。" \
          "截止公告披露日，深圳嘉道谷投资管理有限公司股权结构如下:截止公告披露日，深圳嘉道功程股权投资基金产权结构如下:" \
          "公告还披露，方直科技将探索在中小学教育、在线教育、非学历教育、学前教育、留学咨询等教育行业其他分支领域的投资。" \
          "方直科技2016年营业收入9691万元，营业利润1432万元，归属于普通股股东的净利润1847万元。（多知网 黎珊）}}"
    sum = lsi.summarize(doc)
    for i in sum:
        print(i)
