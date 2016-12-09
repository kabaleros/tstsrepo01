tick = 1
result = 0
import sys
n = int(sys.argv[1])
for counter in range (n):
 tick = tick + result
 result = tick - result
print result
 
