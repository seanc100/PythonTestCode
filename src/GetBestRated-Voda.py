'''
Created on 2 Sep 2009

@author: corrigan
'''

import sys,httplib

serverUrl='localhost:8080'
SoapMessage1='''<?xml version='1.0' encoding='UTF-8'?>
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
<soapenv:Body>
<stor:GetRecommendations xmlns:stor="http://schemas.xiam.com/StoreFront">
<stor:QueryTemplateCode>BESTRATEDd</stor:QueryTemplateCode>
<stor:PhoneNumber>+44107</stor:PhoneNumber>
<stor:DecisionConfidenceLevel>1</stor:DecisionConfidenceLevel>
<stor:DecisionNumberOfResults>5</stor:DecisionNumberOfResults>
</stor:GetRecommendations>
</soapenv:Body>
</soapenv:Envelope>'''

source=sys.argv[1]
print source

SoapMessage=SoapMessage1
print serverUrl
try:
    webservice = httplib.HTTP(serverUrl)
    webservice.putrequest("POST", "/xiam-content-soap/MessageRouter")
    webservice.putheader("Host", "xiamvfweb03")
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
        if line.find("ContentItemName") > -1: 
            print line.strip()
        elif line.find("Rate") > -1: 
            print line.strip()
except:
        print 'Problem with this one: ' + res
    
