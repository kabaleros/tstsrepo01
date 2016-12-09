import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('span')
tagsum = 0
for tag in tags:
    	tagint = int (tag.contents[0])
	tagsum = tagsum + tagint
print tagsum