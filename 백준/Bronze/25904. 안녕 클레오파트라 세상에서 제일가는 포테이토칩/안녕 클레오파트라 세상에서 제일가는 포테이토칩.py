import sys
N, start = map(int,sys.stdin.readline().split())
T_L = list(map(int,sys.stdin.readline().split()))
temp = 0
check = start - 1
for j in range(100):
  for i in range(N):
    check += 1
    if check > T_L[i]:
      temp = 1
      total = i + 1
      break
  if temp:
    break
print(total)