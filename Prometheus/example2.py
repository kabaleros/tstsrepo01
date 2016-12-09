import sys
x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])

a = (1-z)*'.'+z*'!'
b = (x-1)*'la-'+'la'
c = y*(' '+b)

print 'Everybody sing a song:'+c+a