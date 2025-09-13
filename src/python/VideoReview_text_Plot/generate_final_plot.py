import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

f = plt.figure()
f.set_figwidth(4)
f.set_figheight(2)

# Requires 'data', 'avg_verbal_score', and 'activity' from previous steps.
C1=0.5
C2=0.5
ver_score=C1*avg_verbal_score
activity_score=[]
for x in data[0]:
  activity_score.append(activity[x-1])

vis_score= C2*np.array(activity_score)
final_score=np.add(ver_score,vis_score)
transparent=final_score
transparent=transparent/np.max(transparent)

for x, y, a in zip(data[1], data[0], transparent):
    plt.scatter(x, y, marker='s',s=400,color='crimson',alpha=a)
    
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
plt.savefig('8.png', dpi=300)