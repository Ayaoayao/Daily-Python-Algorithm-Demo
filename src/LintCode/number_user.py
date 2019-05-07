#log count differnet user
userArray=[]
nameOccurrence=[]
pullData = open('auth.log','r').read()
dataArray = pullData.split('\n')
# print len(dataArray)
for string in dataArray:
	if 'Failed password for invalid user' in string:
		username=string[string.rfind('user')+5:string.rfind('from')-1]
		userArray.append(username)
# print userArray
newuserArray=list(set(userArray))
print len(newuserArray)