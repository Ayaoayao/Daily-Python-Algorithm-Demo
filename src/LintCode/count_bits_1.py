a = input('Please input an number:')
data=[]
def binary(dec):
	num = 0
	while dec>=1:
		rem = dec%2
		if rem == 1:
			num +=1
		dec = dec/2
	return num


for i in range(a+1):
	s = binary(i)
	data.append(s)
print data


