# Generates a text file from csv, removing serial numbers
import csv
import urllib
import zipfile
import os 

try: 
    filepath = '../data/shortjokes.csv'
    data_file = open(filepath)
except: 
    print ("Dataset not found in ../data/ directory!")
    print ("Downloading...")
    url = 'https://github.com/abhinavmoudgil95/short-jokes-dataset/raw/master/shortjokes.csv'
    urllib.urlretrieve (url, "../data/shortjokes.csv")
    print ("Successfully downloaded: ../data/shortjokes.csv")
    data_file = open('../data/shortjokes.csv')

reader = csv.reader(data_file)
next(reader, None)
f = open('../data/shortjokes.txt', 'w')
for row in reader: 
    f.write(row[1] + "\n\n")
f.close()
