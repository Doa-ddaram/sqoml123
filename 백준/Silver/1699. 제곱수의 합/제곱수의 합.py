from math import sqrt                   #1699번 미완성본
import sys
N = int(sys.stdin.readline())
pow_dp = [0,1,2,3] + [0 for i in range(N-3)]
for i in range(4,N+1):
  some_L = []
  for j in range(1,int(sqrt(i))+1):
    t = int(i - j * j)
    some_L.append(pow_dp[t])
  pow_dp[i] = min(some_L)+1
print(pow_dp[N])