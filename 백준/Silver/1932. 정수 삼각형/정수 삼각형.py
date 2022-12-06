import sys
n = int(sys.stdin.readline())                    #1932번 미완성본
dp = [[0 for j in range(n)] for i in range(n)]
for i in range(n):
  a = list(map(int, sys.stdin.readline().split()))
  dp[i] = a
for i in range(1, n):
  for j in range(i+1):
    if j == 0:
      dp[i][j] += dp[i-1][j]
    elif j == i:
      dp[i][j] += dp[i-1][j-1]
    else:
      dp[i][j] += max(dp[i-1][j], dp[i-1][j-1])
print(max(dp[n-1]))