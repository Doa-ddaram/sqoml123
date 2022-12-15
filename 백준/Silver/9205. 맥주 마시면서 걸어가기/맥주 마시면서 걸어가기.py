import sys                                                                          #9205번 완성본
from collections import deque
input = sys.stdin.readline
for r in range(int(input())):
  con_L = []
  con = int(input())
  beer_x, beer_y  = map(int,input().split())
  for _ in range(con):
    con_L.append(list(map(int,input().split())))
  fes_x, fes_y = map(int,input().split())
  check_L = [0 for i in range(con+1)]
  def bfs(x,y):
    sum_q = deque()
    sum_q.append([x,y])
    while sum_q:
      t = sum_q.popleft()
      if abs(t[0] - fes_x) + abs(t[1] - fes_y) <= 1000:
        return 'happy'
      for i in range(con):
        if abs(t[0] - con_L[i][0]) + abs(t[1] - con_L[i][1])  <= 1000 and check_L[i] == False:
          sum_q.append(con_L[i])
          check_L[i] = True
    return 'sad'
  print(bfs(beer_x,beer_y))