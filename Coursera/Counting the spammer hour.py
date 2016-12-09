fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
mail = list()
for line in fh:
 line = line.rstrip()
 if not line.startswith('From') : continue
 if line.startswith('From:') : continue
 words = line.split()
 hour = words[5].split(':')
 #print hour[0]
 mail.append(hour[0])
counts = dict()
for item in mail:
 counts[item] = counts.get(item,0) + 1
lst = list()
for key,val in counts.items():
 lst.append((key,val))
lst.sort()
for key, val in lst:
 print key,val
