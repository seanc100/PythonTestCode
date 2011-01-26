'''
Created on 2 Sep 2009

@author: corrigan
'''

import sys,httplib

serverUrl='10.4.125.130:8100'
SoapMessage1='''<?xml version='1.0' encoding='UTF-8'?>
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"><soapenv:Body>
<ns1:GetTopContentByTimeAndAction xmlns:ns1="http://schemas.xiam.com/StoreFront">
<ns1:PhoneNumber>16472875083</ns1:PhoneNumber>
<ns1:DecisionNumberOfResults>10</ns1:DecisionNumberOfResults>
<ns1:HistoryAction>BUY</ns1:HistoryAction>
<ns1:TimePeriod>365D</ns1:TimePeriod>'''

SoapMessage2='''
</ns1:GetTopContentByTimeAndAction>
</soapenv:Body>
</soapenv:Envelope>'''

source=sys.argv[1]
print source

SoapMessage=SoapMessage1 + SoapMessage2
print serverUrl
try:
    webservice = httplib.HTTP(serverUrl)
    webservice.putrequest("POST", "/xiam-content-soap/MessageRouter")
    webservice.putheader("Host", "10.4.125.130")
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
    res = webservice.getfile().readlines()
    for line in res:
        if line.find("ContentItemID") > -1: 
            print line.strip()
        elif line.find("ContentItemName") > -1: 
            print line.strip()
except:
        print 'Problem with this one: ' + res
    
