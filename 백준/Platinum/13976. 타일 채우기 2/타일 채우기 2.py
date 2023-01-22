def divpow(L,a,m):          #13976번
  big = 1000000007
  s_L = [[0 for i in range(a)] for j in range(a)]
  temp_L = [0 for j in range(a)]
  temp_L[0] = 11
  temp_L[1] = 3
  temp_L[2] = 1
  while m > 0:
    if m % 2 != 0:
      # print(m)
      # print(L)
      for i in range(a):
        for j in range(a):
          temp = 0
          for r in range(a):
            temp += temp_L[r] * L[i][r]
            temp = temp % big
          s_L[i][j] = temp
      for i in range(a):
        temp_L[i] = s_L[i][j]  
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
N = int(input())
if N % 2:
  print(0)
elif N == 2:
  print(3)
else:
  N = N // 2 - 2
  t = divpow([[4,-1,0],[1,0,0],[0,1,0]],3,N)
  print(t[0])