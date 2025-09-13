import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
from os import listdir
from os.path import isfile, join

dataset = "iphone13"
activity_path="activity/"+dataset
activity_data = [f for f in listdir(activity_path) if isfile(join(activity_path, f))]
print(activity_data)
video_no=1
activity=[]

for t in activity_data:
    data=pd.read_csv(activity_path+"/"+t, header=None)
    data_hand_1=data[data[4]==1]
    data_hand_2=data[data[4]==2]
    
    activity_score_1 = 0
    if not data_hand_1.empty:
        x1=np.array(data_hand_1[2])
        y1=np.array(data_hand_1[3])
        for i in range(len(x1)-1):
          d=math.sqrt((x1[i]-x1[i+1])**2+(y1[i]-y1[i+1])**2)
          activity_score_1=activity_score_1+d

    activity_score_2 = 0
    if not data_hand_2.empty:
        x1=np.array(data_hand_2[2])
        y1=np.array(data_hand_2[3])
        for i in range(len(x1)-1):
          d=math.sqrt((x1[i]-x1[i+1])**2+(y1[i]-y1[i+1])**2)
          activity_score_2=activity_score_2+d
    
    total_activity_score = activity_score_1 + activity_score_2
    activity.append(total_activity_score)
    print(t, video_no, total_activity_score)
    video_no=video_no+1

# Plotting the results
f = plt.figure()
f.set_figwidth(4)
f.set_figheight(2)
activity_normalized = np.array(activity)/np.max(activity)
v=np.arange(1,video_no)

plt.barh(v, activity_normalized, color='dodgerblue')
plt.savefig('7.png', dpi=300)