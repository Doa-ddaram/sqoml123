import sys
N = int(input())
if N == 1:
  print(1)
elif N == 2:
  print(1)
else:
  L = [1] * 91
  for i in range(2, N):
    L[i] = L[i - 1] + L[i - 2]
  print(L[N-1])