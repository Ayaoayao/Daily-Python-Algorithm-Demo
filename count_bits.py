def binary(dec):
	global num 
	if dec<1:
		return 0 
	rem = dec%2
	if rem == 1:
		num +=1
	binary(dec/2)
	return num

num = 0
data = []
dec=input("Enter decimal to be converted: ")
for i in range(dec+1):
	s = binary(i)
	global num
	num = 0
	data.append(s)
print "The bits of the given number is ",data,'.'