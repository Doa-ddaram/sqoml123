import sys
for _ in range(int(input())):
  k = int(sys.stdin.readline())
  n = int(sys.stdin.readline())
  dp = [[0 for j in range(n)] for i in range(k + 1)]
  dp[0] = list(range(1,n+1))
  for i in range(1, k+1):
    for j in range(0, n):
      dp[i][j] = sum(dp[i-1][:j+1])
  print(dp[k][n-1])