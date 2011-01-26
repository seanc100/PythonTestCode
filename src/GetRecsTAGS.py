'''
Created on 2 Sep 2009

@author: corrigan
'''

import httplib

serverUrl = 'localhost:8080'
##serverUrl = 'localhost:8080'
SoapMessage = '''<?xml version='1.0' encoding='UTF-8'?>
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
<soapenv:Body>
<stor:GetRecommendations xmlns:stor="http://schemas.xiam.com/StoreFront">
<stor:QueryTemplateCode>TAG</stor:QueryTemplateCode>
<stor:PhoneNumber>+44101</stor:PhoneNumber>
<stor:DecisionNumberOfResults>10</stor:DecisionNumberOfResults>
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
            ##if line.find("ContentItemTitle") > -1: 
              ##  print line.strip("<ContentItemTitle>").strip().strip("<//ContentItemTitle>")
            if line.find("<ContentItemTitle") > -1: 
                ##print line.strip()
                print line.strip("<ContentItemTitle>").strip().strip("<//ContentItemTitle>")
        
except:
        print 'Problem with this one: '

    
