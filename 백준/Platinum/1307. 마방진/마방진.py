n = int(input())
t_L = [[0 for i in range(n)] for j in range(n)]

def odd(p,L):
  L[0][p // 2] = 1
  t = 2
  x,y = p-1,p // 2 + 1
  x1,y1 = p-1,p // 2 + 1
  while True:
    L[x][y] = t
    if t == p ** 2:
      break
    t += 1
    x1 = x - 1
    if x1 == -1:
      x1 = p-1
    y1 += 1
    if y1 == p:
      y1 = 0
    if L[x1][y1] != 0:
      x1 = x + 1
      if x1 == p:
        x1 = 0
      y1 = y
    x = x1
    y = y1
  return L

def four_mul(x,L):
  temp = x // 4
  count = 0
  for i in range(temp):
    for j in range(temp):
      # count += 1
      L[i][j] = x * i + j + 1
      L[i][3*temp+j] = x * i + 3*temp +j + 1
      L[temp+i][temp+j] = x * (temp+i) + temp +j + 1
      L[temp+i][2*temp+j] = x * (temp+i) + 2*temp +j + 1
      L[2*temp+i][temp+j] =x * (2*temp+i) + temp +j + 1
      L[2*temp+i][2*temp+j]=x * (2*temp+i) + 2*temp +j + 1
      L[3*temp+i][j] = x * (3*temp+i) + j + 1
      L[3*temp+i][3*temp+j]=x * (3*temp+i) + 3*temp +j + 1
  for i in range(n-1,-1,-1):
    for j in range(n-1,-1,-1):
      count+=1
      if L[i][j] == 0:
        L[i][j] = count
  return L

def Else(x,L):
  temp = x // 2
  t2 = temp ** 2
  s_L = [[0 for i in range(temp)] for j in range(temp)]
  k = odd(temp,s_L)
  for i in range(temp):
    for j in range(temp):
      L[i][j]= k[i][j]
      L[temp+i][j] = k[i][j] + t2 * 2
      L[i][temp+j] = k[i][j] + t2 * 3
      L[temp+i][temp+j] = k[i][j] + t2
  p = (x- 2) // 4
  L[p][p], L[p][p+temp]=L[p][p+temp],L[p][p]
  for i in range(p-1):
    for j in range(temp):
      L[x-1-i][j], L[x-1-i][temp+j] = L[x-1-i][temp+j],L[x-1-i][j]
  for i in range(p):
    for j in range(temp):
      if i == 0 and j == temp // 2:
        continue
      L[p+1+i][j],L[p+1+i][temp+j] = L[p+1+i][temp+j], L[p+1+i][j]
  return L
if n % 2:
    k = odd(n,t_L)
elif n % 4:
    k = Else(n,t_L)
else:
    k = four_mul(n,t_L)
for i in k:
    print(*i)