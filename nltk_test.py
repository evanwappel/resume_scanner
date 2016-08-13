import nltk
from nltk import pos_tag, word_tokenize
#from nltk.book import *
#print text6.concordance("camelot")
#print text3.dispersion_plot(["God", "LORD", "Abraham", "Joseph"])
#print sorted(set(text3))
#print len(set(text3))

with open('resume.txt', 'r') as myfile:
    resume_text = myfile.read()
with open('job.txt', 'r') as myfile:
    job_text = myfile.read()


#text = word_tokenize(data)
#sent = nltk.pos_tag(text)
#print [s for s in sent if s[1] == 'NN']
#print [s for s in sent if s[1] == 'VB']


from fuzzywuzzy import fuzz

s1 = resume_text
s2 = job_text

print fuzz.partial_ratio(s1, s2)
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