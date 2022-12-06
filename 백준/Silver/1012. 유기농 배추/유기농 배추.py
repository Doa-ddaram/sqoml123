from collections import deque

def bfs(x,y):
  total = 0
  baechu_q = deque()
  if sample_L[x][y] == 1:  
    baechu_q.append([x,y])
    sample_L[x][y] = 0
    total += 1
  while baechu_q:
    t = baechu_q.popleft()
    ne_x = [1,0,0,-1]
    ne_y = [0,1,-1,0]
    for i in range(4):
      nx = t[0] + ne_x[i]
      ny = t[1] + ne_y[i]
      if nx >= N or nx < 0 or ny >= M or ny < 0:
        continue
      if sample_L[nx][ny] == 1:
        baechu_q.append([nx,ny])
        sample_L[nx][ny] = 0
        total += 1
  if total:
    total_L.append(total)

for _ in range(int(input())):
  total_L = []
  M,N,K = map(int,input().split())
  sample_L= [[0 for i in range(M)] for j in range(N)]
  for r in range(K):
    X, Y = map(int,input().split())
    sample_L[Y][X] = 1
  for i in range(N):
    for j in range(M):
      bfs(i,j)
  print(len(total_L))