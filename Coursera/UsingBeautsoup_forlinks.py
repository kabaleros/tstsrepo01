import urllib
import json
import ssl
from BeautifulSoup import *

url = raw_input('Enter - ')
print 'Retrieving', url
scontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
uh = urllib.urlopen(url, context=scontext)
data = uh.read()
soup = BeautifulSoup(data)
ecount = int(raw_input('Enter count:'))
epos = int(raw_input('Enter position:')) - 1


tags = soup('a')
etag = tags[epos].get('href', None)
print etag

count = 1
while count < ecount:
 url = etag
 print 'Retrieving', url
 scontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
 uh = urllib.urlopen(url, context=scontext)
 data = uh.read()
 soup = BeautifulSoup(data)
 tags = soup('a')
 etag = tags[epos].get('href', None)
 count = count + 1
print 'Last Url: ', etag



"""for tag in tags:
    #listtag = list (tag.get('href', None))
    strtag = str(tag.get('href', None))
	#print 'URL:',tag.get('href', None)
    print strtag
    #listtag = listtag + strtag
    #print listtag"""



"""
# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print tag.get('href', None)
for tag in tags:
    # Look at the parts of a tag
    print 'TAG:',tag
    print 'URL:',tag.get('href', None)
    print 'Contents:',tag.contents[0]
    print 'Attrs:',tag.attrs"""