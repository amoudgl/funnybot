from bs4 import BeautifulSoup as bs
import unicodedata
import urllib
import csv
import sys

filepath = '../../data/onelinefun.csv'
f = open(filepath, 'a')
f.write("S.No.,Jokes\n")
totaljokes = 0
prefix = 'http://onelinefun.com/'

for i in xrange(295):
    url = prefix + str(i + 1) + '/'
    r = urllib.urlopen(url).read()
    html = bs(r, 'html.parser')
    x = html.find_all('div', {'class': 'oneliner'})  
    jokes = [joke.find('p').get_text() for joke in x]
    for joke in jokes:
        joke = joke.replace('\n', '').replace('\t', '').replace('\r', '')
        joke = unicodedata.normalize('NFKD', joke).encode('ascii','ignore')
        totaljokes += 1
        f.write(str(totaljokes)+ "," + joke + "\n")
    print ("Page %d processed, total number of jokes = %d" %(i + 1, totaljokes))
f.close()
