import os
import sys
data = sys.argv[1]
labels = sys.argv[2]

content = open(data).read()
dataset = []
tmp = []

for x in content.split("\n"):
    cols = 0
    for y in x.split():
        if y:
            cols += 1
            tmp.append("%s:%s" % (cols, y))
    if tmp:
        dataset.append(tmp)
    tmp = []

print(len(dataset), len(dataset[0]))

content = open(labels).read()
labelset = {}

for x in content.split("\n"):
    data = x.split()
    if data:
        labelset[int(data[1])] = data[0]

## take the 90% of the data
set_90 = int(len(dataset) * .90)

# split the dataset from 0 to 90% in one array and remaining 10% in another
# array
dataset1 = dataset[1:set_90]
dataset2 = dataset[set_90:]

tmp_data = "tmp_ip_dataset.data"
tmp_classify_data = "remaining_dataset.data"

# write the 90% input data to temporary file
tmp_file = open(tmp_data, "w")
i = 0
for x in dataset1:
    tmp_file.write("%s " % labelset[i])
    i += 1
    tmp_file.write(" ".join([str(y) for y in x]))
    tmp_file.write("\n")
tmp_file.close()

# write the 10% input data to temporary file
tmp_file = open(tmp_classify_data, "w")
for x in dataset2:
    tmp_file.write("%s " % labelset[i])
    i += 1
    tmp_file.write(" ".join([str(y) for y in x]))
    tmp_file.write("\n")
tmp_file.close()

print( ">>Written to file")

# run the 90% data on svm_learn


print( os.popen("./svm_learn -c %s %s" % (100,tmp_data)).read())
# classify the 10% data on svm_classify

print( os.popen("./svm_classify %s svm_model" %tmp_classify_data))
####
preds = "trans_predictions"


# cross check the result predictions across the labels
content = open(preds).read()
match = 0
j = set_90
for x in content.split("\n"):
    if x:
        if x == labelset[j]:
            match += 1
        j += 1

print ("Matched ==>", match)
print ("Total   ==>", len(dataset) - set_90)

