from math import sqrt as s
i,a = map(int,input().split())
c = a - i + 1
sq_a = int(s(a))
def prime_number():
  L = []
  for i in range(2,sq_a+1):
    t = 0
    for j in range(2,int(s(i))+1):
      if i % j == 0:
        t = 1
        break
    if t == 0:
      L.append(i**2)
  return L
p_L = prime_number()
L = set()
for so in p_L:
  if i % so:
    j = (i // so) + 1 
  else:
    j = (i // so)
  while so * j <= a:
    L.add(so*j)
    j += 1
print(c - len(L))