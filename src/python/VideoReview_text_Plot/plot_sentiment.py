import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from os import listdir
from os.path import isfile, join

dataset="iphone13"
sentiment_path="sentiment/"+dataset

data = [f for f in listdir(sentiment_path) if isfile(join(sentiment_path, f))]
f = plt.figure()
f.set_figwidth(4)
f.set_figheight(2)
counter=0
maxx=0
for t in data:
  data=pd.read_csv(sentiment_path+"/"+t, header=None)
  maxx1=np.max(data[1])
  if(maxx<maxx1):
    maxx=maxx1
  col = np.where(data[2]=="NEGETIVE",'r',np.where(data[2]=="POSITIVE",'r','k'))
  transparent=data[3].astype(float)
  for x, y, a, c in zip(data[1], data[0], transparent, col):
    plt.scatter(x, y, marker='s',s=400,color=c,alpha=a)
  counter=counter+1

plt.yticks(np.arange(1, counter+1, 1.0))
plt.xticks(np.arange(1, maxx+1, 1.0))

plt.gca().margins(x=0)
plt.gcf().canvas.draw()
tl = plt.gca().get_xticklabels()
maxsize = max([t.get_window_extent().width for t in tl])
m = 0.1 # inch margin
N=16
s = maxsize/plt.gcf().dpi*N+2*m
margin = m/plt.gcf().get_size_inches()[0]

plt.gcf().subplots_adjust(left=margin, right=1.-margin)
plt.savefig('1.png', dpi=300)