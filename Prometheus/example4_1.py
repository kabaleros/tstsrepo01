tick = 1
result = 0
def text_prompt(msg):
 try:
  return raw_input(msg)
 except NameErrror:
  return input(msg)
n = int(text_prompt('input n:'))
if n < 0:
 print('n should be not less than zero')
else:
 for counter in range (n):
  tick = tick + result
  result = tick - result
 print result
 
