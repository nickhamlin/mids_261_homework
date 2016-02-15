#HW 5.3 - MRJob Definition
from __future__ import division
import csv

from mrjob.job import MRJob
from mrjob.step import MRStep

class Stripes(MRJob):
    
    def mapper_init(self):
        """Load file of words into memory"""
        self.word_dict={}
        with open('testwords.txt','rb') as f:
            for row in f.readlines():
                line=row.strip().split('\t')
                self.word_dict[line[0][1:-1]]=line[1]
        print self.word_dict

    def mapper(self, _, line):
        """ """
        line=line.strip().split('\t')
        ngram=line[0]
        print ngram
        words=ngram.split(" ")
        for word in words:
            if word.lower() in self.word_dict.keys():
                yield word.lower(),self.word_dict[word.lower()] #Yield the ngram and its count
    
    def mapper_final(self):
        yield '*count',self.count #Yield the total for order-inversion
        
    def reducer_init(self):
        self.total_count=None
            
    def reducer(self,ngram,ngram_count):
        total=sum(ngram_count) #
        overall_total=None
        if ngram=='*count':
            overall_total=total
            self.total_count=total
        else:
            yield ngram,(total, total/self.total_count)
        
    def steps(self):
        return [
            MRStep(
                mapper_init=self.mapper_init,
                mapper=self.mapper
                #,mapper_final=self.mapper_final
                #,combiner=self.reducer
                #,reducer_init=self.reducer_init
                #,reducer=self.reducer
                  )        
        ]
        
if __name__ == '__main__':
    Stripes.run()