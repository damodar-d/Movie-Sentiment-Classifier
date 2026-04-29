import nltk
nltk.download('stopwords')
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

ps = PorterStemmer()

def preprocess_text(text):
    pattern = re.compile('<.*?>')
    result_html_clean = re.sub(pattern,'',text)

    result_special_chars_clean = ''

    for i in result_html_clean:
        if i.isalnum():
            result_special_chars_clean += i
        else:
            result_special_chars_clean+= ' '

    results_lowecase_clean = result_special_chars_clean.lower()

    result_stopword_clean =  []

    for i in results_lowecase_clean.split():
      if i not in stopwords.words('english'):
        result_stopword_clean.append(i)
  
    result = result_stopword_clean[:]
    result_stopword_clean.clear()
    
    y = []

    for i in result:
     y.append(ps.stem(i))
    res = y[:]
    y.clear()
    return " ".join(res)

