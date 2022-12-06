import sys                    #1904번
n = int(sys.stdin.readline())
zeon_dp = [0, 1, 2] + [0] * (n-2)
for i in range(3,len(zeon_dp)):
  zeon_dp[i] = zeon_dp[i-1] + zeon_dp[i-2]
  zeon_dp[i] %= 15746
print(zeon_dp[n])