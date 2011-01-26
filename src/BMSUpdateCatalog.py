'''
Created on 2 Sep 2009

@author: corrigan
'''
import sys
from urllib import quote

serverUrl = 'localhost:8080'
header = '''<catalog xsi:noNamespaceSchemaLocation="xcp-catalog_1_1.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'''
xml1 = '''
<catalogItemUpdate>
<source val="bds.content" />
<item val="'''
xml2 = '''"/>
<name val="'''
xml3 = '''"/>
<customAttribute val="'''
xml4 = '''" code="Category" action="update"/>
</catalogItemUpdate>'''
footer = '''</catalog>'''


print serverUrl
f = open('BREW_BMS_KEYWORDS.csv', 'r')
itemNameFile = open('brew_item_names.csv', 'r')
f1 = open('bms-update.xml', 'w')
f1.write(header)
res = ''

## read itemNames
line = itemNameFile.readline()
dictName = {}    
while line:
    values = line.split(',')
    dictName[values[0]] = values[1].rstrip('\r\n')      
    line = itemNameFile.readline()
        
print dictName
for line in f:
        try:  
            list = line.split('"')
            print list            
            itemcode = list[0].strip(',') 
            value = list[1].strip(',')
            name = dictName[itemcode]
            print itemcode
            print value
            print name
            Message = xml1 + itemcode.strip() + xml2 + name.replace('&', '&amp;') + xml3 + value.strip() + xml4
            ##print Message
            f1.write(Message)
            
        except:
            print 'Problem with this one: ' + res
            
f1.write(footer)            
    
