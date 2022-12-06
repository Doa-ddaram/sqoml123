import sys
sample_L = [[0 for i in range(101)] for j in range(101)]
total = 0 
for _ in range(4):
  y1,x1,y2,x2= map(int,input().split())
  for i in range(y1+1, y2+1):
    for j in range(x1+1, x2+1):
      sample_L[i][j] = 1
for i in range(1,101):
  for j in range(1,101):
    if sample_L[i][j]:
      total += 1
print(total)