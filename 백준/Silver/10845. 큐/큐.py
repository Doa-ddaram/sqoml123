from collections import deque
import sys
base_q = deque()
for i in range(int(sys.stdin.readline())):
  t = sys.stdin.readline().rstrip()
  if t[0:2] == 'pu':
    base_q.append(int(t[5:]))
  elif t[0:2] == 'po':
    if len(base_q) == 0:
      print(-1)
      continue
    temp = base_q.popleft()
    print(temp)
  elif t[0:2] == 'si':
    print(len(base_q))
  elif t[0:2] == 'em':
    if len(base_q):
      print(0)
    else:
      print(1)
  elif t[0:2] == 'fr':
    if len(base_q):
      print(base_q[0])
    else:
      print(-1)
  else:
    if len(base_q):
      print(base_q[-1])
    else:
      print(-1)