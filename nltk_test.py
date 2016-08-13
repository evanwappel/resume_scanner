import nltk
from nltk import pos_tag, word_tokenize
#from nltk.book import *
#print text6.concordance("camelot")
#print text3.dispersion_plot(["God", "LORD", "Abraham", "Joseph"])
#print sorted(set(text3))
#print len(set(text3))
text = word_tokenize("And now for something completely different")
print nltk.pos_tag(text)

#from __future__ import print_function

#tokenizer = nltk.data.load('nltk:tokenizers/punkt/english.pickle')
#tokenizer.tokenize('Hello.  This is a test.  It works!')



#sentence = """At eight o'clock on Thursday morning
#... Arthur didn't feel very good."""

#tokens == nltk.word_tokenize(sentence)
#print tokens
#['At', 'eight', "o'clock", 'on', 'Thursday', 'morning',
#'Arthur', 'did', "n't", 'feel', 'very', 'good', '.']
#tagged = nltk.pos_tag(tokens)
#print tagged[0:6]
#[('At', 'IN'), ('eight', 'CD'), ("o'clock", 'JJ'), ('on', 'IN'),
#('Thursday', 'NNP'), ('morning', 'NN')]