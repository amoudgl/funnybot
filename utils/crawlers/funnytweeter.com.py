import requests
from bs4 import BeautifulSoup as bs
import unicodedata

filepath = '../../data/funnytweeter.csv'
f = open(filepath, 'w')
f.write("S.No.,Jokes\n")
totaljokes = 0
prefix = 'http://funnytweeter.com/page/'

for i in xrange(4568):
    url = prefix + str(i + 1) + '/'
    r = requests.get(url).text
    html = bs(r, 'html.parser')
    jokes = html.find_all('div', {'class': 'article_wrap'})
    for joke in jokes:
        # save only text tweets, ignore the ones with image
        if (joke.find_all('img', {'class': 'tweet_media'})[0]['src'] == ''):
            joke = joke.find_all('p')[0].get_text().split(":", 1)[1]
            joke = joke.replace('\n', " ").replace("\r", " ").replace("\t", " ").replace("    ", " ").replace("  ", " ").rstrip().strip().replace("  ", " ")
            joke = joke.replace(u"\u201c", '"').replace(u"\u201d", '"').replace(u"\u2019", "'").replace(u"\u2026", "...") 
            joke = unicodedata.normalize('NFKD', joke).encode('ascii','ignore')
            totaljokes += 1
            f.write(str(totaljokes)+ "," + joke + "\n")
    print ("Page %d processed, total number of jokes = %d" %(i + 1, totaljokes))

f.close()
