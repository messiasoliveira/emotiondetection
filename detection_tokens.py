"""
	Tutorial : https://www.youtube.com/watch?v=siVUal-TeMc
	Classes # https://cs.nyu.edu/~grishman/jet/guide/PennPOS.html

"""

import nltk
#nltk.download()
texto = 'Mr. Green killed Colonel Mustard in the study with the candlestick.'
print(texto)

frases = nltk.tokenize.sent_tokenize(texto)
print(frases)

tokens = nltk.word_tokenize(texto)
print(tokens)

classes = nltk.pos_tag(tokens)
print(classes)

entidades = nltk.chunk.ne_chunk(classes)
print(entidades)
