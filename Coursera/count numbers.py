import re
fname = raw_input ('Enter the file name:')
try:
    fhand = open (fname)
except:
    print 'File cannot be opened', fname
    exit
inp = fhand.read()
y =  re.findall('[0-9]+', inp)
for i in range (len(y)):
    y[i] = int(y[i])
print sum (y)