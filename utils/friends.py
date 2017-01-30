from bs4 import BeautifulSoup as bs
import urllib

# extract webpage containing links to all seasons
r = urllib.urlopen('http://www.livesinabox.com/friends/scripts.shtml').read()
soup = bs(r)

# extract all seasons 
season = soup.find_all("ul")
prefix = "http://www.livesinabox.com/friends/"
filename = "friends.txt"
filepath = "../data/" + filename
f = open(filepath, 'a')
# for each season
for i in xrange(len(season)):

	# extract links to episodes
	a_tags = season[i].find_all('a')
	links = [link['href'] for link in a_tags]

	# visit page for each episode and save text
	for link in links:
		url = prefix + link
		html = urllib.urlopen(url).read()
		s = bs(html, 'html.parser')
		for script in s(["script", "style"]):
			script.extract() 
		text = s.get_text()
		lines = (line.strip() for line in text.splitlines())
		chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
		text = '\n'.join(chunk for chunk in chunks if chunk)
		f.write(text.encode('utf8'))
		f.write((u"\n").encode('utf8'))
	print ("Finished writing Season %d to file %s" %(i + 1, filepath))
