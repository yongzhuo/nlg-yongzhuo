# [nlg-yongzhuo](https://github.com/yongzhuo/nlg-yongzhuo)

[![PyPI](https://img.shields.io/pypi/v/nlg-yongzhuo)](https://pypi.org/project/nlg-yongzhuo/)
[![Build Status](https://travis-ci.com/yongzhuo/nlg-yongzhuo.svg?branch=master)](https://travis-ci.com/yongzhuo/nlg-yongzhuo)
[![PyPI_downloads](https://img.shields.io/pypi/dm/nlg-yongzhuo)](https://pypi.org/project/nlg-yongzhuo/)
[![Stars](https://img.shields.io/github/stars/yongzhuo/nlg-yongzhuo?style=social)](https://github.com/yongzhuo/nlg-yongzhuo/stargazers)
[![Forks](https://img.shields.io/github/forks/yongzhuo/nlg-yongzhuo.svg?style=social)](https://github.com/yongzhuo/nlg-yongzhuo/network/members)
[![Join the chat at https://gitter.im/yongzhuo/nlg-yongzhuo](https://badges.gitter.im/yongzhuo/nlg-yongzhuo.svg)](https://gitter.im/yongzhuo/nlg-yongzhuo?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)


# Install(安装)

```bash
pip install nlg-yongzhuo
```

# API(联合调用, 整合几种算法)
```bash
from nlg_yongzhuo import *

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
              "总的来说就是一句话，从全局角度考虑，获取重要的信。 """

# fs可以填其中一个或几个 text_pronouns, text_teaser, mmr, text_rank, lead3, lda, lsi, nmf
res_score = text_summarize(doc, fs=[text_pronouns, text_teaser, mmr, text_rank, lead3, lda, lsi, nmf])
for rs in res_score:
    print(rs)

```


# Usage(调用),详情见/test/目录下
```bash

# feature_base
from nlg_yongzhuo import word_significance
from nlg_yongzhuo import text_pronouns
from nlg_yongzhuo import text_teaser
from nlg_yongzhuo import mmr
# graph_base
from nlg_yongzhuo import text_rank
# topic_base
from nlg_yongzhuo import lda
from nlg_yongzhuo import lsi
from nlg_yongzhuo import nmf
# nous_base
from nlg_yongzhuo import lead3


docs ="和投票目标的等级来决定新的等级.简单的说。" \
          "是上世纪90年代末提出的一种计算网页权重的算法! " \
          "当时，互联网技术突飞猛进，各种网页网站爆炸式增长。" \
          "业界急需一种相对比较准确的网页重要性计算方法。" \
          "是人们能够从海量互联网世界中找出自己需要的信息。" \
          "百度百科如是介绍他的思想:PageRank通过网络浩瀚的超链接关系来确定一个页面的等级。" \
          "Google把从A页面到B页面的链接解释为A页面给B页面投票。" \
          "Google根据投票来源甚至来源的来源，即链接到A页面的页面。" \
          "一个高等级的页面可以使其他低等级页面的等级提升。" \
          "具体说来就是，PageRank有两个基本思想，也可以说是假设。" \
          "即数量假设：一个网页被越多的其他页面链接，就越重）。" \
          "质量假设：一个网页越是被高质量的网页链接，就越重要。" \
          "总的来说就是一句话，从全局角度考虑，获取重要的信。"
# 1. word_significance
sums_word_significance = word_significance.summarize(docs, num=6)
print("word_significance:")
for sum_ in sums_word_significance:
    print(sum_)

# 2. text_pronouns
sums_text_pronouns = text_pronouns.summarize(docs, num=6)
print("text_pronouns:")
for sum_ in sums_text_pronouns:
    print(sum_)

# 3. text_teaser
sums_text_teaser = text_teaser.summarize(docs, num=6)
print("text_teaser:")
for sum_ in sums_text_teaser:
    print(sum_)
# 4. mmr
sums_mmr = mmr.summarize(docs, num=6)
print("mmr:")
for sum_ in sums_mmr:
    print(sum_)
# 5.text_rank
sums_text_rank = text_rank.summarize(docs, num=6)
print("text_rank:")
for sum_ in sums_text_rank:
    print(sum_)
# 6. lda
sums_lda = lda.summarize(docs, num=6)
print("lda:")
for sum_ in sums_lda:
    print(sum_)
# 7. lsi
sums_lsi = lsi.summarize(docs, num=6)
print("mmr:")
for sum_ in sums_lsi:
    print(sum_)
# 8. nmf
sums_nmf = nmf.summarize(docs, num=6)
print("nmf:")
for sum_ in sums_nmf:
    print(sum_)
# 9. lead3
sums_lead3 = lead3.summarize(docs, num=6)
print("lead3:")
for sum_ in sums_lead3:
    print(sum_)

```

# nlg_yongzhuo
    - text_summary
    - text_augnment(todo)
    - text_generation(todo)
    - text_translation(todo)


# run(运行, 以text_teaser为例)
    - 1. 直接进入目录文件运行即可, 例如进入:nlg_yongzhuo/text_summary/feature_base/
    - 2. 运行: python text_teaser.py


# nlg_yongzhuo/data
  * 哈工大的新浪微博短文本摘要[LCSTS](http://icrc.hitsz.edu.cn/Article/show/139.html)
  * 教育新闻自动摘要语料[chinese_abstractive_corpus](https://github.com/wonderfulsuccess/chinese_abstractive_corpus)
  * NLPCC 2017 task3[Single Document Summarization](http://tcci.ccf.org.cn/conference/2017/taskdata.php)
  * 娱乐新闻等[“神策杯”2018高校算法大师赛 ](https://www.dcjingsai.com/common/cmpt/%E2%80%9C%E7%A5%9E%E7%AD%96%E6%9D%AF%E2%80%9D2018%E9%AB%98%E6%A0%A1%E7%AE%97%E6%B3%95%E5%A4%A7%E5%B8%88%E8%B5%9B_%E7%AB%9E%E8%B5%9B%E4%BF%A1%E6%81%AF.html)

# 模型与论文paper与地址
* pagerank:     [The PageRank citation ranking: Bringing order to the Web. 1999](http://dbpubs.stanford.edu:8090/pub/showDoc.Fulltext?lang=en&doc=1999-66&format=pdf)
* textrank:     [TextRank: Bringing Order into Texts](https://www.researchgate.net/publication/200042361_TextRank_Bringing_Order_into_Text)
* textteaser:   [Automatic Text Summarization for Indonesian Language Using TextTeaser]
* significance: [The Automatic Creation of Literature Abstracts*](http://courses.ischool.berkeley.edu/i256/f06/papers/luhn58.pdf)
* LSI:          [Text summarization using Latent Semantic Analysis](https://www.researchgate.net/publication/220195824_Text_summarization_using_Latent_Semantic_Analysis)
* LDA:          [Latent Dirichlet Allocation](http://jmlr.csail.mit.edu/papers/v3/blei03a.html)


# 参考/感谢
* 文本摘要综述:   [https://github.com/icoxfog417/awesome-text-summarization](https://github.com/icoxfog417/awesome-text-summarization)
* textteaser:   [https://github.com/IndigoResearch/textteaser](https://github.com/IndigoResearch/textteaser)
* NaiveSumm:    [https://github.com/amsqr/NaiveSumm](https://github.com/amsqr/NaiveSumm)
* ML主题模型:    [https://github.com/ljpzzz/machinelearning](https://github.com/ljpzzz/machinelearning)


*希望对你有所帮助!
