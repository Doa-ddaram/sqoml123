import sys

n = int(sys.stdin.readline())
L = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
M = list(map(int,sys.stdin.readline().split()))
L.sort()
for i in range(m):
  t = 0
  st, ed = 0, n - 1
  temp = (st + ed) // 2
  while st <= ed:
    if M[i] < L[temp]:
      ed = temp - 1
      temp = (st + ed) // 2
    elif M[i] > L[temp]:
      st = temp + 1
      temp = (st + ed) // 2
    else:
      t += 1
      break
  M[i] = t
  print(M[i])