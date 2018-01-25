def searchMatrix( matrix, target):
	# write your code here
	if not matrix:
		return False
	row=len(matrix)
	col=len(matrix[0])
	flag=0
	if row==1:
		for i in range(col):
			if matrix[0]==target:
				flag=1

	else:			
		for i in range(row):
			print(matrix[i],matrix[i+1])
			if i<row-1:
				if target>=matrix[i][0] and target<matrix[i+1][0]:
					temp_col=i
					break
	    	else:
				if target>=matrix[row-1][0] and target <=matrix[row-1][col-1]:
					temp_col=row-1
				else:
					return False

		for j in range(col):
			if matrix[temp_col][j]==target:
				flag=1

		if flag==1:
			return True
		else:
			return False

if __name__ == '__main__':
	matrix=[[5]]
	target=2
	if searchMatrix(matrix,target):
		print("success")
	else:
		print("false")