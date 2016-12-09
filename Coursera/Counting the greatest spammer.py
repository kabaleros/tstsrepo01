fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count = 0
mail = list()
for line in fh:
 line = line.rstrip()
 if not line.startswith('From') : continue
 if line.startswith('From:') : continue
 words = line.split()
 mail.append(words[1])
counts = dict()
for word in mail:
 counts[word] = counts.get(word,0) + 1
bigcount = None
bigword = None
for word,count in counts.items():
 if bigcount is None or count > bigcount:
  bigword = word
  bigcount = count
print bigword, bigcount