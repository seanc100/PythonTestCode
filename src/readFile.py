
import sys

## set up counters
timeLimit = 20

## time taken counters
ten =0
twenty =0
thirty = 0
forty = 0
fifty = 0
sixty = 0
seventy = 0
eighty = 0
ninety = 0
hundred = 0
plus100 = 0
singleRequestCount = 0
multiRequestCount = 0
subhistoryCount = 0
error=0

## lookup counters
rechistory = 0
subscriber = 0
group = 0
allowRestrictedOff = 0
allowRestrictedOn = 0
gender = 0
DOB = 0

## profile counters
zerorecs = 0
profileupdates = 0
likes = 0
buys = 0
errors = 0 
catalogupdates = 0 
catalogdeletes = 0
timeLimitAborts = 0

## times and counts arrays
times = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
counts = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
print times

## open file
filename = sys.argv[1]
print "Opening File %s" % (filename)
f=open(filename, 'r')

## read lines from file
for line in f:			
		## if single request
		try:
			if line.find("TomcatSOAPInterface::GetSubRecs:: took") != -1:
				singleRequestCount = singleRequestCount + 1
				bits = line.split(' ')
				if len(bits) > 0:						
					##print bits				
					time = int(bits[7].strip("ms\n"))
					if (time >= 0 and time <= 10):
						ten += 1
					if (time >= 10 and time <= 20):
						twenty += 1  					
					if (time >= 20 and time <= 30):
						thirty += 1  
					if (time >= 30 and time <= 40):
						forty += 1 
					if (time >= 40 and time <= 50):
						fifty += 1 
					if (time >= 50 and time <= 60):
						sixty += 1 
					if (time >= 60 and time <= 70):
						seventy += 1  	
					if (time >= 70 and time <= 80):
						eighty += 1  
					if (time >= 80 and time <= 90):
						ninety += 1 
					if (time >= 90 and time <= 100):
						hundred += 1 					
					if (time >= 100):
						plus100 += 1
					
					## incremet hour and counts	
					timestamp = bits[1];
					hours = timestamp.split(':')
					hour = int(hours[0])					
					if hour >= 0 and hour <= 24:						 						 
						 times[hour] += 1					 
						 if time > 40:							
							counts[hour] += 1;
						
		
			## if subscriberHistory			
			elif line.find("Time taken to get subscriberHistory") != -1:				
				subhistoryCount += 1
				## print line
				
			## if subscriberHistory			
			elif line.find("GroupRecommender: Time taken to get groups for subscriber") != -1:				
				subscriber += 1
				## print line
				
			## if subscriberHistory			
			elif line.find("RecommendationHistoryThread: Time taken to get rec history") != -1:				
				rechistory += 1
				## print line
				
			## if subscriberHistory			
			elif line.find("Time taken to get subscriber") != -1:				
				subscriber += 1
				## print line
				
			## if subscriberHistory			
			elif line.find("TomcatSOAPInterface::GetSubRecsMulti:: took") != -1:				
				multiRequestCount += 1
				## print line	
				
			## if subscriberHistory			
			elif line.find("filterRecommendations:: found 0 recs before filtering") != -1:				
				zerorecs += 1
				## print line	
				
			## if subscriberHistory			
			elif line.find("<profileUpdateRequest>") != -1:				
				profileupdates += 1
				## print line	
				
			## if subscriberHistory			
			elif line.find("historyAction val=\"like\"") != -1:				
				likes += 1
				## print line	
				
			## if subscriberHistory			
			elif line.find("historyAction val=\"buy\"") != -1:				
				buys += 1
				## print line	
				
			## if subscriberHistory			
			elif line.find("allowRestrictedContent val=\"false\"") != -1:				
				allowRestrictedOff += 1
				## print line			
				
			## if subscriberHistory			
			elif line.find("allowRestrictedContent val=\"true\"") != -1:				
				allowRestrictedOn += 1
				## print line	
				
			## if subscriberHistory			
			elif line.find("customAttribute code=\"Gender\"") != -1:				
				gender += 1
				## print line	
				
			## if subscriberHistory			
			elif line.find("customAttribute code=\"DOB\"") != -1:				
				DOB += 1
				## print line	
				
			## if subscriberHistory			
			elif line.find("Error") != -1:				
				error += 1
				## print line
				
			## if subscriberHistory			
			elif line.find("catalogItemUpdate") != -1:				
				catalogupdates += 1
				## print line		
				
			## if subscriberHistory			
			elif line.find("catalogItemDelete") != -1:				
				catalogdeletes += 1
				## print line	
				
			## if subscriberHistory			
			elif line.find("recommendation generation cut short by time limit") != -1:				
				timeLimitAborts += 1
				## print line																																																																			

		except:
			pass
	
	
print	
print "Report for file:  %s" % (filename)
print
print "Total Single requests = %d" % (singleRequestCount)	
print "Total Multi requests = %d" % (multiRequestCount)	
print

if(singleRequestCount > 0):
	print "zero recs:\t %3.2f" % (zerorecs*100/singleRequestCount)
	print "aborted:\t %3.2f" % (timeLimitAborts*100/singleRequestCount)


print
print "profileUpdates:"
print "likes: %d" % likes
print "buys: %d" % buys
print "gender: %d" % gender
print "DOB: %d" % DOB
print "allow restricted: %d" % allowRestrictedOn
print "disallow restricted: %d" % allowRestrictedOff
print "catalogupdates: %d" % catalogupdates
print "catalogdeletes: %d" % catalogdeletes

print "log contains errors/exceptions: %d" % (errors)

if(singleRequestCount > 0):
	print
	print "Stats for Single requests:"
	print "sub activity\t over the  %dms limit: %d" % (timeLimit, subhistoryCount)
	print "rec history\t over the  %dms limit: %d" % (timeLimit, rechistory)
	print "subscriber\t over the  %dms limit: %d" % (timeLimit, subscriber)
	print "sub group\t over the  %dms limit: %d" % (timeLimit, group)
	print

print "Response times histogram:"
print "10ms\t 20ms\t 30ms\t 40ms\t 50ms\t 60ms\t 70ms\t 80ms\t 90ms\t 100ms\t +100ms"
print "%2.1f\t %2.1f\t %2.1f\t %2.1f\t %2.1f\t %2.1f\t %2.1f\t %2.1f\t %2.1f\t %2.1f\t %2.1f" % ((ten*100/singleRequestCount), (twenty*100/singleRequestCount), 
														 (thirty*100/singleRequestCount), (forty*100/singleRequestCount), 
														 (fifty*100/singleRequestCount), (sixty*100/singleRequestCount), 
														 (seventy*100/singleRequestCount), (eighty*100/singleRequestCount), 
														 (ninety*100/singleRequestCount), (hundred*100/singleRequestCount), 
														 (plus100*100/singleRequestCount))

print
print "Percent of requests over 40ms: %3.2f" % ((forty*100/singleRequestCount) + 
														 (fifty*100/singleRequestCount) + (sixty*100/singleRequestCount) +
														 (seventy*100/singleRequestCount) + (eighty*100/singleRequestCount) +
														 (ninety*100/singleRequestCount) + (hundred*100/singleRequestCount) + 
														 (plus100*100/singleRequestCount))

print "Times > 40ms by hour:"
print "hour\t count\t %over 40ms"
hour =0
for i in times:	
	if i > 0:
		print "%d \t %d \t %3.2f" % (hour, i, (counts[hour]*100.0/times[hour]))
	else:
	    print "%d \t %d \t %3.2f" % (hour, i, 0)
	hour += 1
	

