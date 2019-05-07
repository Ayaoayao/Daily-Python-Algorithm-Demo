ori_array = []
out_array = []
result = 1
while(1):
	number = input('please input a number:')
	if number == 0:
		break
	else:
		ori_array.append(number)
for i in range(len(ori_array)):
	result = result * ori_array[i]
for i in range(len(ori_array)):
	out = result/ori_array[i]
	out_array.append(out)
print ori_array 
print out_array