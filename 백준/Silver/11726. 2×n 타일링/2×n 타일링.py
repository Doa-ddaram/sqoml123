import sys
N = int(sys.stdin.readline())
if N == 1:
  print(1)
elif N == 2:
  print(2)
else:
  L = list(range(1, 1002))
  for i in range(2, N):
    L[i] = L[i - 1] + L[i - 2]
  print(L[N-1] % 10007)
