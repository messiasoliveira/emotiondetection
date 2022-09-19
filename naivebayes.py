from importlib.metadata import distribution
import nltk
from nltk import ConfusionMatrix
from stopwords import StopWords
from stemming import Stemming
from utils import Utils

class NaiveBayes:
    def __init__(self):
        self.message = None
        self.stemming = Stemming()
        self.stopwords = StopWords()
        self.utils = Utils()
        
    def preprocess(self,base):
        stopwords = self.stopwords.get()
        stemming = self.stemming.apply(base,stopwords)
        searched = self.utils.searchwords(stemming)
        frequencia = self.utils.searchfreq(searched)
        self.utils.set_frequencia(frequencia)
        classify = nltk.classify.apply_features(self.utils.extractorwords,self.stemming.apply(base,stopwords))
        return classify
        
        
    def run(self,treinamento,teste):
        fullbase = self.preprocess(treinamento)
        classificador = nltk.NaiveBayesClassifier.train(fullbase)
        print(classificador.labels())
        print(classificador.show_most_informative_features(5))
        print("Result::",classificador)

        #self.message = self.utils.extractorwords(self.stemming.extract("eu te amo"))
        #self.distribution(classificador)
        baseteste = self.preprocess(teste)
        accu = nltk.classify.accuracy(classificador,baseteste)
        print(accu)
        #self.showerror(baseteste,classificador)
        self.matrizconfusion(baseteste,classificador)

    def showerror(self,base,classificador):
        erros = []
        for (frase,classe) in base:
            resultado = classificador.classify(frase)
            if resultado != classe:
                print(classe,resultado,frase)
                erros.append((classe,resultado,frase))

    def matrizconfusion(self,base,classificador):
        esperado = []
        previsto = []
        for (frase,classe) in base:
            resultado = classificador.classify(frase)
            previsto.append(resultado)
            esperado.append(classe)
        matriz = ConfusionMatrix(esperado,previsto)
        print(matriz)

    def distribution(self,classificador):
        distribution = classificador.prob_classify(self.message)
        for classe in distribution.samples():
            print("%s: %f" % (classe,distribution.prob(classe)))