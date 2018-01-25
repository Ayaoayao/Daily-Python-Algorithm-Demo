#The k largest number
n=input('How many largest number you want:')
InputArray=[1,1,1,2,3,3]
OutputArray=[]
TempArray=list(set(InputArray))
for elements in TempArray:
	OutputArray.append([InputArray.count(elements),elements])
print OutputArray[0:n]
