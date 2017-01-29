import sys
import copy
import math


def average(x):
	assert len(x)>0
	return float(sum(x))/len(x)
def pearson_def(x,y):
	assert len(x)==len(y)
	n=len(x)
	assert n>0
	avg_x=average(x)
	avg_y=average(y)
	diffprod=0
	xdiff2=0
	ydiff2=0
	for idx in range(n):
		xdiff=x[idx]-avg_x
		ydiff=y[idx]-avg_y
		diffprod+=xdiff*ydiff
		xdiff2+=xdiff*xdiff
		ydiff2+=ydiff*ydiff


	if(ydiff2==0 or xdiff2==0):
		return 0
	else:
		return diffprod/math.sqrt(xdiff2*ydiff2)

#############
datafile=sys.argv[1]
f=open(datafile)
data=[]
l=f.readline()
count=0
while(l!=''):
	a=l.split()
	l2=[]
	for j in range(0,len(a),1):
		l2.append(float(a[j]))
	data.append(l2)
	l=f.readline()
rows=len(data)
cols=len(data[0])
f.close()
print(len(data))
#data_feature=[]
#for i in range(0,rows,1):
#	data_feature.append(0)
#data_feature=copy.deepcopy(data)
r=[[0 for row in range(0,len(data))]for col in range(0,len(data))]
for i in range(0,len(data),1):
	for j in range(0,len(data),1):
		r[i][j]=pearson_def(data[i],data[j])
print("co-relation coefficient\n")
print(r)
sum_r=[[0 for row in range(0,1)]for col in range(0,len(data))]
for i in range(0,len(sum_r),1):
	sum_r[i][0]=sum(r[i])
print(sum_r)
n=len(sum_r)

for i in range(0,len(sum_r),1):
	sum_r[i][0]=sum_r[i][0]/n
	if(sum_r[i][0]<0.5):	
		del data[i]
print("no of features\n");
print(len(data))
f0=open("feature","r+")
for i in range(0,len(data,1)):
	f0.write(str(data[i]))
	f0.write("\n")
f0.close()

		
