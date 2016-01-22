#!/usr/bin/python

#HW 1.2 - Reducer Function Code
import sys
sum = 0 #Running total of occurrances for the chosen word
for i in sys.stdin:
    line=i.split('\t') #Parse line into a list of fields
    sum+=int(line[1]) #Extract chunk count from the second field of each incoming line
print line[0]+'\t'+str(sum)