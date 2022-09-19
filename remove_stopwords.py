import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
sw = stopwords.words('portuguese')

#print(textlower.translate({ord('\n'):None,ord('.'):None,ord(','):None}))

nltk.download('brown')
from nltk import FreqDist
from nltk.corpus import brown

##aaa = textlower.translate({ord('\n'):None,ord('.'):None,ord(','):None})
freqs = FreqDist(brown.words())
text_stopwords = {}
for word, freq in freqs.items():
    print(word,freq)
    text_stopwords.append([word,freq for i in sw if i == word])

print(text_stopwords)