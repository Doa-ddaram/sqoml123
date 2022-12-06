import sys
n, k = map(int, sys.stdin.readline().split())  #11051번 미완성본
jo_dp = [[0 for i in range(k+1)] for j in range(n+1)]
for i in range(n+1):
  jo_dp[i][0] = 1
for i in range(1, n + 1):
  for j in range(1, k + 1):
    jo_dp[i][j] = jo_dp[i-1][j-1] + jo_dp[i-1][j]
    jo_dp[i][j] %= 10007
print(jo_dp[n][k])