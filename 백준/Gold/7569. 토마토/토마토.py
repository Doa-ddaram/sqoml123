import sys                                                  #7569번 미완성본(현재 방법으로 메모리 초과 뜰 가능성 높음)
from collections import deque
input = sys.stdin.readline
M,N,H = map(int,input().split())
sample_L = [[[0 for i in range(M)] for j in range(N)] for r in range(H)]
check_L = [[[0 for i in range(M)] for j in range(N)] for r in range(H)]
for i in range(H):
  for j in range(N):
    sample_L[i][j] = list(map(int,input().split()))
case_q = deque()
Max = 0
def bfs(L):
  global Max
  tomato_q = deque()
  for so in L:
    tomato_q.append(so)
  while tomato_q:
    t = tomato_q.popleft()
    total = check_L[t[0]][t[1]][t[2]] + 1
    ne_x = [0,0,-1,1,0,0]
    ne_y = [0,0,0,0,1,-1]
    ne_z = [1,-1,0,0,0,0]
    for i in range(6):
      nx,ny,nz = t[2] + ne_x[i], t[1] + ne_y[i], t[0] + ne_z[i]
      if nx >= M or nx < 0 or ny >= N or ny < 0 or nz >= H or nz < 0:
        continue
      if sample_L[nz][ny][nx] == 0:
        tomato_q.append([nz, ny, nx])
        check_L[nz][ny][nx] = total
        sample_L[nz][ny][nx] = 2
        if total > Max:
          Max = total
for i in range(H):
  for j in range(M):
    for r in range(N):
      if sample_L[i][r][j] == 1:
        case_q.append([i,r,j])
        sample_L[i][r][j] = 2
bfs(case_q)
fin = 1
for i in range(H):
  for j in range(N):
    for r in range(M):
      if sample_L[i][j][r] == 0:
        print(-1)
        fin = 0
        break
    if fin == 0:
      break
  if fin == 0:
    break
if fin:
  print(Max)