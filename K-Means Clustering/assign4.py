import sys
import copy
import random
DEBUG=1
def calculation(data):
	#selection of random points as clusters
	rd=len(data[0])
	k=int(sys.argv[2])
	cluster=[]
	for i in range(0,k,1):
		cluster.append(0)
	cluster=random.sample(data,k)
	mean=cluster[:]
	rows=len(data)
	cols=len(data[0])
	data_ch=[item for item in data if item not in cluster]
	data_c=data_ch[:]
	data_copy1=data_ch[:]
	dist=[[0 for row in range(0,k)]for col in range(0,len(data_c))]
	r=-1
	c=0
	c1=0
	r1=0
	flag=1
	f=1
	for i in range(0,len(dist),1):
		r=r+1
		for j in range(0,len(dist[0]),1):
			f=1
			flag=1
			while(f==1):
				while(flag==1):
					dist[i][j]+=data_c[r][c]-cluster[j][c1]
					c=c+1
					if(c==len(data[0])):
						c=0
						flag=0
					c1=c1+1
					if(c1==len(cluster[0])):
						c1=0
						r1=r1+1
						f=0
	for i in range(0,len(dist),1):
		for j in range(0,len(dist[0]),1):
			dist[i][j]=dist[i][j]**2
	i=0
	j=0
	k=0
	flag=1
	
	#appending cluster number to data points
	rows=len(dist)
	cols=len(dist[0])
	for i in range(0,rows,1):
		m=dist[i][0]
		index=1
		for j in range(1,cols,1):
			if(dist[i][j]<m):
				m=dist[i][j]
				index=j+1
		data_c[i].append(index)
	j=len(data_c[0])
	k=1
	n=[]
	#counting no datapoints in each cluster
	for i in range(0,len(cluster),1):
		n.append(0)
	data_copy1=[item for item in data if item  not in cluster]
	while(k<=len(cluster)):
		i=-1
		while(i<len(data_c)):
			i=i+1
			while(i<len(data_c) and data_c[i][j-1]==k):
				for l in range(0,rd,1):
					mean[k-1][l]+=data_copy1[i][l]
				n[k-1]=n[k-1]+1
				i=i+1
		k=k+1
	for i in range(0,len(mean),1):
		for j in range(0,len(mean[0]),1):
			mean[i][j]=mean[i][j]/n[i]
	cluster=mean[:]
	print("\n")
	
	d_c=[[0 for row in range(0,len(data_c[0]))]for col in range(0,len(data_c))]
	j=0
	k=len(data_c[0])-1
	while(j<len(data_c[0])):
		for i in range(0,len(data_c),1):
			d_c[i][j]=data_c[i][k]
		j=j+1
		k=k-1
	for i in range(0,len(d_c),1):
		print(d_c[i])
#reading data file
datafile=sys.argv[1]
f=open(datafile)
data=[]
i=0
l=f.readline()
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
#printing data file
if(DEBUG):
	for i in range(0,len(data),1):
		print(data[i])
#copying data list to another list data_copy
data_copy=[]
for i in range(0,rows,1):
	data_copy.append(0)
data_copy=copy.deepcopy(data)
calculation(data)
			
