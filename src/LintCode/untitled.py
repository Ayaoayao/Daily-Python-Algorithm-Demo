k = 0
def SortArray(Array):
	global k
	for i in range(len(Array)):
		for j in range (i +1,len(Array)):
			if Array[i] > Array[j]:
				k+=1

dataArray=[4, 80, 70, 23, 9, 60, 68, 27, 66, 78, 12, 40, 52, 53, 44, 8, 49, 28, 18, 46, 21, 39, 51, 7, 87, 99, 69, 62, 84, 6, 79, 67, 14, 98, 83, 0, 96, 5, 82, 10, 26, 48, 3, 2, 15, 92, 11, 55, 63, 97, 43, 45, 81, 42, 95, 20, 25, 74, 24, 72, 91, 35, 86, 19, 75, 58, 71, 47, 76, 59, 64, 93, 17, 50, 56, 94, 90, 89, 32, 37, 34, 65, 1, 73, 41, 36, 57, 77, 30, 22, 13, 29, 38, 16, 88, 61, 31, 85, 33, 54]
Array_a = dataArray[0:50]
Array_b = dataArray[50:100]
SortArray(Array_a)
SortArray(Array_b)
Array_a.sort()
Array_b.sort()
x = 0
y = 0
while (x <=49 and y<=49):
	if Array_a[x] < Array_b[y]:
		x +=1
	elif Array_a[x] > Array_b[y]:
		k = k + 50 - x
		y +=1
print k