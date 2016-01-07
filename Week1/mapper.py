#!/usr/bin/python
import sys
import re
count = 0
WORD_RE = re.compile(r"[\w']+")
filename = sys.argv[2]
findword = sys.argv[1]
with open (filename, "r") as myfile:
    for i in myfile.readlines():
        line=i.lower() #make our search case insensitive
        temp_count=len(re.findall(findword.lower(),line))
        count+=temp_count
print count #We can just print the result to stdout and redirect it in the shell script