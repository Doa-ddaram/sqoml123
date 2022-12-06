tri_dp = [0,1,1,1,2,2] + [0] * 95
for i in range(6,101):
  tri_dp[i] = tri_dp[i-1] + tri_dp[i-5]
for _ in range(int(input())):
  n = int(input())
  print(tri_dp[n])