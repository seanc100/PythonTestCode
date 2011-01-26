'''
Created on 2 Sep 2009

@author: corrigan
'''

import httplib

serverUrl='10.44.66.153:8080'
xml1='''<soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:stor=\"http://schemas.xiam.com/StoreFront\">
   <soapenv:Header/><soapenv:Body>
      <stor:InsertSubscriberHistoryByNumber>
         <stor:TransactionTime>2010-12-09T17:00:00Z</stor:TransactionTime>
         <stor:HistoryAction>RATE</stor:HistoryAction>
         <stor:Weighting>80</stor:Weighting>
         <stor:ContentItemCode>'''
                  
xml2='</stor:ContentItemCode><stor:PhoneNumber>'
xml3='</stor:PhoneNumber></stor:InsertSubscriberHistoryByNumber></soapenv:Body></soapenv:Envelope>'

print serverUrl
subCount = 2
itemCount = 0
f = open('itemcodes.txt', 'r')
res=''
for line in f:
        itemCount = itemCount + 1
        ##subCount = subCount + 1
        if itemCount < 10000:
            SoapMessage = xml1 + line.strip() + xml2 + '+4410' + str(subCount) + xml3
        
    
            for i in range(1, 2):
                try:
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
    
