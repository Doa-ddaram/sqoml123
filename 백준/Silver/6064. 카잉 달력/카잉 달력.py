import sys        
from math import gcd
for i in range(int(input())):
  m, n, a, b = map(int, input().split())
  A, B = a, b
  while True:
    if A == B:
      print(A)
      break
    if A > m * n // gcd(m, n):
      print(-1)
      break
    if A - b < 0:
      A += m
    if (A - b) % n == 0:
      print(A)
      break
    else:
      A += m