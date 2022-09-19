import nltk
import stopwords

class Stemming:
    def apply(self,text,stopwordsnltk):
        stemmer = nltk.stem.RSLPStemmer()
        frasesstemming = []
        for (palavras,emocao) in text:
            comstemming = [str(stemmer.stem(p)) for p in palavras.split() if p not in stopwordsnltk]
            frasesstemming.append((comstemming,emocao))
        return frasesstemming

    def extract(self,frase):
        testestemming = []
        stemmer = nltk.stem.RSLPStemmer()
        for (palavras) in frase.split():
            comstem = [p for p in palavras.split()]
            testestemming.append(str(stemmer.stem(comstem[0])))
        print(testestemming)
        return testestemming
