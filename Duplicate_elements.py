#find duplicate elements in array
TestArray=[4,3,2,7,8,2,3,1]
NoDuplicatedArray=list(set(TestArray))
OutputArray=[]
print NoDuplicatedArray
for elements in NoDuplicatedArray:
	if TestArray.count(elements) == 2:
		print elements
		OutputArray.append(elements)
print OutputArray