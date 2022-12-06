import sys
L = list(map(int,sys.stdin.readline().split()))
total = 0
for i in range(len(L)):
  total += (L[i] ** 2)
print(total % 10)