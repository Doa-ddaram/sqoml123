import sys
from collections import deque
subin, sis = map(int,input().split())
check_L = [0 for i in range(100001)]
def bfs(x):
  sum_q = deque()
  sum_q.append(x)
  while sum_q:
    t = sum_q.popleft()
    time = check_L[t] + 1
    if t == sis:
      check_L[t] == time
      break
    if 0 <= t+1 <= 100000:
      if check_L[t+1] == 0 :
        sum_q.append(t+1)
        check_L[t+1] = time
    if 0 <= t-1 <= 100000:
      if check_L[t-1] == 0:
        sum_q.append(t-1)
        check_L[t-1] = time
    if 0 <= 2 * t <= 100000:
      if check_L[2 * t] == 0:
        sum_q.append(2 * t)
        check_L[2 * t] = time
  return check_L[sis]
print(bfs(subin))