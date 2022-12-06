import sys
from collections import deque
N = int(input())
sample_L = [list(map(int,input().split())) for i in range(N)]
final_L= []
def bfs(deep, x, y):
  total = 0
  rain_q = deque()
  if sample_L[x][y] > deep and check_L[x][y] == 0:
    rain_q.append([x,y])
    check_L[x][y] += 1
    total += 1
  while rain_q:
    t = rain_q.popleft()
    ne_x = [1,0,0,-1]
    ne_y = [0,1,-1,0]
    for i in range(4):
      nx = t[0] + ne_x[i]
      ny = t[1] + ne_y[i]
      if nx >= N or nx < 0 or ny >= N or ny < 0:
        continue
      if sample_L[nx][ny] > deep and check_L[nx][ny] == 0:
        rain_q.append([nx,ny])
        check_L[nx][ny] += 1
        total += 1
  if total:
    total_L.append(total)
for i in range(0,100):
  check_L = [[0 for k in range(N)] for t in range(N)]
  total_L = []
  for j in range(N):
    for r in range(N):
      bfs(i,j,r)
  final_L.append(len(total_L))
print(max(final_L))