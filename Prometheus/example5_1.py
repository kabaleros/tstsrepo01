import sys
spisok = list (str (sys.argv[1]).lower().replace(" ",""))
antispisok = spisok [::-1]
if spisok == antispisok:
 print 'YES'
else:
 print 'NO'

""" import sys
s = sys.argv[1]
flag = True
s_cleaned = s.lower().replace(' ', '')
s_length = len(s_cleaned)
for i in range(s_length / 2):
    if s_cleaned[i] != s_cleaned[s_length-1-i]:
        flag = False
if flag:
    print 'YES'
else:
    print 'NO' """