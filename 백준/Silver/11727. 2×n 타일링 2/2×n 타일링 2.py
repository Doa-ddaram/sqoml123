import sys
n = int(sys.stdin.readline())
L = [0] * 1001

L[1] = 1
for i in range(2, n + 1):
  if i % 2 == 0:
    L[i] = L[i-1] * 2 + 1
  else:
    L[i] = L[i-1] * 2 - 1
print(L[n] % 10007)