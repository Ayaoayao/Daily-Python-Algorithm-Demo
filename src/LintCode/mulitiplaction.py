a=[0,1]
b=[1,7,8,2,7,1,8]
output=[]
string=''
for x in range(len(a)):
	for y in range(len(b)):
		try:
			output[x+y]+=a[x]*b[y]
		except IndexError:
			output.append(a[x]*b[y])
		else:
			pass

for x in range(len(output),0,-1):
	if output[x-1]>=10:
		if x>=2:
			output[x-2]+=output[x-1]//10
			output[x-1]=output[x-1]%10
		else:
			output.insert(0,output[x-1]//10)
			output[x]=output[x]%10
print(output)
count=0
while(len(output)>1):
	print(count)
	if output[count]==0:
		output.remove(0)
	else:
		break
for x in output:
	string+=str(x)


print(output)
print(string)