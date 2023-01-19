import os, io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
N = int(input())
F_L = [1] * 4000001
L = 10 ** 9 + 7
for i in range(1,4000000):
  F_L[i+1] = F_L[i] * (i+1) % L
def divpow(a,m):
  temp = 1
  while m > 0:
    if m % 2 != 0:
      temp = temp * a
      temp = temp % L
    a = a * a
    a = a % L
    m = m // 2
  return temp
for _ in range(N):
  n, k = map(int,input().split())
  k1 = F_L[n]
  k = F_L[k] * F_L[n-k] % L
  k = divpow(k,L-2)
  print(k1 * k % L)