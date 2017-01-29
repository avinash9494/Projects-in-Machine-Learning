




import sys
import time
import numpy as np
from sklearn import svm
from sklearn.svm import LinearSVC
from sklearn.feature_selection import SelectPercentile, chi2, SelectKBest
from sklearn.metrics import accuracy_score
start = time.time()
f = open("traindata")
data = f.readline()
dataset = []
while data!='':
    a=data.split()
    l2 = []
    for j in range(len(a)):
       if a[j]:
           l2.append(int(a[j]))
    dataset.append(l2)
    data = f.readline()
end = time.time()
dataset=np.array(dataset)

print len(dataset)
print "Time : ",round(end-start,2)



start = time.time()
f = open("trueclass.txt")
data = f.readline()

labels = []
while data!='':
    a=data.split()

    labels.append(int(a[0]))
    data = f.readline()

labels = np.array(labels).reshape(len(labels), 1)
end = time.time()


data_labels = np.append(dataset,labels, axis=1)
np.random.shuffle(data_labels)
np.random.shuffle(data_labels)
np.random.shuffle(data_labels)
labels = data_labels[:, -1:]
dataset = data_labels[:, :-1]
labels = np.array(labels).reshape(len(labels),1)

print dataset.shape
print labels.shape


ninetyperdata=dataset[:7200]
tenperdata=dataset[7200:]
ninetyperlabels=labels[:7200]
tenperlabels=labels[7200:]


print "Time : ",round(end-start,2)

a = SelectKBest(chi2,15)
b = LinearSVC()

new_d1= a.fit_transform(ninetyperdata,ninetyperlabels)
b.fit(new_d1,ninetyperlabels)

d1=a.transform(tenperdata)
print "Accuracy", b.score(d1,tenperlabels)


fileopen = open("testdata")
dataread = fileopen.readline()
alldata = []
while dataread!='':
    ac=dataread.split()
    l2 = []
    for j in range(len(ac)):
       if ac[j]:
           l2.append(int(ac[j]))
    alldata.append(l2)
    dataread = fileopen.readline()

end = time.time()
alldata=np.array(alldata)
fileopen.close()
fileopen=open("outputlabels.txt","w")

for i,xy in enumerate(alldata):
    d1=a.transform(xy)
    fileopen.write(str(b.predict(d1))+" "+str(i)+"\n")

fileopen.close()

sys.exit(0)
