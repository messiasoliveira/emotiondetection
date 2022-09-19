import nltk
from stemming import Stemming

class Utils:
    def __init__(self):
        self.frequencia = None

    def set_frequencia(self, frequencia):
        self.frequencia = frequencia

    def searchwords(self, frase):
        allwords = []
        for (palavras,emocao) in frase:
            allwords.extend(palavras)
        return allwords

    def searchonewords(self, frequencia):
        return frequencia.keys()

    def searchfreq(self,words):
        return nltk.FreqDist(words)
    
    def getfreq(self,base):
        return self.searchfreq(self.searchwords(Stemming.apply(base)))

    def extractorwords(self,text):
        doc = set(text)
        features = {}
        for words in self.searchonewords(self.frequencia):
            features['%s' % words] = (words in doc)
        return features