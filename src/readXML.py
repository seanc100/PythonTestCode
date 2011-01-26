'''
Created on 2 Sep 2009

@author: corrigan
'''
import sys
from xml.etree import ElementTree as ET

xmlfilename = '5388.xml'
print 'Reading xml file'                                         

tree = ET.parse(xmlfilename).getroot()
#tree.write(sys.stdout) 

#Create an iterator
iter = tree.getiterator()
for element in iter:
    #First the element tag name
   print "Element:", element.tag
 


