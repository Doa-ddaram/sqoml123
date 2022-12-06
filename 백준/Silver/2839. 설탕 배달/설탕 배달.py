import sys
dp = [0, 0, 0, 1, -1, 1,2,-1,2,3,2,3,4]+ [1] * 4988
for i in range(13,5001):
  dp[i] = min(dp[i-3] + 1, dp[i-5] + 1)
n = int(sys.stdin.readline())
print(dp[n])