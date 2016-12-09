import sys
a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

if ((b+c-a)<=0) or ((a+c-b)<=0) or ((a+b-c)<=0):
 print ('not triangle')
else:
 print ('triangle')
