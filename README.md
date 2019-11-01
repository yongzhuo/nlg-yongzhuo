# nlg-yongzhuo

# Install(安装)

```bash
pip install nlg-yongzhuo
```

# Train&Usage(调用),详情见/test/目录下
```bash

from nlg_yongzhuo import word_significance
from nlg_yongzhuo import text_pronouns
from nlg_yongzhuo import text_teaser
from nlg_yongzhuo import mmr


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

3. text_teaser
sums_text_teaser = text_teaser.summarize(docs, num=6)
print("text_teaser:")
for sum_ in sums_text_teaser:
    print(sum_)
4. mmr
sums_mmr = mmr.summarize(docs, num=6)
print("mmr:")
for sum_ in sums_mmr:
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
    - 数据下载
      ** github项目中只是上传部分数据，需要的前往链接: https://pan.baidu.com/s/1I3vydhmFEQ9nuPG2fDou8Q 提取码: rket


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
