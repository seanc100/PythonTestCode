'''
Created on 2 Sep 2009

@author: corrigan
'''

import httplib

serverUrl='10.4.125.130:8100'
serverUrl2='localhost:8080'
SoapMessage='''<?xml version='1.0' encoding='UTF-8'?>
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
<soapenv:Body>
<stor:GetSubscriberRecommendationsByNumber xmlns:stor="http://schemas.xiam.com/StoreFront">
<stor:PhoneNumber>+44100</stor:PhoneNumber>
<stor:DecisionNumberOfResults>10</stor:DecisionNumberOfResults>
<stor:MaxTimesToRecommendItem>5</stor:MaxTimesToRecommendItem>
<stor:CustomAttributes>
<stor:CustomAttribute>
<stor:CustomAttributeName>ContentChannelRef</stor:CustomAttributeName>
<stor:CustomAttributeValue>=MAX(5,11,true);MAX(5,73,true)</stor:CustomAttributeValue>
</stor:CustomAttribute>
</stor:CustomAttributes>
</stor:GetSubscriberRecommendationsByNumber>
</soapenv:Body>
</soapenv:Envelope>'''

print serverUrl2
try:
    webservice = httplib.HTTP(serverUrl2)
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
    res = webservice.getfile().readlines()
    for line in res:
        if line.find("ContentSourceCode") > -1: 
            print line.strip()
        elif line.find("ContentItemName") > -1: 
            print line.strip()
except:
        print 'Problem with this one: ' + res
    
