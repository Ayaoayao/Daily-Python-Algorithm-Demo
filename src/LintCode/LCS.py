def longestCommonSubstring(A, B):
    # write your code here
    if not A or not B:
        return 0
    output=[]
    for i in range(len(A)):
        indexA=i
        indexB=0
        flag=0
        start=[]
        while (indexB<len(B)):
            if A[indexA]==B[indexB]:
            	flag=1
                start.append(indexB)
                indexB+=1
            else:
                indexB+=1
        print(A[indexA],"This is start array",start)

        if flag==0:
            output.append(0)
        else:
            for j in start:
            	left=indexA
                length=0
                while(left<len(A) and j<len(B)):
                    if A[left]==B[j]:
                        left+=1
                        j+=1
                        length+=1
                    else:
                        break
                output.append(length)
            
    return max(output)   

if __name__ == '__main__':
    A="www.lintcode.com code"
    B="www.ninechapter.com code"
    result=longestCommonSubstring(A,B)
    print(result)
    print("finish")