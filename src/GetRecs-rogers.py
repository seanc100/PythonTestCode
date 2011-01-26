'''
Created on 2 Sep 2009

@author: corrigan
'''

import sys,httplib

serverUrl='172.25.172.36:8080'
SoapMessage1='''<?xml version='1.0' encoding='UTF-8'?>
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:stor="http://schemas.xiam.com/StoreFront">
<soapenv:Header/>
<soapenv:Body>
<stor:GetSubscriberRecommendationsByNumber>
<stor:PhoneNumber>+101</stor:PhoneNumber> 
<stor:DecisionNumberOfResults>40</stor:DecisionNumberOfResults>
<stor:ContentSourceCodeFilter>
'''
SoapMessage2='''
</stor:ContentSourceCodeFilter>
</stor:GetSubscriberRecommendationsByNumber>
</soapenv:Body>
</soapenv:Envelope>'''

source=sys.argv[1]
print source

SoapMessage= SoapMessage1 + source + SoapMessage2
print serverUrl
try:
    webservice = httplib.HTTP(serverUrl)
    webservice.putrequest("POST", "/xiam-content-soap/MessageRouter")
    webservice.putheader("Host", "172.25.172.36")
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
        if line.find("ContentItemCode") > -1: 
            print line.strip()
        elif line.find("ContentItemName") > -1: 
            print line.strip()
except:
        print 'Problem with this one: ' + res
    
