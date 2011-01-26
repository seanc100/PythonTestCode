'''
Created on 2 Sep 2009

@author: corrigan
'''

import httplib

serverUrl='localhost:8080'
SoapMessage='''<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:stor="http://schemas.xiam.com/StoreFront">
   <soapenv:Header/>
   <soapenv:Body>
      <stor:GetRelatedItemsByNumber>
         <stor:PhoneNumber>+44100</stor:PhoneNumber>                         
         <stor:ContentItemCode>5862598</stor:ContentItemCode>             
         <stor:CustomAttributes>
            <stor:CustomAttribute>             
               <stor:CustomAttributeCode>PriceCode</stor:CustomAttributeCode>
               <stor:CustomAttributeValue>=EQUAL_TO_ITEM()</stor:CustomAttributeValue>
            </stor:CustomAttribute>
         </stor:CustomAttributes>
      </stor:GetRelatedItemsByNumber>
   </soapenv:Body>
</soapenv:Envelope>'''

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
        if line.find("Value") > -1:         
            print line.strip()
        elif line.find("ContentItemName") > -1: 
            print line.strip()
except:
        print 'Problem with this one: ' + res
    
