# -*- coding: UTF-8 -*-
# !/usr/bin/python
# @time     :2019/7/25 21:09
# @author   :Mo
# @function :


from nlg_yongzhuo.text_summarization.extractive_sum.feature_base.word_significance import WordSignificanceSum
from nlg_yongzhuo.text_summarization.extractive_sum.feature_base.text_pronouns import TextPronounsSum
from nlg_yongzhuo.text_summarization.extractive_sum.feature_base.text_teaser import TextTeaserSum
from nlg_yongzhuo.text_summarization.extractive_sum.feature_base.mmr import MMRSum

from nlg_yongzhuo.text_summarization.extractive_sum.graph_base.textrank.textrank import TextRankSum

from nlg_yongzhuo.text_summarization.extractive_sum.nous_base.lead_3.lead_3 import Lead3Sum

from nlg_yongzhuo.text_summarization.extractive_sum.topic_base.topic_lda import LDASum
from nlg_yongzhuo.text_summarization.extractive_sum.topic_base.topic_lsi import LSISum
from nlg_yongzhuo.text_summarization.extractive_sum.topic_base.topic_nmf import NMFSum

# feature
word_significance = WordSignificanceSum()
text_pronouns = TextPronounsSum()
text_teaser = TextTeaserSum()
mmr = MMRSum()

# graph-3
text_rank = TextRankSum()

# nous
lead3 = Lead3Sum()

# topic
lda = LDASum()
lsi = LSISum()
nmf = NMFSum()
