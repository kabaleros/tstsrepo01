result = ""
import sys
spisok = sys.argv[1:]
antispisok = spisok [::-1]
for element in antispisok:
 result = result+" "+element
print result.lstrip()

""" import sys
args = sys.argv[1:]
args.reverse()
result = args[0]
for item in args[1:]:
    result = result + ' ' + item

print result """