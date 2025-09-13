from os import listdir
from os.path import isfile, join

dataset="iphone13"
text_path="text/"+dataset

text_data = [f for f in listdir(text_path) if isfile(join(text_path, f))]
all_text=""
for t in text_data:
  with open(text_path+"/"+t) as f:
    lines=f.readlines()
  text=str(lines[0])
  text=text.split("@")

  for i in range(len(text)):
    data = text[i]
    all_text=all_text+" "+str(data)