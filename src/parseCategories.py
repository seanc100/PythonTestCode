'''
Created on 2 Sep 2009

@author: corrigan
'''

tags=[]
print "running parse Categories"
f = open('5388_010610153335_xiamexport.xml', 'r')
for line in f:
        try:  
            if line.find("<category ") != -1:
                catId = line[line.find("id=")+3:].strip('"')
                catId2 = catId.strip('">\n') 
                #print line
            elif line.find("<name lang=") != -1: 
                if  line.find("ww")!= -1:
                    tag = catId2 + '-' + line.strip('\n').strip('<name lang="ww">').strip('</')
                    print tag
                    if tag  not in tags: 
                        tags.append(tag)
                

            
        except:
            print 'Problem with this one: ' + line
          
tags.sort()
for t in tags:
    print t