'''
Created on 2 Sep 2009

@author: corrigan
'''

import urllib2

serverUrl='http://xiamvfweb05:8080/fi/feedback?tranid=1001&id='
#serverUrl='http://10.4.125.130:8100/fi/feedback?tranid=1001&id='
testUrl2='&action=BUY&subid='
testUrl3='&opcoid=101&devicecode=1013&useragent=Nokia6600&actiontime=2009-09-02T12%3A00%3A00-0000&fromrt=TRUE&slotid=101&applicationid=widget&rating=5'
count = 0
f = open('itemcodes.txt', 'r')
for line in f:
    count = count + 1
    url = serverUrl + line.strip() + testUrl2 + 'test' + str(count) + testUrl3
    print url
    try:
        urllib2.urlopen(url)
    except:
        print 'Problem with this one: ' + url
    
