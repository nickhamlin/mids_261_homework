#!/usr/bin/python
import sys
import re
WORD_RE = re.compile(r"[\w']+") #Compile regex to easily parse complete words
filename = sys.argv[1]
findwords = sys.argv[2].lower() 
with open (filename, "r") as myfile:
    for num,line in enumerate(myfile.readlines()):
        fields=line.split('\t') #parse line into separate fields
        subject_and_body=" ".join(fields[-2:]).strip()#parse the subject and body fields from the line, and combine into one string
        words=re.findall(WORD_RE,subject_and_body) #create list of words
        for word in words:
            flag=0
            if word in findwords:
                #This flag indicates to the reducer that a given word should be considered
                #by the reducer when calculating the conditional probabilities
                flag=1 
                
            #This will send one row for every word instance to the reducer.
            print fields[0]+'\t'+fields[1]+'\t'+word+'\t1\t'+str(flag)