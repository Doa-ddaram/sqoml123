import sys
n, m = map(int,sys.stdin.readline().split())
matrix_1 = [[0 for i in range(m)] for i in range(n)]
matrix_2 = [[0 for i in range(m)] for i in range(n)]
for i in range(n):
  matrix_1[i] = list(map(int,sys.stdin.readline().split()))
for i in range(n):
  matrix_2[i] = list(map(int,sys.stdin.readline().split()))
total_L = [[0 for i in range(m)] for i in range(n)]
for i in range(n):
  for j in range(m):
    total_L[i][j] = matrix_1[i][j] + matrix_2[i][j]
for i in range(n):
  for j in range(m):
    print(total_L[i][j], end = ' ')
  print()