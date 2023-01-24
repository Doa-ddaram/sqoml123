import io,os
from collections import deque
N, M = map(int,input().split())
sample_L = [list(input()) for i in range(N)]
total_L = [[0 for i in range(M)] for j in range(N)]
def bfs(y,x):
  total = 0
  miro_queue = deque()
  if sample_L[y][x] != '0':
    miro_queue.append([y,x])
    total = 1
    total_L[y][x] = total
    sample_L[y][x] = '0'
  while miro_queue:
    temp = miro_queue.popleft()
    next_y = [0,1,0,-1]
    next_x = [1,0,-1,0]
    for i in range(4):
      if temp[0] + next_y[i] >= N or temp[1] + next_x[i] >= M or temp[0] + next_y[i] < 0 or temp[1] + next_x[i] < 0:
        continue
      if sample_L[temp[0]+next_y[i]][temp[1] + next_x[i]] != '0':
        miro_queue.append([temp[0]+next_y[i],temp[1]+next_x[i]])
        total_L[temp[0]+next_y[i]][temp[1]+next_x[i]] += (total_L[temp[0]][temp[1]] + 1)
        sample_L[temp[0]+next_y[i]][temp[1]+next_x[i]] = '0'
bfs(0,0)
print(total_L[N-1][M-1])