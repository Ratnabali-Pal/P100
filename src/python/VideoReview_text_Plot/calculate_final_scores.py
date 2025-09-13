import numpy as np

# This script requires one_gram_keyword_score, bi_gram_keyword_score, 
# and word_cloud_score to be loaded or passed from previous scripts.

one_gram_keyword_score=one_gram_keyword_score/np.max(one_gram_keyword_score)
bi_gram_keyword_score=bi_gram_keyword_score/np.max(bi_gram_keyword_score)
word_cloud_score=word_cloud_score/np.max(word_cloud_score)

avg_verbal_score = (one_gram_keyword_score + bi_gram_keyword_score + word_cloud_score) / 3