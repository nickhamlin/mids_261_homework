#!/usr/bin/python

#HW 1.4 - Mapper Function
import sys
import re
WORD_RE = re.compile(r"[\w']+")
filename = sys.argv[1]
findwords = sys.argv[2].lower().split() 
with open (filename, "r") as myfile:
    for num,line in enumerate(myfile.readlines()):
        fields=line.split('\t') #parse line into separate fields
        subject_and_body=" ".join(fields[-2:]).strip()#parse the subject and body fields from the line, and combine into one string
        words=re.findall(WORD_RE,subject_and_body)
        for word in words:
            flag=0
            if word in findwords:
                flag=1
            print fields[0]+'\t'+fields[1]+'\t'+word+'\t1\t'+str(flag)