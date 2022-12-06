import sys
from math import sqrt
while True:
  n = int(sys.stdin.readline())
  a, b = 3, 0
  if n == 0:
    break
  while a + b != n:
    t = 0
    for j in range(2, int(sqrt(a))+1):
      if a % j == 0:
        t += 1
        break
    if t == 0:
      b = n - a
    for k in range(2, int(sqrt(b))+1):
      if b % k == 0:
        t += 1
        a += 2
        break
  print('%d = %d + %d' %(n, a, b))