import sys                    #11057번 (10844번과 흡사한 방법으로 하면 됨.) (2775번 참고)
n = int(sys.stdin.readline())
ascent_dp = [[0 for j in range(10)] for i in range(1001)]
ascent_dp[1] = [1,1,1,1,1,1,1,1,1,1]
ascent_dp[2] = [1,2,3,4,5,6,7,8,9,10]
for i in range(3, n+1):
  for j in range(10):
    ascent_dp[i][j] = sum(ascent_dp[i-1][:j+1])
print(sum(ascent_dp[n]) % 10007)
