'''
Created on 2 Sep 2009

@author: corrigan
'''

import httplib

serverUrl = 'localhost:8080'
SoapMessage = '''<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:stor="http://schemas.xiam.com/StoreFront">
   <soapenv:Header/>
   <soapenv:Body>
      <stor:GetRecommendations>
         <stor:QueryTemplateCode>MOSTDOWNLOADEDd</stor:QueryTemplateCode>
         <stor:PhoneNumber>+44100</stor:PhoneNumber> 
         <stor:LogRecommendation>TRUE</stor:LogRecommendation>     
          <stor:DecisionNumberOfResults>10</stor:DecisionNumberOfResults>
         <stor:SortField>ci:title</stor:SortField>  
         <!-- stor:SortField>ci:name</stor:SortField -->             
      </stor:GetRecommendations>
   </soapenv:Body>
</soapenv:Envelope>'''

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
            if line.find("ContentItemTitle") > -1: 
                print line.strip()
            ##elif line.find("ContentItemCode") > -1: 
                ##print line.strip()
        
except:
        print 'Problem with this one: ' + res

    
