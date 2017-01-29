import sys
DEBUG = 1
#reading and displaying the truelabels file
truelabel = sys.argv[1]
f = open(truelabel)
data = []
i = 0
l = f.readline()
while(l!=''):
	a = l.split()
	l2 = []
	for j in range(0,len(a),1):
        	l2.append(float(a[j]))
	data.append(l2)
	l = f.readline()
rows = len(data)
cols = len(data[0])
f.close()
print("truelabels file\n")
if(DEBUG):
	for i in range(0,len(data),1):
		print(data[i])

print("\n")
#reading and displaying the predicted labels file
predictedfile = sys.argv[2]
f1 = open(predictedfile)
data1 = []
i = 0
l1 = f1.readline()
while(l1!=''):
	a1 = l1.split()
	l2 = []
	for j in range(0,len(a1),1):
        	l2.append(float(a1[j]))
	data1.append(l2)
	l1 = f1.readline()
rows1 = len(data1)
cols1 = len(data1[0])
f1.close()
print("predicted labels file\n")
if(DEBUG):
	for i in range(0,len(data1),1):
        	print(data1[i])

print("\n")

#calculation part
TP = 0
TN = 0
FP = 0
FN = 0
BER = 0
Precision = 0
Recall = 0

for i in range(0,len(data),1):
	if(data[i][1]==data1[i][1]):
	
		if(data[i][0]==1 and data1[i][0]==1):
			TP+=1
			
		if(data[i][0]==1 and data1[i][0]==0):
			FP = FP + 1
			
		if(data[i][0]==0 and data1[i][0]==1):
			FN = FN + 1
			
		if(data[i][0]==0 and data1[i][0]==0):
			TN = TN + 1
			
		
print( TP,"TP\n",TN,"TN\n",FP,"FP\n",FN,"FN\n")		   

E=(FP+FN)/(TP+FP+FN+TN)
BER=((FP/(FP+TN))+(FN/(FN+TP)))/2
Precision = TP/(TP+FP)
Recall = TP/(TP+FN)
print( E,"E\n",BER,"BER\n",Precision,"Precision\n",Recall,"Recall\n")
