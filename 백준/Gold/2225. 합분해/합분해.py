import sys                                    #2225번
n, k = map(int,sys.stdin.readline().split())
add_dp = [[0 for j in range(n+2)] for i in range(k+1)]
add_dp[1] = [0] + [1] * (n + 1)
for i in range(2, k+1):
  for j in range(n+2):
    add_dp[i][j] = sum(add_dp[i-1][:j+1])
    add_dp[i][j] %= 1000000000
print(add_dp[k][n+1])