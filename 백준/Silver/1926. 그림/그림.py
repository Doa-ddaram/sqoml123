from collections import deque
import sys
m, n = map(int,sys.stdin.readline().split())
sample_L = [list(map(int,sys.stdin.readline().split())) for i in range(m)]
total_L = []
def bfs(y,x):
  total = 0
  painting_q = deque()
  if sample_L[y][x] != 0:
    painting_q.append([y,x])
    total += 1
    sample_L[y][x] = 0
  while painting_q:
    temp = painting_q.popleft()
    ne_x = [1, 0, 0, -1]
    ne_y = [0, 1, -1, 0]
    for i in range(4):
      if temp[0] + ne_y[i] >= m or temp[0] + ne_y[i] < 0 or temp[1] + ne_x[i] >= n or temp[1] + ne_x[i] < 0:
        continue
      if sample_L[temp[0] + ne_y[i]][temp[1] + ne_x[i]] != 0:
        total += 1
        painting_q.append([temp[0] + ne_y[i],temp[1] + ne_x[i]])
        sample_L[temp[0] + ne_y[i]][temp[1] + ne_x[i]] = 0
  if total:
    total_L.append(total)
for i in range(m):
  for j in range(n):
    bfs(i,j)
if total_L:
  total_L.sort(reverse=True)
  print(len(total_L))
  print(total_L[0])
else:
  print(0)
  print(0)