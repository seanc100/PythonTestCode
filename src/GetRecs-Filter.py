'''
Created on 2 Sep 2009

@author: corrigan
'''

import httplib

serverUrl = 'localhost:8080'
SoapMessage = '''
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
   <soapenv:Body>
      <stor:GetRecommendations xmlns:stor="http://schemas.xiam.com/StoreFront">
         <stor:QueryTemplateCode>RECOMMENDED</stor:QueryTemplateCode>
         <stor:PhoneNumber>44100</stor:PhoneNumber>
         <stor:DecisionConfidenceLevel>1</stor:DecisionConfidenceLevel>
         <stor:DecisionNumberOfResults>10</stor:DecisionNumberOfResults>
         <stor:CustomAttributes>
         <stor:CustomAttribute>
               <stor:CustomAttributeName>ItemTypeIDs</stor:CustomAttributeName>
               <stor:CustomAttributeValue></stor:CustomAttributeValue>
         </stor:CustomAttribute>
         </stor:CustomAttributes>
      </stor:GetRecommendations>
   </soapenv:Body>
</soapenv:Envelope>
'''

appCount = 0
gameCount = 0
print serverUrl

try:
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
        res = webservice.getfile().readlines()
        for line in res:
            if line.find("ContentItemName") > -1: 
                ##print "\n"
                print line.strip()
            ##elif line.find("<CustomAttributeValue>") > -1: 
            ##    print line.strip()
        
except:
        print 'Problem with this one: '

    
