
import sys
import pdb
import random
import math
from itertools import chain
DEBUG = 1 #to make sure everything is working

#read data
datafile = sys.argv[1]
f=open(datafile)
data_t = []
i=0

l = f.readline()
while (l!='') : 
	a = l.split()
	l2=[]
	for j in range (0,len(a),1) :
		l2.append(float(a[j]))
	data_t.append(l2)
	l=f.readline()
rows = len(data_t)
cols = len(data_t[0])
f.close()
if(DEBUG) :
	for i in range(0,len(data_t),1) :
		print(data_t[i])

###appending 1 to all rows
data=[[1 for row in range(0,cols+1)]for col in range(0,rows)]
for i in range(rows):
	for j in range(cols):
		data[i][j]=data_t[i][j]
for row in data:
	print(row)
rows=len(data)
cols=len(data[0])


##read labels###
labelfile = sys.argv[2]
f = open(labelfile)
# going to use dictionary
trainlabels = {}  # is hash table / dictionary
n=[]
n.append(0)
n.append(0)
l=f.readline()
while(l!=''):
    a = l.split()
    trainlabels[int( a[1])] = int (a[0])
    n[int (a[0])] +=1
    l=f.readline()

if(DEBUG) :
    for i in range(0,len(n),1) :
      print(n[i])
      print(trainlabels)
y=[]
for i in range(0,rows,1):
	y.append(0)
for i in range(0,rows,1):
	y[i]=float(trainlabels[i])

	print(y[i])
for i in range(0,rows,1):
	if y[i]==0:
		y[i]=-1
for i in range(0,rows,1):
	print(y[i])
w=[]
###initialising w
for i in range(0,cols,1):
	w.append(0)
for i in range(0,cols,1):
	w[i]=random.random()
	print("weights assigned :\n",w[i])
###calculating objective
temp=[[0 for row in range(0,cols)]for col in range(0,rows)]
len_temp=len(temp)
for i in range(0,rows,1):
	temp.append(0)
for i in range(0,cols,1):
	for j in range(0,rows,1):
		temp[j][i]=w[i]*data[j][i]

if(DEBUG) :
	for i in range(0,rows,1) :
		print(temp[i])
t2=0.0
for i in range(0,len_temp,1):
	t2+=sum(temp[i])
t1=0.0
t1=sum(y)
temp1=[[0 for row in range(0,cols)]for col in range(0,rows)]

len_temp1=len(temp1)
for i in range(0,rows,1):
	temp1.append(0)
for i in range(0,cols,1):
	for j in range(0,rows,1):
		temp1[j][i]=w[i]*data[j][i]*y[i]
	
t3=0.0
for i in range(0,len_temp1,1):
	t3+=sum(temp1[i])

obj=0
obj=(t1*t1)+(t2*t2)-(2*t3)
print("obj\n",obj)
prev_obj=float('inf')
delta=0.001
f=[[0 for row in range(0,cols)]for col in range(0,rows)]

temp_1=[[0 for row in range(0,cols)]for col in range(0,rows)]
while(prev_obj-obj>0.001):
	prev_obj=obj
	##calculation gradient
	k=0

	while(k<cols):
		for l in range(0,rows,1):
			for m in range(0,cols,1):	
				for i in range(0,cols,1):
					for j in range(0,rows,1):
						temp_1[j][i]=w[i]*data[j][i]*data[j][k]
				t_2=0.0
				for i in range(0,len(temp_1),1):
					t_2+=sum(temp_1[i])
				t_1=0.0
	
				temp_2=[]
				for i in range(0,rows,1):
					temp_2.append(0)
	
				for i in range(0,rows,1):
					temp_2[i]=data[i][k]*y[i]
				t_1=sum(temp_2)
				f[l][m]=-2*t_1+2*t_2
	k=k+1
	##updating weights
	for i in range(0,cols):
		for j in range(0,rows):
			w[j][i]-=delta*f[j][i]
	
	##updating objective
	t2=0.0
	
	temp=[[0 for row in range(0,cols)]for col in range(0,rows)]
	len_temp=len(temp)
	for i in range(0,rows,1):
		temp.append(0)
	for i in range(0,cols,1):
		for j in range(0,rows,1):
			temp[j][i]=w[i]*data[j][i]
	for i in range(0,len_temp,1):
		t2+=sum(temp[i])
	t1=0.0
	t1=sum(y)
	temp1=[[0 for row in range(0,cols)]for col in range(0,rows)]

	len_temp1=len(temp1)
	for i in range(0,rows,1):
		temp1.append(0)
	for i in range(0,cols,1):
		for j in range(0,rows,1):
			temp1[j][i]=w[i]*data[j][i]*y[i]
	
	t3=0.0
	for i in range(0,len_temp1,1):
		t3+=sum(temp1[i])
	obj=(t1*t1)+(t2*t2)-(2*t3)
	print("obj\n",obj)
for i in range(0,cols,1):
	print("final weights\n",w[i])
##calculation of distance from origin
w0=w[cols-1]
for i in range(0,cols-1,1):
	w_val+=w[i]*w[i]
dist=0.0
dist=abs(-w0/math.sqrt(w_val))
print("distance from origin:\n",dist)
		
