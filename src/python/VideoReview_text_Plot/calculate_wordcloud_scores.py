# This script requires 'text_data' and 'word_could_dict' from previous steps.

def get_segment_cloud(words,cloud):
  score=0
  for w in words:
   score=score+cloud.get(w, 0) # Use .get for safety
  return score

dataset = "iphone13"
counter=1
cloud_path="wordcloud/"+dataset+"/cloud.txt"
fh = open(cloud_path, "w+")
for t in text_data:
  segment=1
  with open("text/"+dataset+"/"+t) as f:
    lines=f.readlines()
  text=str(lines[0])
  text=text.split("@")
  for i in range(len(text)):
    data = text[i].split(' ')
    res=get_segment_cloud(data,word_could_dict)
    fh.write(str(counter)+","+str(segment)+","+str(res)+"\\n")
    segment=segment+1
  counter=counter+1
fh.close()