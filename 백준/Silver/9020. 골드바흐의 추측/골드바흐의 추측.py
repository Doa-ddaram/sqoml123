from math import sqrt
import sys
for _ in range(int(sys.stdin.readline())):
  n = int(sys.stdin.readline())
  start = n // 2
  for i in range(start,0,-1):
    t = 1
    for j in range(2, int(sqrt(i))+1):
      if i % j == 0:
        t = 0
        break
    if t:
      for r in range(2,int(sqrt(n-i)) +1):
        if (n - i) % r == 0:
          t = 0
          break
      if t:
        print(i, n - i)
        break