from sys import argv
from array import array
import random
from math import copysign as sign
import pdb

##for computing dot product
def dot(a,b):
	res=float(0)
	for i in range(0,len(a)):
		res+=(a[i]*b[i])

	return res

##for computing alpha
def find_alpha(data,label):
	last_sign=1
	x=sorted([a*b for a,b in zip(data,label)])
	for i in x:
		if i==0:
			sign=-1
		else:
			sign=i/abs(i)
		if sign == -last_sign:
			alpha = x[i]
			break
	return alpha


#reading data
data_path = argv[1]
f=open(data_path)
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

label_path=argv[2]
####read labels in an array
label_file=open(label_path)
labels=[]
i=0
l=label_file.readline()
while(l!=''):
	a=l.split()
	l2=[]
	for j in range(0,len(a),1):
		l2.append(l2)
	labels.append(l2)
	l=data_file.readline()

y=[]
for i in range(0,rows,1):
	y.append(0)
for i in range(0,rows,1):
	y[i]=float(labels[i])

	print(y[i])
for i in range(0,rows,1):
	if y[i]==0:
		y[i]=-1
for i in range(0,rows,1):
	print(y[i])
####starting the coordinate descent
w=array('f')
d=array('f')

####initialising d,w to 0's
for i in range(0,cols):
	d[i]=0
	w[i]=0
####initialize w to a random plane
for i in range(0,cols):
	w[i]=random.random()

delta=float(0)
data_prim=array('f')
label_prim=array('i')
alpha=0
prev_error=0
error=10000000
stop_condition=100
temp_error=array('f')
while(stop_condition!=0 or error!=0):
	prev_error=error
	for j in range(0,cols):
		d[j]=1
		for i in range(0,rows):
			delta=dot(d,data[i])
			if(delta!=0):
				####create new data and append it to to data_prim and label_prim
				for l in range(0,cols):
					for k in range(0,rows):
					data_prim[k][l]=data[k][l]*y[k]
					data_prim[k][l]=data[k][l]*y[k]
					label_prim[k]=y[k]
		alpha=find_alpha(data_prim,label_prim)
		error=0
		####change w and compute error
		w[j]=w[j]+alpha*d[j]
		for l in range(0,rows):
			temp_error[l]=(y[l]-dot(w,data[l]))*(y[l]-dot(w,data[l]))
		error=sum(temp_error)

			

		if(error<prev_error):
			####update w
			w[j]=w[j]-alpha*d[j]

		d[j]=0
		del data_prim[:]
		del label_prim[:]
	stop_contdition-=1
print(w)
print(error)

				

