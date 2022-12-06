import sys
from math import sqrt
n = int(sys.stdin.readline())
x = str(sys.stdin.readline())
L = x.split()
count = 0
for i in range(n):
  L[i] = int(L[i])
for j in range(n):
  t = 0
  if L[j] > 3:
    for k in range(2,int(sqrt(L[j])) + 1):
      if L[j] % k == 0:
        t = 1
        break
  elif L[j] == 1:
    t = 1
  if t == 0:
    count += 1
print(count)