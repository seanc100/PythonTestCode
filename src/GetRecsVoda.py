'''
Created on 2 Sep 2009

@author: corrigan
'''

import httplib

##serverUrl = 'localhost:8080'
## voda dev server
serverUrl = '10.44.66.153:20000'
SoapMessage = '''<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
   <soapenv:Body>
      <stor:GetRecommendations xmlns:stor="http://schemas.xiam.com/StoreFront">
         <stor:QueryTemplateCode>RECOMMENDEDd</stor:QueryTemplateCode>
         <stor:PhoneNumber>44101</stor:PhoneNumber>
         <stor:DecisionConfidenceLevel>1</stor:DecisionConfidenceLevel>
         <stor:DecisionNumberOfResults>10</stor:DecisionNumberOfResults>
         <stor:ItemSkipList>5870017</stor:ItemSkipList>
         <stor:Pagination>
            <stor:ListEnabled>false</stor:ListEnabled>
            <stor:ListId>-1</stor:ListId>
         </stor:Pagination>
         <stor:SubscriberAttributes/>
         <stor:CustomAttributes>
            <stor:CustomAttribute>
               <stor:CustomAttributeName>ContentGrading</stor:CustomAttributeName>
               <stor:CustomAttributeValue>=LESS_THAN_OR_EQUAL_TO(60)</stor:CustomAttributeValue>
            </stor:CustomAttribute>
            <stor:CustomAttribute>
               <stor:CustomAttributeName>ItemTypeIds</stor:CustomAttributeName>
               <stor:CustomAttributeValue>2091|1915|2214|2213|2215|2212|2210|2216</stor:CustomAttributeValue>
            </stor:CustomAttribute>
            <stor:CustomAttribute>
               <stor:CustomAttributeName>BinaryURL80x80</stor:CustomAttributeName>
               <stor:CustomAttributeValue>.*</stor:CustomAttributeValue>
            </stor:CustomAttribute>
         </stor:CustomAttributes>
         <stor:LogRecommendation>TRUE</stor:LogRecommendation>
         <stor:ExtraReference>/73/135922/148337/5870017</stor:ExtraReference>
         <stor:ExtraReference2>1352</stor:ExtraReference2>
         <stor:ExtraReference3>Vodafone/1.0/GT-I6410/I6410BUJC1 Java/VF-Java/1.0 profile/MIDP-2.1 configuration/CLDC-1.1</stor:ExtraReference3>
         <stor:ExtraReference5>vertical</stor:ExtraReference5>
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
            ##if line.find("ContentItemTitle") > -1: 
              ##  print line.strip("<ContentItemTitle>").strip().strip("<//ContentItemTitle>")
            if line.find("<ContentItemName") > -1: 
                ##print line.strip()
                print line.strip("<ContentItemName>").strip().strip("<//ContentItemName>")
        
except:
        print 'Problem with this one: ' + res

    
