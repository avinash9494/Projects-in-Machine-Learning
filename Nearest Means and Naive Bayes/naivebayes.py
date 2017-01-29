import sys
DEBUG = 1
#reading labels file
datafile = sys.argv[1]
f = open(datafile)
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
#printing labels file
#if(DEBUG):
#	for i in range(0,len(data),1):
#		print(data[i])
#reading train labels file
trainlabelfile = sys.argv[2]
f = open(trainlabelfile)
trainlabels = {}
n = []
n.append(0)
n.append(0)
l = f.readline()
while(l!=''):
	a = l.split()
	trainlabels[int(a[1])] = int(a[0])
	n[int(a[0])] += 1
	l = f.readline()
#printing length of classes and trainlabels
print("length of dict\n",len(trainlabels))
print("length of classes\n")
if(DEBUG) :
	for i in range(0,len(n),1):
		print(n[i])
#	print(trainlabels)
m0=[]
m1=[]
#calculation of means 
for i in range(0,cols,1):
	m0.append(0)
	m1.append(0)
for i in range(0,rows,1):
	if(trainlabels.get(i)!=None and trainlabels.get(i)==0):
		for j in range(0,cols,1):
			m0[j] += data[i][j]
	if(trainlabels.get(i)!=None and trainlabels.get(i)==1):
		for j in range(0,cols,1):
			m1[j] += data[i][j]
for j in range(0,cols,1):
	m0[j] = m0[j]/n[0]
	m1[j] = m1[j]/n[1]

#calculation of varience 
var0=[]
var1=[]
for i in range(0,cols,1):
	var0.append(0)
	var1.append(0)
for i in range(0,len(trainlabels),1):
	if(trainlabels.get(i)!=None and trainlabels.get(i)==0):
		for j in range(0,cols,1):
			var0[j]= var0[j]+((int(data[i][j])-m0[j])*(int(data[i][j])-m0[j]))
	if(trainlabels.get(i)!= None and trainlabels.get(i)==1):
		for j in range(0,cols,1):
			var1[j]+=((data[i][j]-m0[j])*(data[i][j]-m0[j]))
for j in range(0,cols,1):
	var0[j]=float(var0[j])/float(n[0])
	var1[j]=float(var1[j])/float(n[1])
print("variance\n")
for i in range(0,cols,1):
	print(var0[j],"\n",var1[j],"\n")
#classification and writing output prediction to labels.prediction file
print("means\n",m0,"\n",m1)
f0=open("naivebayeslabels.prediction","r+")
for i in range(0,rows,1):
	if(trainlabels.get(i)==None):
		d0=0
		for j in range(0,cols,1):
			d0+=(m0[j]-data[i][j])**2
			d0=float(d0)/float(var0[1])
		d1=0
		for j in range(0,cols,1):
			d1+=(m1[j]-data[i][j])**2
			d1=float(d1)/float(var1[1])
		if(d0<d1):
			f0.write("0 ")
			f0.write(str(i))
			f0.write("\n")
		else:
			f0.write("1 ")
			f0.write(str(i))
			f0.write("\n")
f0.close()

#computing efficiency

f = open("naivebayeslabels.prediction","r+")
predictedlabels=[]

l = f.readline()
while(l!=''):
	a = l.split()
	l2 = []
	for j in range(0,len(a),1):
        	l2.append(float(a[j]))
	predictedlabels.append(l2)
	l = f.readline()
print(len(predictedlabels))
print(len(data))
i=0
j=0
count=0
while(i<len(data)):
	if(predictedlabels[j][1]==data[i][1]):
		if(predictedlabels[j][0]==data[i][0]):
			count+=1
		j+=1
		if(j==len(predictedlabels)):
			break
	else:
		i+=1

print(count)
efficiency=(float(count)/float(len(predictedlabels)))*100
print("efficiency\n",efficiency)
