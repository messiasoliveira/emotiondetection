from importlib.metadata import distribution
import nltk

from stopwords import StopWords
#nltk.download("all")
### remove special characters
nltk.download("stopwords")
nltk.download('rslp')

base = [('eu sou admirada por muitos','alegria'),
        ('me sinto completamente amado','alegria'),
        ('amar e maravilhoso','alegria'),
        ('estou me sentindo muito animado novamente','alegria'),
        ('eu estou muito bem hoje','alegria'),
        ('que belo dia para dirigir um carro novo','alegria'),
        ('o dia esta muito bonito','alegria'),
        ('estou contente com o resultado do teste que fiz no dia de ontem','alegria'),
        ('o amor e lindo','alegria'),
        ('nossa amizade e amor vai durar para sempre', 'alegria'),
        ('estou amedrontado', 'medo'),
        ('ele esta me ameacando a dias', 'medo'),
        ('isso me deixa apavorada', 'medo'),
        ('este lugar e apavorante', 'medo'),
        ('se perdermos outro jogo seremos eliminados e isso me deixa com pavor', 'medo'),
        ('tome cuidado com o lobisomem', 'medo'),
        ('se eles descobrirem estamos encrencados', 'medo'),
        ('estou tremendo de medo', 'medo'),
        ('eu tenho muito medo dele', 'medo'),
        ('estou com medo do resultado dos meus testes', 'medo')]

stopwords = ['a', 'agora', 'algum', 'alguma', 'aquele', 'aqueles', 'de', 'deu', 'do', 'e', 'estou', 'esta', 'esta',
             'ir', 'meu', 'muito', 'mesmo', 'no', 'nossa', 'o', 'outro', 'para', 'que', 'sem', 'talvez', 'tem', 'tendo',
             'tenha', 'teve', 'tive', 'todo', 'um', 'uma', 'umas', 'uns', 'vou']


stopwordsnltk = nltk.corpus.stopwords.words("portuguese")
stopwordsnltk.append("vou")
stopwordsnltk.append("tão")
stopwordsnltk.append("vai")
def removestopword(texto):
    frases = []
    for (palavras, emocao) in texto:
        semstop = [p for p in palavras.split() if p not in stopwordsnltk]
        frases.append((semstop,emocao))
    return frases

print(removestopword(base))

def applystemmer(text):
    stemmer = nltk.stem.RSLPStemmer()
    frasesstemming = []
    for (palavras,emocao) in text:
        comstemming = [str(stemmer.stem(p)) for p in palavras.split() if p not in stopwordsnltk]
        frasesstemming.append((comstemming,emocao))
    return frasesstemming

#print(applystemmer(base))

def searchwords(frase):
    allwords = []
    for (palavras,emocao) in frase:
        allwords.extend(palavras)
    return allwords

#print(searchwords(applystemmer(base)))

def searchfreq(words):
    return nltk.FreqDist(words)

frequencia = searchfreq(searchwords(applystemmer(base)))
#print(frequencia.most_common(50))

def searchonewords(frequencia):
    return frequencia.keys()
    
onewords = searchonewords(frequencia)
#print(onewords)

def extractorwords(text):
    doc = set(text)
    features = {}
    for words in searchonewords(frequencia):
        features['%s' % words] = (words in doc)
    return features
featuresonewords = extractorwords(['am','nov','dia'])
#print(featuresonewords)

fullbase = nltk.classify.apply_features(extractorwords,applystemmer(base))
#print(fullbase)

# prob table
classificador = nltk.NaiveBayesClassifier.train(fullbase)
#print(classificador.labels())
#print(classificador.show_most_informative_features(5))

def extract_stemming(frase):
    testestemming = []
    stemmer = nltk.stem.RSLPStemmer()
    for (palavras) in frase.split():
        comstem = [p for p in palavras.split()]
        testestemming.append(str(stemmer.stem(comstem[0])))
    print(testestemming)
    return testestemming

testestemming = extract_stemming("eu sinto amor por você")

novo = extractorwords(testestemming)
#print(novo)

result = classificador.classify(novo)
print(result)

distribution = classificador.prob_classify(novo)
for classe in distribution.samples():
    print("%s: %f" % (classe,distribution.prob(classe)))


# frasescomstemmingteste = applystemmer(baseteste)
# fullbase = nltk.classify.apply_features(extractorwords,applystemmer(basetreinamento))
# #print(fullbase)
# palavrasteste = searchwords(applystemmer(baseteste))
# # prob table
# classificador = nltk.NaiveBayesClassifier.train(fullbase)
# #print(classificador.labels())
# #print(classificador.show_most_informative_features(5))

# testestemming = extract_stemming("eu sinto amor por voce")

# novo = extractorwords(testestemming)
# print(novo)

# result = classificador.classify(novo)
# print(result)

# distribution = classificador.prob_classify(novo)
# for classe in distribution.samples():
#     print("%s: %f" % (classe,distribution.prob(classe)))