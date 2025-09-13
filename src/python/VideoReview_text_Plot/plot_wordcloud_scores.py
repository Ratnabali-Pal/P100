import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas.errors import EmptyDataError

dataset = "iphone13"
cloud_path="wordcloud/"+dataset+"/cloud.txt"

f = plt.figure()
f.set_figwidth(4)
f.set_figheight(2)
try:
    data=pd.read_csv(cloud_path, header=None)
    transparent=data[2].astype(float)
    transparent=transparent/np.max(transparent)
    word_cloud_score=transparent
    for x, y, a in zip(data[1], data[0], transparent):
        plt.scatter(x, y, marker='s',s=400,color='maroon',alpha=a)
    
    # These variables (counter, maxx, maxsize) would need to be passed from other scripts
    # For example:
    # counter = 10
    # maxx = 15
    # maxsize = 100

    plt.yticks(np.arange(1, counter, 1.0))
    plt.xticks(np.arange(1, maxx+1, 1.0))

    plt.gca().margins(x=0)
    plt.gcf().canvas.draw()
    tl = plt.gca().get_xticklabels()

    plt.gca().margins(x=0)
    plt.gcf().canvas.draw()
    tl = plt.gca().get_xticklabels()
    m = 0.1 # inch margin
    N=16
    s = maxsize/plt.gcf().dpi*N+2*m
    margin = m/plt.gcf().get_size_inches()[0]

    plt.gcf().subplots_adjust(left=margin, right=1.-margin)
    plt.savefig('5.png', dpi=300)
except EmptyDataError:
    print(f"File {cloud_path} is empty. Skipping plot generation.")