#log analysis
ipArray=[]
ipOccurrence=[]
pullData = open('auth.log','r').read()
dataArray = pullData.split('\n')
# print len(dataArray)
for string in dataArray:
	if 'Failed password for root' in string:
		ipArray_Temp=string[string.rfind('from')+5:string.rfind('port')-1]
		ipArray.append(ipArray_Temp)

#print sorted(ipArray)
# print len(ipArray)
newipArray=list(set(ipArray))
# print newipArray
for ip in newipArray:
	ipOccurrence.append(int(ipArray.count(ip)))

# print ipOccurrence
print max(ipOccurrence)
index =ipOccurrence.index(max(ipOccurrence))
print newipArray[index]