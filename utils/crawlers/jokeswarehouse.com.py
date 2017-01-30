from bs4 import BeautifulSoup as bs
import unicodedata
import urllib
import csv
import sys

filepath = '../../data/jokeswarehouse.csv'
f = open(filepath, 'a')
f.write("S.No.,Jokes\n")

# extract urls
url = 'http://www.jokeswarehouse.com/cgi-bin/bydate.cgi'
r = urllib.urlopen(url).read()
html = bs(r, 'html.parser')
urls = html.find_all('a')
urls = [url['href'] for url in urls]
totaljokes = 0

for url in urls:
    r = urllib.urlopen(url).read()
    html = bs(r, 'html.parser')
    suburls = html.find_all('a')
    suburls = [suburl['href'] for suburl in suburls]
    for suburl in suburls:
        r = urllib.urlopen(suburl).read()
        html = bs(r, 'html.parser')
        joke = html.find('p').get_text()
        joke = joke.replace('\n', " ").replace("\r", " ").replace("\t", " ").replace("    ", " ").replace("  ", " ").rstrip().strip().replace("  ", " ")
        totaljokes += 1
        joke = unicodedata.normalize('NFKD', joke).encode('ascii','ignore')
        f.write(str(totaljokes)+ "," + joke + "\n")
    print ("total number of jokes processed = %d" %(totaljokes))

f.close()
