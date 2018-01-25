#Next_greater_number
InputArray=[1,2,3]
OutputArray=[]
Length=len(InputArray)
K=InputArray.index(max(InputArray))
for i in range(Length):
	if i==K:
		OutputArray.append(-1)
	else:
		OutputArray.append(max(InputArray))
print OutputArray