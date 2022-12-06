import sys                             #dp
n = int(sys.stdin.readline())
stair_dp = [[0 for j in range(10)] for i in range(n+1)]
stair_dp[1] = [0,1,1,1,1,1,1,1,1,1]
for i in range(1, n):
  for j in range(0, 10):
    if j == 0 :
      stair_dp[i+1][j+1] += stair_dp[i][j]
    elif j == 9:
      stair_dp[i+1][j-1] += stair_dp[i][j]
    else:
      stair_dp[i+1][j+1] += stair_dp[i][j]
      stair_dp[i+1][j-1] += stair_dp[i][j]
print(sum(stair_dp[n])% 1000000000)