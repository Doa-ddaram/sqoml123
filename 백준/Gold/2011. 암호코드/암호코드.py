code = list(map(int,list(input())))
n = len(code)
dp = [0 for i in range(n+1)]
dp[0],dp[1] = 1, 1
if code[0] == 0:
  print(0)
else:
  for i in range(2, n+1):
    if code[i-1] !=0:
      dp[i] += dp[i-1]
    check = code[i-2] * 10 + code[i-1]
    if check >= 10 and check <= 26:
      dp[i] += dp[i-2]
  print(dp[n]% 1000000)