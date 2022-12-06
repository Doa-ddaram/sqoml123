import sys
sam = int(sys.stdin.readline())
rgb_dp = [[0 for i in range(3)] for j in range(sam + 1)]
for i in range(1, sam+1):
  rgb_dp[i] = list(map(int, input().split()))
for j in range(2, sam+1):
  rgb_dp[j][0] += min(rgb_dp[j-1][1], rgb_dp[j-1][2])
  rgb_dp[j][1] += min(rgb_dp[j-1][0], rgb_dp[j-1][2])
  rgb_dp[j][2] += min(rgb_dp[j-1][0], rgb_dp[j-1][1])
print(min(rgb_dp[sam]))