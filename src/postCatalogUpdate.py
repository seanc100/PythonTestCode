'''
Created on 2 Sep 2009

@author: corrigan
'''

import httplib

try:
    serverUrl='localhost:8080'
    print 'posting to server: ' + serverUrl
    
    f = open('bms-update-example.xml', 'r')
    xml = f.read()    
    print '\n xml: \n' + xml
    
    
    webservice = httplib.HTTP(serverUrl)
    webservice.putrequest("POST", "/xmc/Catalog")
    webservice.putheader("Content-type", "text/xml")
    webservice.putheader("Content-length", "%d" % len(xml))
    webservice.putheader("X-XIAM-ContentProvider", "Voda")
    webservice.putheader("X-XIAM-ContentUsername", "Voda")
    webservice.putheader("X-XIAM-Contentpassword", "Voda")
    webservice.endheaders()
                
    print 'sending...'
    webservice.send(xml)
                
    # get the response        
    statuscode, statusmessage, header = webservice.getreply()
    print "\nResponse: ", statuscode, statusmessage    
    res = webservice.getfile().read()
    print '\nResponse: \n' + res
except:
    print 'Problem with this one: ' + res
    
