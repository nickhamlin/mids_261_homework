#HW 5.3 - MRJob Definition
import csv
import re

from mrjob.job import MRJob
from mrjob.step import MRStep

class MostFreqWords(MRJob):
    
    #SORT_VALUES=True
    
#     def jobconf(self):
#         orig_jobconf = super(MostFreqWords, self).jobconf()        
#         custom_jobconf = {  #key value pairs
#             'mapred.output.key.comparator.class': 'org.apache.hadoop.mapred.lib.KeyFieldBasedComparator',
#             'mapred.text.key.comparator.options': '-k2,2nr',
#             #'mapred.partition.keypartitioner.options':'-k1,1',
#             'mapred.reduce.tasks': '1',
#         }
#         combined_jobconf = orig_jobconf
#         combined_jobconf.update(custom_jobconf)
#         self.jobconf = combined_jobconf
#         return combined_jobconf
            
    def mapper(self, _, line):
        counts = {}
        line.strip()
        [ngram,count,pages,books] = re.split("\t",line)
        count = int(count)
        words = re.split(" ",ngram)
        for word in words:
            counts.setdefault(word.lower(),0)
            counts[word.lower()] += count
        for word in counts.keys():
            yield word,counts[word]
    
    def combiner(self,word,count):
        yield word,sum(count)
            
    def reducer(self,word,count):
        yield word,sum(count)
        
    def mapper_id(self,word,count):
        yield word,count  
        
    def reducer_init(self):
        pass
        
    def steps(self):
        return [
            MRStep(mapper=self.mapper
                   ,combiner=self.combiner
                    ,reducer=self.reducer
                  )
#             ,MRStep(#mapper=self.mapper_id
#                     reducer_init=self.reducer_init
#                     #reducer=self.mapper_id
#                   )   
        ]
        
if __name__ == '__main__':
    MostFreqWords.run()