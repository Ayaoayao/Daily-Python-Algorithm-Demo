k = 0
def SortArray(Array):
	global k
	for i in range(len(Array)):
		for j in range (i+1,len(Array)):
			if Array[i] > Array[j]:
				k+=1

def StrtoInt(Array):
	IntArray=[]
	for i in range(len(Array)):
		IntArray.append(int(Array[i]))
	return IntArray

pullData = open('IntegerArray.txt','r').read()
dataArray = pullData.split('\n')
IntdataArray = StrtoInt(dataArray)
Array_a = IntdataArray[0:50000]
Array_b = IntdataArray[50000:100000]
SortArray(Array_a)
SortArray(Array_b)
Array_a.sort()
Array_b.sort()
x = 0
y = 0
while (x <=49999 and y<=49999):
	if Array_a[x] < Array_b[y]:
		x +=1
	elif Array_a[x] > Array_b[y]:
		k = k + 50000 - x
		y +=1
print k

