count = 0
import sys
a = int(sys.argv[1])
b = int(sys.argv[2])
for i in range (a,b+1):
 stroka = str(i)
 while len(stroka) < 6:
  stroka = '0' + stroka
 spisok = list (stroka)
 for element in range(6):
  spisok[element] = int(spisok[element])
 if sum (spisok[0:3]) == sum (spisok[3:6]):
   count = count+1  
print count 


"""
import sys
a1 = int(sys.argv[1])
a2 = int(sys.argv[2])
i_str = ''
counter = 0
for i in range(a1, a2+1):
    i_str = str(i)
    zeros_to_add = 6 - len(i_str)
    i_str = zeros_to_add * '0' + i_str
    if (int(i_str[0]) + int(i_str[1]) + int(i_str[2])) == (int(i_str[3]) + int(i_str[4]) + int(i_str[5])):
     counter = counter + 1      
print counter