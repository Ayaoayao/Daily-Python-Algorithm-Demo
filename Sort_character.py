# Sort Characters By Frequency
InputString='treasdfklhkadsjfhe'
Frequency=[]
TempInput=list(InputString)
TempInputSet=list(set(TempInput))
TempOutput=[]
for elements in TempInputSet :
	TempValue=[TempInput.count(elements),elements]
	Frequency.append(TempValue)
print Frequency
Frequency=sorted(Frequency, key= lambda quanity : quanity[0]) # sort by frequency
Frequency=reversed(Frequency)

for times in Frequency:
	for i in range(times[0]):
		TempOutput.append(times[1])
TempOutput=''.join(TempOutput)
print TempOutput
