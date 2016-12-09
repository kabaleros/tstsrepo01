fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list ()
for line in fh:
 line = line.rstrip()
 formlist = line.split()
 for item in formlist:
  if item not in lst: lst.append(item)
lst.sort()
print lst