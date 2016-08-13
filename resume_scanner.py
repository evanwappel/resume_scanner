#!/usr/bin/python

with open('resume.txt', 'r') as myfile:
    data=myfile.read()
print data

# count the words in the resume
#print "resume word count"
#file=open("resume.txt","r+")
#print file
#wordcount={}
#for word in file.read().split():
#    if word not in wordcount:
#        wordcount[word] = 1
#    else:
#        wordcount[word] += 1
#print type(wordcount)


#import operator
#x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
#sorted_wordcount = sorted(wordcount.items(), key=operator.itemgetter(1), reverse=True)

#for k,v in sorted_wordcount:
#    if v>=2:
#    	print k, v
#print sorted_wordcount

print "job description word count"
file=open("job_description.txt","r+")
wordcount={}
for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
#print type(wordcount)


import operator
#x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_wordcount = sorted(wordcount.items(), key=operator.itemgetter(1), reverse=True)

for k,v in sorted_wordcount:
    if v>=2:
    	print k, v