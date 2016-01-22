#!/usr/bin/python

#HW 1.2 - Mapper Function Code
import sys
count = 0 #Running total of occurrances for the chosen word
findword = "assistance" 
for line in sys.stdin:
    subject_and_body=" ".join(line.split('\t')[-2:])#parse the subject and body fields from the line, and combine into one string
    count+=subject_and_body.count(findword) #Python's str.count() method makes counting the instances of the word easy
print findword+'\t'+str(count)