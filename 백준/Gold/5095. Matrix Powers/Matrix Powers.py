import io,os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
def divpowmat(L,n,p,m):
  mod = p 
  s_L = [[0 for i in range(n)] for j in range(n)]
  temp_L = [[0 for i in range(n)] for j in range(n)]
  for i in range(n):
    temp_L[i][i] = 1
  while m > 0:
    if m % 2 != 0:
      for i in range(n):
        for j in range(n):
          temp = 0
          for r in range(n):
            temp += temp_L[i][r] * L[r][j]
            temp %= mod
          s_L[i][j] = temp
      for i in range(n):
        for j in range(n):
          temp_L[i][j] = s_L[i][j] 
    for i in range(n):
      for j in range(n):
        temp = 0
        for r in range(n):
          temp += L[i][r] * L[r][j]
          temp %= mod
        s_L[i][j] = temp
    for i in range(n):
      for j in range(n):
        L[i][j] = s_L[i][j]
    m = m // 2
  return temp_L
while True:
  a,b,c = map(int,input().split())
  if a == 0 and b == 0 and c == 0:
    break
  mat_L = [list(map(int,input().split())) for i in range(a)]
  t = divpowmat(mat_L,a,b,c)
  for i in t:
    i = list(map(str,i))
    print(' '.join(i).strip())
  print()