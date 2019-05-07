import numpy as np 
import random
import time

for i in range(100):
	InputData=open('a.txt','a')
	Tempdata=[]
	a= random.randrange(0,1001)
	Tempdata.append(str(i))
	Tempdata.append(str(a))
	Data = ",".join(Tempdata)
	InputData.writelines(str(Data))
	InputData.write('\n')
	time.sleep(1)
InputData.close()