import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from os import listdir
from os.path import isfile, join

dataset=iphone13
keyword_path=keyword+dataset
keyword_data = [f for f in listdir(keyword_path) if isfile(join(keyword_path, f))]
f = plt.figure()
f.set_figwidth(4)
f.set_figheight(2)
for t in keyword_data
  data_k=pd.read_csv(keyword_path++t, header=None)
  transparent=data_k[2].astype(float)
  transparent=transparentnp.max(transparent)
  one_gram_keyword_score=transparent
for x, y, a in zip(data_k[1], data_k[0], transparent)
    plt.scatter(x, y, marker='s',s=400,color='b',alpha=a)

# These variables (counter, maxx, maxsize) would need to be defined or passed from the previous script
# For example
# counter = 10 
# maxx = 15
# maxsize = 100

plt.yticks(np.arange(1, counter+1, 1.0))
plt.xticks(np.arange(1, maxx+1, 1.0))

plt.gca().margins(x=0)
plt.gcf().canvas.draw()
tl = plt.gca().get_xticklabels()

plt.gca().margins(x=0)
plt.gcf().canvas.draw()
tl = plt.gca().get_xticklabels()
m = 0.1 # inch margin
N=16
s = maxsizeplt.gcf().dpiN+2m
margin = mplt.gcf().get_size_inches()[0]

plt.gcf().subplots_adjust(left=margin, right=1.-margin)
plt.savefig('2.png', dpi=300)