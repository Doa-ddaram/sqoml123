def divpow(L,m):  
  big = 1000000007
  s_L = [[0 for i in range(2)] for j in range(2)]
  temp_L = [[0 for i in range(2)] for j in range(2)]
  for i in range(2):
    temp_L[i][i] = 1
  while m > 0:
    if m % 2 != 0:
      for i in range(2):
        for j in range(2):
          temp = 0
          for r in range(2):
            temp += temp_L[i][r] * L[r][j]
            temp = temp % big
          s_L[i][j] = temp
      for i in range(2):
        for j in range(2):
          temp_L[i][j] = s_L[i][j]  
    for i in range(2):
      for j in range(2):
        temp = 0
        for r in range(2):
          temp += L[i][r] * L[r][j]
          temp = temp % big
        s_L[i][j] = temp
    for i in range(2):
      for j in range(2):
        L[i][j] = s_L[i][j]
    m = m // 2
  return temp_L
n = int(input())
t = divpow([[1,1],[1,0]],n)
print((t[0][0] * t[0][1]) % 1000000007)