import os, io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
N , d =map(int,input().split())  #24268번 완성본(순열로 풀어낸 문제)  
def bi(x,y,m):
  while x <= y:
    t  = (x + y) // 2
    if sort_set_L[t] >= m:
      y = t - 1
    else:
      x = t + 1
  return x
from math import factorial as fact
from itertools import permutations
set_L = list(permutations(list(range(d)), d))
set_L = set_L[fact(d-1):]
sort_set_L = []
for i in range(len(set_L)):
  te = 0
  for j in range(d-1,-1,-1):
    te = te + ((d ** j) * set_L[i][d-1-j])
  sort_set_L.append(te)
sort_set_L = sorted(sort_set_L)
def bi(x,y,m):
  while x <= y:
    t  = (x + y) // 2
    if sort_set_L[t] >= m:
      y = t - 1
    else:
      x = t + 1
  return x
p = bi(0,len(sort_set_L)-1, N+1)
if p == len(sort_set_L):
  print(-1)
else:
  print(sort_set_L[p])