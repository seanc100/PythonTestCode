'''
Created on 2 Sep 2009

@author: corrigan
'''

tags=[]
print "running parse keywords"
f = open('vodafone-genres.txt', 'r')
for line in f:
        try:  
            newline = line.strip('"')            
            list = newline.split(',')
            for l in list:
                tag  = l.strip('"\n') 
                if tag  not in tags: 
                    tags.append(tag)        
            
        except:
            print 'Problem with this one: ' + list
          
tags.sort()
for t in tags:
    print t