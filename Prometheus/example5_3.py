import sys
stroka = str (sys.argv[1])
while True:
 clear_stroka = stroka.replace("()","")
 if len(clear_stroka) != len(stroka):
  stroka = clear_stroka
  continue
 else:
  break
if len(stroka) == 0:
 print 'YES'
else:
 print 'NO'
 
"""
import sys
string = sys.argv[1]
count = 0
flag = True
for char in string:
    if char == '(':
        count = count + 1
    elif char == ')':
        count = count - 1
    if count < 0:
        flag = False
if flag and count == 0:
    print 'YES'
else:
    print 'NO'