from bs4 import BeautifulSoup as bs
import unicodedata
import urllib
import csv
import sys

filepath = '../../data/joke-db.csv'
f = open(filepath, 'a')
f.write("S.No.,Jokes\n")
prefix = 'http://www.joke-db.com/c/all/clean/page:'
totaljokes = 0

for i in xrange(235):
    url = prefix + str(i + 1) + '/'
    r = urllib.urlopen(url).read()
    html = bs(r, 'html.parser')
    jokes = html.find_all('div', {'class': 'joke-box-upper'})
    jokes = [joke.get_text() for joke in jokes]
    for joke in jokes:
        joke = joke.replace('\n', " ").replace("\r", " ").replace("\t", " ").replace("    ", " ").replace("  ", " ").rstrip().strip().replace("  ", " ")
        joke = joke.replace(u"\u201c", '"').replace(u"\u201d", '"').replace(u"\u2019", "'").replace(u"\u2026", "...")
        joke = unicodedata.normalize('NFKD', joke).encode('ascii','ignore')
        totaljokes += 1
        f.write(str(totaljokes)+ "," + joke + "\n")
    print ("Page %d processed, total number of jokes = %d" %(i + 1, totaljokes))

f.close()
