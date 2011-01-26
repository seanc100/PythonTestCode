'''
Created on 2 Sep 2009

@author: corrigan
'''

import httplib

serverUrl='localhost:8080'
xml1='''<soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:stor=\"http://schemas.xiam.com/StoreFront\">
   <soapenv:Header/><soapenv:Body>
      <stor:InsertSubscriberHistoryByNumber>
         <stor:TransactionTime>2010-08-16T15:40:00Z</stor:TransactionTime>
         <stor:HistoryAction>BUY</stor:HistoryAction>
         <stor:Weighting>100</stor:Weighting>
         <stor:ContentItemCode>'''
                  
xml2='</stor:ContentItemCode><stor:PhoneNumber>'
xml3='</stor:PhoneNumber></stor:InsertSubscriberHistoryByNumber></soapenv:Body></soapenv:Envelope>'

print serverUrl
f = open('itemcodes.txt', 'r')
res=''
for line in f:  
    count=0  
    for i in range(1, 4):
        try:
            count = count + 1    
            SoapMessage = xml1 + line.strip() + xml2 + 'test101' + str(count) + xml3
            print SoapMessage
            #urllib2.urlopen(url)
            #construct and send the header
            webservice = httplib.HTTP(serverUrl)
            webservice.putrequest("POST", "/xiam-content-soap/MessageRouter")
            webservice.putheader("Host", "localhost")
            webservice.putheader("User-Agent", "Mozilla")
            webservice.putheader("Content-type", "text/xml; charset=\"UTF-8\"")
            webservice.putheader("Content-length", "%d" % len(SoapMessage))
            webservice.putheader("SOAPAction", "\"\"")
            webservice.endheaders()
            
            print 'sending...'
            webservice.send(SoapMessage)
            
            # get the response        
            statuscode, statusmessage, header = webservice.getreply()
            print "Response: ", statuscode, statusmessage
            print "headers: ", header
            res = webservice.getfile().read()
            print res
        except:
            print 'Problem with this one: ' + res
    
