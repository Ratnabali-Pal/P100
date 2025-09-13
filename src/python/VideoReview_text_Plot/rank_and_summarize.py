import pandas as pd
import numpy as np
from nlp import NLP # Assuming this is the intended library

# Requires 'cloud_path', 'final_score', and 'sentence_segment' from previous steps.
# The 'NLP-python' package might need to be installed if not present.

data=pd.read_csv(cloud_path, header=None)
all_rank_score=np.array([data[1],data[0],final_score,np.array(sentence_segment)])
all_rank_score=all_rank_score.T
f_score=all_rank_score[all_rank_score[:, 2].argsort()]
f_score=f_score[::-1]
segment=[]
video=[]
rank=[]
th=0.5
M=5
counter=1
s=f_score[0][0]
v=f_score[0][1]
print(s,v)
print(f_score)