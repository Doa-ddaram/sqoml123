import sys
k = int(input())
babba_dp = [0,0,1,2] + [0 for i in range(k-3)]
for i in range(4,k+1):
  babba_dp[i] = babba_dp[i-1] + babba_dp[i-2]
if k == 1:
  print(0, 1)
elif k == 2:
  print(1,1)
else:
  print(babba_dp[k-1],babba_dp[k])