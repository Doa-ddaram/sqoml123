n = int(input())
def Fal(x):
    for i in range(len(x)//2):
        if x[i] != x[-1-i]:
            return 'No'
    return x
def p_n(x):
  from math import sqrt as s
  if x == 1:
    return False
  t = 0
  for j in range(2,int(s(x))+1):
    if x % j == 0:
      t = 1
      break
  if t == 0:
    return x
  return False
while True:
  if Fal(str(n)) != 'No':
    if p_n(n):
      print(n)
      break
  n += 1
  if n >= 98690:
    print(1003001)
    break