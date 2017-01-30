# Generates a text file from csv, removing serial numbers
jokes = open('../data/all-jokes.csv').readlines()
f = open('../data/all-jokes.txt', 'a')
for i in xrange(1, len(jokes)):
    joke = jokes[i].split(',',1)[1]
    f.write(joke)
f.close()
