import sys
from math import sqrt
a, b = map(int, sys.stdin.readline().split())
for i in range(a, b+1):
  t = 0
  if i == 1:
    t = 1
  for j in range(2, int(sqrt(i))+1):
    if i % j == 0:
      t += 1
      break
  if t == 0:
    print(i)