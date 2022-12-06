import sys
n = int(sys.stdin.readline())
stair_L = [[0 for i in range(3)] for j in range(301)]
for i in range(n):
  t = int(sys.stdin.readline())
  stair_L[i+1][0],stair_L[i+1][1],stair_L[i+1][2] = t,t,t
stair_L[2][0] = stair_L[1][2] + stair_L[2][2]
stair_L[3][0] += stair_L[1][2]
stair_L[3][1] += stair_L[2][2]
for i in range(4, n+1):
  stair_L[i][0] += (max(stair_L[i-2]))
  stair_L[i][1] += (stair_L[i-1][2] + max(stair_L[i-3]))
print(max(stair_L[n]))