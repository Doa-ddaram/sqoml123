import sys
from math import sqrt
input = sys.stdin.readline
M = int(input())
N = int(input())
total = 0
for i in range(M,N+1):
  t = True
  for j in range(2,int(sqrt(i)+1)):
    if i % j == 0:
      t = False
      break
  if t:
    if i == 1:
      continue
    if total == 0 :
      Min = i
    total += i
if total:
  print(total)
  print(Min)
else:
  print(-1)