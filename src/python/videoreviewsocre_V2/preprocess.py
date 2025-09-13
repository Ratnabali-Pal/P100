# scripts/preprocess.py

import os
from . import config

def combine_scores():
    """
    Reads sentiment, keyword, and cloud score files and combines them into a single file.
    """
    allscore_path = os.path.join(config.SCORE_DIR, "allscore.txt")
    sentiment_path = os.path.join(config.SCORE_DIR, "sentiment.txt")
    keyword_path = os.path.join(config.SCORE_DIR, "keyword.txt")
    cloud_path = os.path.join(config.SCORE_DIR, "cloud.txt")

    with open(allscore_path, 'w+') as file4, \
         open(sentiment_path, 'r') as file1, \
         open(keyword_path, 'r') as file2, \
         open(cloud_path, 'r') as file3:

        line1 = file1.read().splitlines()
        line2 = file2.read().splitlines()
        line3 = file3.read().splitlines()

        for l1, l2, l3 in zip(line1, line2, line3):
            l2_rev = l2.split(',')[2:]
            l3_rev = l3.split(',')[2:]
            
            file4.writelines(f"{l1},{l2_rev[0]},{l2_rev[1]},{l3_rev[0]}\n")

if __name__ == '__main__':
    combine_scores()