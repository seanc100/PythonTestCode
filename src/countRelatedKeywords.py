'''
Created on 2 Sep 2009

@author: corrigan
'''

from operator import itemgetter

N = 10000
listofwords = []
words = {}
relatedWords = {}

print "running parse keywords"

try:  
    for line in open("vodafone-keywords.txt"):
         line = line.strip('\n') 
         listofwords = line.split(',')
         for word in line.split(','):
            newword = word.strip().lower()
            word = newword.strip('\n')            
            words[word] = words.get(word, 0) + 1   
            if relatedWords.get(word):
                listrelatedWords = relatedWords.get(word)
                for w1 in listofwords:
                    if w1.lower() != word.lower():
                        if w1 not in listrelatedWords:
                            listrelatedWords.append(w1)
                relatedWords[word] = listrelatedWords
            else:
                relatedWords[word] = listofwords
           
    related_words = sorted(relatedWords.iteritems(), key=itemgetter(0), reverse=False)[:N]
       
    f = open('related-words.txt', 'w') 
    for word, listofwords in related_words:
        print "\n" +  word 
        print listofwords  
        f.writelines("%s=" % word)
        for item in listofwords:
            f.writelines("%s," % item)
        f.writelines("\n")

        ##f.write(listofwords)     
            
except:
    print 'Problem with this one: '
          