import urllib
import json

serviceurl = 'http://python-data.dr-chuck.net/comments_225378.json'


while True:
 address = raw_input('Enter location: ')
 if len(address) < 1 : break
 url = serviceurl
 print 'Retrieving', url
 uh = urllib.urlopen(url)
 data = uh.read()
 print 'Retrieved',len(data),'characters'
 i = 0
 sum = 0
 info = json.loads(str(data))
 for item in info['comments']:
  sum = sum + item['count']
  i = i + 1
 print 'Count:', i 
 print 'Sum:', sum