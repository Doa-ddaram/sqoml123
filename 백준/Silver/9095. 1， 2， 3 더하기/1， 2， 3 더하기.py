import sys
L = [0] * 11
L[1], L[2], L[3] = 1, 2, 4
for _ in range(int(sys.stdin.readline())):
  n = int(sys.stdin.readline())
  if n > 3:
    for i in range(4, n + 1):
      L[i] = L[i-1] + L[i-2] + L[i-3]
  print(L[n])