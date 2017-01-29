
import sys
import time
import numpy
from sklearn import svm
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
start = time.time()
file = open(sys.argv[1])
traindata = file.readline()
dataset1 = []
while traindata!='':
    x=traindata.split()
    t1 = []
    for j in range(len(x)):
       if x[j]:
           t1.append(int(x[j]))
    dataset1.append(t1)
    traindata = file.readline()
end = time.time()
dataset1=numpy.array(dataset1)

print len(dataset1)
print "Time : ",round(end-start,2)



start = time.time()
file = open(sys.argv[2])
traindata = file.readline()

truelabels = []
while traindata!='':
    x=traindata.split()

    truelabels.append(x[0])
    traindata = file.readline()

truelabels = numpy.array(truelabels).reshape(len(truelabels), 1)
end = time.time()


data_labels = numpy.append(dataset1,truelabels, axis=1)
numpy.random.shuffle(data_labels)
numpy.random.shuffle(data_labels)
numpy.random.shuffle(data_labels)
truelabels = numpy.reshape(data_labels[:, -1:], -1)
dataset1 = data_labels[:, :-1]

print dataset1.shape
print truelabels.shape

split90=len(dataset1)*.90
data90=dataset1[:7200]
data10=dataset1[7201:]
label90=truelabels[:7200]
label10=truelabels[7201:]

#data90 = data_labels[:, :-1]

print len(dataset1)
print len(truelabels)

print "Time : ",round(end-start,2)

x = LinearSVC()
y = LinearSVC()

new_d1= x.fit_transform(data90,label90)
new_d2 =y.fit_transform(new_d1,label90)

z= svm.SVC(kernel='linear')
z.fit(new_d2,label90)

d1=x.transform(data10)
d2=y.transform(d1)
print "Accuracy ",z.score(d2,label10)

fileopen = open(sys.argv[3])
dataread = fileopen.readline()
alldata = []
while dataread!='':
    xz=dataread.split()
    t1 = []
    for j in range(len(xz)):
       if xz[j]:
           t1.append(int(xz[j]))
    alldata.append(t1)
    dataread = fileopen.readline()

end = time.time()
alldata=numpy.array(alldata)
fileopen.close()
fileopen=open("/Users/Max/Desktop/Pro/outputlabels.txt","w")

for i,ab in enumerate(alldata):
    d1=x.transform(ab)
    d2=y.transform(d1)
    fileopen.write(z.predict(d2)+" "+i+"\n")

fileopen.close()

sys.exit(0)