import sys
x = float(sys.argv[1])
m = float(sys.argv[2])
v = float(sys.argv[3])
import math

y=(1/(v*math.sqrt(2*math.pi)))*math.exp(-((x-m)**2)/(2*v**2))
print y