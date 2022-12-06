import sys
from math import sqrt
M = int(sys.stdin.readline())
N = int(sys.stdin.readline())
total_L = [-1]
for i in range(M, N+1):
  if sqrt(i) == i / int(sqrt(i)):
    total_L.append(i)
if len(total_L) == 1:
  print(-1)
else:
  print(sum(total_L[1:]))
  print(total_L[1])