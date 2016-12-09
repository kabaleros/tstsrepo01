import urllib
import xml.etree.ElementTree as ET

serviceurl = 'http://python-data.dr-chuck.net/comments_225374.xml'
#serviceurl = 'http://python-data.dr-chuck.net/comments_42.xml'

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
 tree = ET.fromstring(data)
 for count in tree.iter('count'):
  i = i + 1
  sum = sum + int(count.text)
 print 'Count:', i 
 print 'Sum:', sum