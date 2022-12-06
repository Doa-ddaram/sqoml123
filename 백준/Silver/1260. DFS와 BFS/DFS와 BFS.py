from collections import deque
import sys
n, m , v = map(int,sys.stdin.readline().split())
temp_L = [0 for i in range(n+1)]
total_L = [[] for i in range(n+1)]
for i in range(1, m+1):
  a, b = map(int,sys.stdin.readline().split())
  total_L[a].append(b)
  total_L[b].append(a)
# total_L = [[0],[2,3],[5,1],[4,1],[5,3],[4,2]]
def DFS(n):
  temp_L[n] = 1
  total_L[n].sort()
  print(n, end = ' ')
  for i in range(len(total_L[n])):
    t = total_L[n][i]
    if temp_L[t] == 0:
      DFS(t)
DFS(v)
print()
temp_L = [0 for i in range(n+1)]
# total_L = [[0],[2,3],[5,1],[4,1],[5,3],[4,2]]
def BFS(n):
  temp_L[n] = 1
  BFS_Q = deque()
  BFS_Q.append(n)
  while BFS_Q:
    t = BFS_Q.popleft()
    print(t, end = ' ')
    total_L[t].sort()
    for i in range(len(total_L[t])):
      temp = total_L[t][i]
      if temp_L[temp] == 0:
        BFS_Q.append(temp)
        temp_L[temp] = 1
BFS(v)