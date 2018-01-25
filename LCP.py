def LCP(strs):
	while len(strs)>1:
		left=strs[0]
		right=strs[1]
		print(left,right)
		count=min(len(left),len(right))
		temp=""
		for i in range(count):
			if left[i]==right[i]:
				temp+=left[i]
			else:
				break
		strs.remove(left)
		strs.remove(right)
		print(temp)
		strs.insert(0,temp)
	if len(strs)==1:
		return strs[0]

if __name__ == '__main__':
	test=["bchkjskjfaaaaasafa","bchkjskjafaaaaasafa","bchkjskafaasdlintcodeafa","bchkjska"]
	array=LCP(test)
	print(array)