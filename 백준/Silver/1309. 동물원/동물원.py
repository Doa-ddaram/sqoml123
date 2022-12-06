import sys
n = int(input())
zoo_dp = [0,3,7,17] + [0 for i in range(n-3)]
for i in range(4,n+1):
  zoo_dp[i] = (zoo_dp[i-1] * 2 + zoo_dp[i-2]) % 9901
print(zoo_dp[n])