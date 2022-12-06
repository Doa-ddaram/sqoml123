from collections import deque
N = int(input())
apart_L = [list(input()) for i in range(N)]
total_L = []
def bfs(x,y):
  total = 0
  apart_q = deque()
  if apart_L[x][y] != '0':
    apart_q.append([x,y])
    apart_L[x][y] = '0'
    total = 1
  else:
    return 0
  while apart_q:
    t = apart_q.popleft()
    dir_x = [1,0,0,-1]
    dir_y = [0,1,-1,0]
    for i in range(4):
      if t[0] + dir_x[i] < 0 or t[0] + dir_x[i] >= N or t[1] + dir_y[i] < 0 or t[1] + dir_y[i] >= N:
        continue
      if apart_L[t[0] + dir_x[i]][t[1] + dir_y[i]] != '0':
        apart_q.append([t[0] + dir_x[i],t[1] + dir_y[i]])
        apart_L[t[0] + dir_x[i]][t[1] + dir_y[i]] = '0'
        total += 1
  return total
for i in range(N):
  for j in range(N):
    t = bfs(i,j)
    if t > 0 :
      total_L.append(t)
print(len(total_L))
total_L.sort()
for i in range(len(total_L)):
  print(total_L[i])