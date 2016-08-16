#!/usr/bin/python

# import resume.txt
file=open("resume.txt","r+")

# create dict
wordcount={}
for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1

# create list from dict
temp = []
for key, value in wordcount.iteritems():
	#print key
	temp.append(key)

# lowercase
temp = [item.lower() for item in temp]

# remove punctuation
import string
punct = set(string.punctuation)
for x in range(0,len(temp)):
	punct_flag = 0
 	for y in range(0,len(punct)):
 		#print x, temp[x], y, list(punct)[y], temp[x].find(list(punct)[y])
 		if temp[x].find(list(punct)[y]) != -1:
 			punct_flag = 1
 			temp[x] = temp[x].replace(list(punct)[y],'')
 			#print punct_flag, temp[x]

# remove duplicates
temp = dict.fromkeys(temp).keys()
# sort
temp.sort();
resume_text = temp











# import resume.txt
file=open("job.txt","r+")

# create dict
wordcount={}
for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1

# create list from dict
temp = []
for key, value in wordcount.iteritems():
	#print key
	temp.append(key)

# lowercase
temp = [item.lower() for item in temp]

# remove punctuation
import string
punct = set(string.punctuation)
for x in range(0,len(temp)):
	punct_flag = 0
 	for y in range(0,len(punct)):
 		#print x, temp[x], y, list(punct)[y], temp[x].find(list(punct)[y])
 		if temp[x].find(list(punct)[y]) != -1:
 			punct_flag = 1
 			temp[x] = temp[x].replace(list(punct)[y],'')
 			#print punct_flag, temp[x]

# remove duplicates
temp = dict.fromkeys(temp).keys()
# sort
temp.sort();
job_text = temp
#print job_text









#Loop through the job decription
matched_list = []
unmatched_list=[]
for x in range(0,len(job_text)):
	match_flag = 0
	for y in range(0,len(resume_text)):
		
		if job_text[x] == resume_text[y]:
			match_flag = 1
			matched_list.append(job_text[x])
			#print x, b_sorted[x], y, a_sorted[y], match_flag
		
		#print y, (len(a_sorted)-1)
		if y == (len(resume_text)-1):
			if match_flag == 0:
				unmatched_list.append(job_text[x])
				#print b_sorted[x]

print "Results:", "\n"
print "matched:", matched_list, "\n"
print "unmatched:", unmatched_list, "\n"

job_word_count = len(job_text)
print round((float(len(matched_list)) / float(job_word_count) * 100),1), "% match", "\n"
