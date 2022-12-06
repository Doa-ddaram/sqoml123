import sys
from collections import deque
n = int(input())
sta, end = map(int,input().split())
node_n = int(input())
sample_L= [0 for i in range(node_n)]
for i in range(node_n):
  sample_L[i] = (list(map(int,input().split())))
check_L = [0 for i in range(n+1)]
def bfs(x):
  node_q = deque()
  node_q.append(x)
  while node_q:
    t = node_q.popleft()
    total = check_L[t] + 1
    for i in range(node_n):
      if sample_L[i][0] == t:
        node_q.append(sample_L[i][1])
        check_L[sample_L[i][1]] = total
        sample_L[i] = [0,0]
      elif sample_L[i][1] == t:
        node_q.append(sample_L[i][0])
        check_L[sample_L[i][0]] = total
        sample_L[i] = [0,0]
bfs(sta)
if check_L[end]:
  print(check_L[end])
else:
  print(-1)
