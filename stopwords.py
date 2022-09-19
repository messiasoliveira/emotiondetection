import nltk

class StopWords:
    def __init__(self):
        self.extraitems = ['a', 'agora', 'algum', 'alguma', 'aquele', 'aqueles', 'de', 'deu', 'do', 'e', 'estou', 'esta', 'esta',
             'ir', 'meu', 'muito', 'mesmo', 'no', 'nossa', 'o', 'outro', 'para', 'que', 'sem', 'talvez', 'tem', 'tendo',
             'tenha', 'teve', 'tive', 'todo', 'um', 'uma', 'umas', 'uns', 'vou','tão','vai']
    
    def get(self,extraitems=[],language="portuguese"):
        stopwordsnltk = nltk.corpus.stopwords.words(language) 
        stopwordsnltk += self.extraitems + extraitems
        return stopwordsnltk
    
    def remove(self,texto,stopwordsnltk):
        frases = []
        for (palavras, emocao) in texto:
            semstop = [p for p in palavras.split() if p not in stopwordsnltk]
            frases.append((semstop,emocao))
        return frases