import sys
input = sys.stdin.readline
N, M = map(int,input().split())         #2740번
matrix_1_L = [list(map(int,input().split())) for j in range(N)]
M, K = map(int,input().split())
matrix_2_L = [list(map(int,input().split())) for j in range(M)]
matrix_3_L = [[0 for i in range(K)] for j in range(N)]
for i in range(N):
  for j in range(K):
    for r in range(M):
      matrix_3_L[i][j] += matrix_1_L[i][r] * matrix_2_L[r][j]
    print(matrix_3_L[i][j], end = ' ')
  print('')