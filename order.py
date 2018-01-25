def permute(nums):
	ReturnArray=[]
	if len(nums)==1:
		ReturnArray.append(nums)
		return ReturnArray

	else:
		for element in nums:
			temp=nums[:]
			temp.remove(element)
			TempList=permute(temp)
			for array in TempList:
				try: 
					ReturnArray.index(array+[element])
				except ValueError:
					ReturnArray.append(array+[element])
				else:
					pass
				try:
					ReturnArray.index([element]+array)
				except ValueError:
					ReturnArray.append([element]+array)
				else:
					pass
	return ReturnArray

	

if __name__ == '__main__':
	nums=[1,2,2]
	output=permute(nums)
	print(output)