import sys
n = int(sys.stdin.readline())
L = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
M = list(map(int, sys.stdin.readline().split()))
L.sort()
for j in range(m):
  t = 0
  st, ed = 0, n - 1
  temp = (st + ed) // 2
  while st == ed or ed > st:
    if M[j] > L[temp]:
      st = temp + 1
      temp = (st + ed) // 2
    elif M[j] < L[temp]:
      ed = temp - 1
      temp = (st + ed) // 2
    else:
      M[j] = 1
      t += 1
      break
  if t == 0:
    M[j] = 0
print(' '.join(map(str, M)))