import random

# read all datasets
d1 = open('../data/funjokes.csv').readlines()
d2 = open('../data/jokeswarehouse.csv').readlines()
d3 = open('../data/onelinefun.csv').readlines()
d4 = open('../data/thejokecafe.csv').readlines()
d5 = open('../data/joke-db.csv').readlines()

# remove headers 
header = d1[0]
d1 = d1[1:]
d2 = d2[1:]
d3 = d3[1:]
d4 = d4[1:]
d5 = d5[1:]
print("Size of dataset: %d" %(len(d1) + len(d2) + len(d3) + len(d4) + len(d5)))

# remove serial numbers from datasets
for i in xrange(len(d1)):
    d1[i] = d1[i].split(',', 1)[1]
for i in xrange(len(d2)):
    d2[i] = d2[i].split(',', 1)[1]
for i in xrange(len(d3)):
    d3[i] = d3[i].split(',', 1)[1]
for i in xrange(len(d4)):
    d4[i] = d4[i].split(',', 1)[1]
for i in xrange(len(d5)):
    d5[i] = d5[i].split(',', 1)[1]

# combine datasets and shuffle
data = []
data.extend(d1)
data.extend(d2)
data.extend(d3)
data.extend(d4)
data.extend(d5)
random.shuffle(data)
print("Size of dataset: %d" %(len(data)))

# write all jokes to file
f = open('../data/all-jokes.csv', 'a')
f.write(header)
count = 0
for joke in data:
    count += 1
    f.write(str(count) + "," + joke)
f.close()
