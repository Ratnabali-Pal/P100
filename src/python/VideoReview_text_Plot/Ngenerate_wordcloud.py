from wordcloud import (WordCloud, get_single_color_func)
import matplotlib.pyplot as plt
import re
from collections import Counter
import nltk
from nltk.corpus import stopwords

# This script assumes 'all_text' is available from text_processing.py
# You might need to load it from a file or integrate the scripts.

nltk.download('stopwords')
sw_nltk = stopwords.words('english')
words = [word for word in all_text.split() if word.lower() not in sw_nltk]
new_text=words
word_could_dict=Counter(new_text)
wc = WordCloud(collocations=False,background_color='#ffffff',random_state=5).generate_from_frequencies(word_could_dict)

plt.figure(figsize=(4,3), dpi=200)
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.savefig('4.png', dpi=300)
plt.show()