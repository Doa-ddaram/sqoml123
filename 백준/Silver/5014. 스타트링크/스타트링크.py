from collections import deque
import sys
F,S,G,U,D = map(int,sys.stdin.readline().split())
check_L = [0 for i in range(F+1)]
def bfs(x):
  startlink_q = deque()
  startlink_q.append(x)
  while startlink_q:
    t = startlink_q.popleft()
    if t == G:
      return check_L[t]
    if t <= F:
      if 1 <= t + U <= F and check_L[t + U] == 0 and t + U != S:
        startlink_q.append(t + U)
        time = check_L[t] + 1
        check_L[t + U] = time
      if 1 <= t - D <= F and check_L[t - D] == 0 and t - D != S:
        startlink_q.append(t - D)
        time = check_L[t] + 1
        check_L[t - D] = time
  return 'use the stairs'
print(bfs(S))