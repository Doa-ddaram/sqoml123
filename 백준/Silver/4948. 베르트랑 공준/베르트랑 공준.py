import sys
from math import sqrt
while True:
  n = int(sys.stdin.readline())
  if n == 0:
    break
  total = 0
  for i in range(n + 1,2 * n + 1):
    for j in range(2, int(sqrt(i))+2):
      if i % j == 0:
        break
    if j == int(sqrt(i)) + 1:
      total += 1
  print(total)