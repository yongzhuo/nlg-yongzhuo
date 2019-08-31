# -*- coding: UTF-8 -*-
# !/usr/bin/python
# @time     :2019/8/21 22:20
# @author   :Mo
# @function :textrank using textrank4zh


from textrank4zh import TextRank4Sentence


doc = "文本生成NLG，不同于文本理解NLU（例如分词、词向量、分类、实体提取），" \
      "是重在文本生成的另一种关键技术（常用的有翻译、摘要、同义句生成等）。" \
      "传统的文本生成NLG任务主要是抽取式的，生成式的方法看起来到现在使用也没有那么普遍。" \
      "现在，我记录的是textrank，一种使用比较广泛的抽取式关键句提取算法。" \
      "版权声明：本文为CSDN博主「大漠帝国」的原创文章，遵循CC 4.0 by-sa版权协议，" \
      "转载请附上原文出处链接及本声明。原文链接：https://blog.csdn.net/rensihui" \
      "/article/details/98530760"

doc = doc.encode('utf-8').decode('utf-8')
tr4s = TextRank4Sentence()
tr4s.analyze(text=doc, lower=True, source = 'all_filters')

for item in tr4s.get_key_sentences(num=6):
    print(item.index, item.weight, item.sentence)
