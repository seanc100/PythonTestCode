import os, glob
import fnmatch


javacount = 0
list = []

def scandirs(path, list):	
    for currentFile in glob.glob(os.path.join(path, '*')):
        if os.path.isdir(currentFile):
            ##print 'got a directory: ' + currentFile
            scandirs(currentFile, list)        
        if fnmatch.fnmatch(currentFile, '*.java'):               
            ##print "Opening File %s" % (currentFile)
            f = open(currentFile, 'r')       
            for line in f:					           
            	if line.find("PP_TXT_DECISION") != -1:
            		property = line[line.find("PP_TXT"):]
            		if property.find(","):
            			property = property[:property.find(",")]
            			if property.find("=") == -1:
            				property = property.strip(';').strip(')')
            				property = property[property.find("PP_TXT")+7:]            				
            				if property not in list:
            				    list.append(property)            				




	
def readhtml(filename, list):	
	print "reading file" + filename
	f = open(filename, 'r')       
	text = f.read()
	##print text
	list.sort()
	for item in list:
		##print 'searching for property ' + item
		if item not in text:			
		   print 'NOT found property ' + item
		
            	  
        	
print "Running with path " + 'C:/projects/trunk/source/'
scandirs('C:\\projects\\trunk\\source\\', list)
	
readhtml('C:\\projects\\trunk\\doc\\decision\\Decision Configuration Guide.htm', list)
	






