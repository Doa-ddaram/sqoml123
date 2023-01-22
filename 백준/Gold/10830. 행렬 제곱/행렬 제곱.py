import sys
input = sys.stdin.readline
def divpow(L,a,m):
  big = 1000
  s_L = [[0 for i in range(a)] for j in range(a)]
  temp_L = [[0 for i in range(a)] for j in range(a)]
  for i in range(a):
    temp_L[i][i] = 1
  while m > 0:
    if m % 2 != 0:
      # print(m)
      # print(L)
      for i in range(a):
        for j in range(a):
          temp = 0
          for r in range(a):
            temp += temp_L[i][r] * L[r][j]
            temp = temp % big
          s_L[i][j] = temp
      for i in range(a):
        for j in range(a):
          temp_L[i][j] = s_L[i][j]  
      # print(temp_L)
    for i in range(a):
      for j in range(a):
        temp = 0
        for r in range(a):
          temp += L[i][r] * L[r][j]
          temp = temp % big
        s_L[i][j] = temp
    for i in range(a):
      for j in range(a):
        L[i][j] = s_L[i][j]
    m = m // 2
  return temp_L
N,B = map(int,input().split())
lis = [list(map(int,input().split())) for i in range(N)]
t = divpow(lis,N,B)
for i in range(N):
  print(' '.join(map(str, t[i])))