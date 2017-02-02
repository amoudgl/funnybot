from bs4 import BeautifulSoup as bs
import re
import unicodedata
import urllib

filepath = '../../data/funtweets.csv'
f = open(filepath, 'w')
f.write("S.No.,Jokes\n")
totaljokes = 0
prefix = 'http://funtweets.com/'

for i in xrange(3085):
    url = prefix + str(i + 1) + '/'
    r = urllib.urlopen(url).read()
    html = bs(r, 'html.parser')
    tweets = html.find_all('div', {'class': 'tweet-text'})
    for tw in tweets:
        joke = tw.get_text()
        username = tw.find('a').get_text()
        joke = re.sub(username, '', joke)
        joke = joke.replace('\n', " ").replace("\r", " ").replace("\t", " ").replace("    ", " ").replace("  ", " ").rstrip().strip().replace("  ", " ")
        joke = joke.replace(u"\u201c", '"').replace(u"\u201d", '"').replace(u"\u2019", "'").replace(u"\u2026", "...") 
        joke = unicodedata.normalize('NFKD', joke).encode('ascii','ignore')
        totaljokes += 1
        f.write(str(totaljokes)+ "," + joke + "\n")
    print ("Page %d processed, total number of jokes = %d" %(i + 1, totaljokes))

f.close()
