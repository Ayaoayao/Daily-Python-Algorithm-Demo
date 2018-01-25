def LIS(nums):
	output=[]
	index1=0
	while(index1<len(nums)-1):
		if nums[index1+1]<=nums[index1]:
			index1+=1
		else:
			break

	while(index1<len(nums)-1):
		index2=index1
		flag=0
		while(index2<len(nums)-1 and flag==0):
			if nums[index2+1]>nums[index2]:
				index2+=1
				if index2==len(nums)-1:
					output.append(int(index2-index1+1))
					index1=index2
			else:
				flag=1
				output.append(int(index2-index1+1))
				index1=index2
		index1+=1
	return output

if __name__ == '__main__':
	test=[5,4,1,2,3,0,1,2,4,5]
	array=LIS(test)
	print(array)