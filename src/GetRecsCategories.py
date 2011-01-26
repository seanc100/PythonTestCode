'''
Created on 2 Sep 2009

@author: corrigan
'''

import httplib
import urllib;

##serverUrl = '10.44.66.153:8080'
serverUrl = 'localhost:8080'
SoapMessage = '''<?xml version='1.0' encoding='UTF-8'?>
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
<soapenv:Body>
<stor:GetRecommendations xmlns:stor="http://schemas.xiam.com/StoreFront">
<stor:QueryTemplateCode>GETCATEGORIES</stor:QueryTemplateCode>
<stor:PhoneNumber>+44100668</stor:PhoneNumber>
<stor:DecisionConfidenceLevel>1</stor:DecisionConfidenceLevel>
<stor:DecisionNumberOfResults>100</stor:DecisionNumberOfResults>
<stor:CustomAttributes>
<stor:CustomAttribute>
<stor:CustomAttributeName>CategoryName</stor:CustomAttributeName>
<stor:CustomAttributeValue>.*|Sport.*|Football.*|racing.*|health.*|summer.*|Weather.*|(?i)utilities.*|Travel.*|Social.*|News.*|Music.*|(?i)ebooks.*</stor:CustomAttributeValue>
</stor:CustomAttribute>
<stor:CustomAttribute>
<stor:CustomAttributeName>BinaryURL80x80</stor:CustomAttributeName>
<stor:CustomAttributeValue>.*</stor:CustomAttributeValue>
</stor:CustomAttribute>
</stor:CustomAttributes>
</stor:GetRecommendations>
</soapenv:Body>
</soapenv:Envelope>'''

appCount = 0
gameCount = 0
print serverUrl

try:
        webservice = httplib.HTTP(serverUrl)
        webservice.putrequest("POST", "/xiam-content-soap/MessageRouter")
        webservice.putheader("Host", "10.44.66.153")
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
            if line.find("ContentItemTitle") > -1: 
                print line.strip("<ContentItemTitle>").strip().strip("<//ContentItemTitle>")
            ##if line.find("<ContentItemID") > -1: 
                ##print line.strip()
                ##print line.strip("<ContentItemID>").strip().strip("<//ContentItemID>")
        
except:
        print 'Problem with this one: '

    
