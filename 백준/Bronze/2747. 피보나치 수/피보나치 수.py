import sys
n = int(sys.stdin.readline())
fibo_dp = [0 for i in range(n+1)]
if n >= 3:
  fibo_dp[1] = 1
  fibo_dp[2] = 1
  for i in range(3,n+1):
    fibo_dp[i] = fibo_dp[i-1] + fibo_dp[i-2]
  print(fibo_dp[n])
else:
  print(1)
