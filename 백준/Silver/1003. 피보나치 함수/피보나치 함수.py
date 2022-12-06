L = [[1,0],[0,1]]

for i in range(2, 42):
  L.append([L[i-1][0]+L[i-2][0],L[i-1][1]+L[i-2][1]])
for _ in range(int(input())):
  n = int(input())
  print(L[n][0],L[n][1])