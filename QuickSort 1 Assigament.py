import sys   
sys.setrecursionlimit(100000000)  

k=0
NewArray=[]
def StrtoInt(Array):			#convert the input data from string to int list
	IntArray=[]
	for i in range(len(Array)):
		IntArray.append(int(Array[i]))
	return IntArray

def SortArray(Array,l,r):			#sort array
	global Newarray
	global k
	if r-l  == 0:
		return 0
	else:
		pivot=NewArray[l]     # choose the pivot
		i=l+1
		for j in range(l+1,r+1):
			if NewArray[j] < pivot:		#swap a[i] and a[j].  if the new element is bigger than p, do nothing
				Parameter=NewArray[j]
				NewArray[j]=NewArray[i]
				NewArray[i]=Parameter
				i+=1
			
		AnParameter=NewArray[i-1]   #swap a[l] and a[i-1] after the loop
		NewArray[i-1]=NewArray[l]
		NewArray[l]=AnParameter
		
		k=k+r-l
		
		if i>l+2:
			SortArray(NewArray,l,i-2)  #recursive left array and right array
		if r>i:
			SortArray(NewArray,i,r)


pullData = open('QuickSort.txt','r').read()
dataArray = pullData.split('\n')
NewArray = StrtoInt(dataArray)
SortedArray=SortArray(NewArray,0,len(NewArray)-1)
print 'This is the end of the program'
print k