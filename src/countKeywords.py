'''
Created on 2 Sep 2009

@author: corrigan
'''

from string import punctuation
from operator import itemgetter

N = 10000
words = {}

print "running parse keywords"

try:  
    words_gen = (word.strip(punctuation).lower() for line in open("android-keywords.txt")
                                             for word in line.split(','))
    
    for newword in words_gen:
        word = newword.strip('\n').strip()
        words[word] = words.get(word, 0) + 1       
               
    top_words = sorted(words.iteritems(), key=itemgetter(1), reverse=True)[:N]

    for word, frequency in top_words:
        ##print "%s" % (word)
        ##print "%d" % (frequency)  
        print "%s:  %d" % (word, frequency)       
            
except:
    print 'Problem with this one: '
          

    
