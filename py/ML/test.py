from py.ML.bayes import *

listOPost, listClasses = loadDataSet()
myVocabList = createVocabList(listOPost)
myVocabList = ['cute', 'love', 'help', 'garbage', 'quit', 'I', 'problems', 'is', 'park',
               'stop', 'flea', 'dalmation', 'licks', 'food', 'not', 'him', 'buying',
               'posting', 'has', 'worthless', 'ate', 'to', 'maybe', 'please', 'dog', 'how',
               'stupid', 'so', 'take', 'mr', 'steak', 'my']

setOfWord2Vec(myVocabList,listOPost[0])
setOfWord2Vec(myVocabList,listOPost[3])