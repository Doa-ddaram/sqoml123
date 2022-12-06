import sys                                        #2096번 미완성본 (메모리 초과)
n = int(sys.stdin.readline())
down_dp = [0 for i in range(3)]
min_dp = [0 for i in range(3)]
temp_min_dp = [0 for i in range(3)]
max_dp = [0 for i in range(3)]
temp_max_dp = [0 for i in range(3)]
down_dp = list(map(int,sys.stdin.readline().split()))
a, b, c = down_dp[0], down_dp[1],down_dp[2]
temp_min_dp[0],temp_min_dp[1],temp_min_dp[2] = a, b, c
temp_max_dp[0],temp_max_dp[1],temp_max_dp[2] = a, b, c
for i in range(2,n+1):
  down_dp = list(map(int,sys.stdin.readline().split()))
  a, b, c = down_dp[0], down_dp[1],down_dp[2]
  min_dp[0] = (min(temp_min_dp[0], temp_min_dp[1]) + down_dp[0])
  min_dp[1] = (min(temp_min_dp[0], temp_min_dp[1], temp_min_dp[2]) + down_dp[1])
  min_dp[2] = (min(temp_min_dp[1], temp_min_dp[2]) + down_dp[2])
  max_dp[0] = (max(temp_max_dp[0], temp_max_dp[1]) + down_dp[0])
  max_dp[1] = (max(temp_max_dp[0], temp_max_dp[1], temp_max_dp[2]) + down_dp[1])
  max_dp[2] = (max(temp_max_dp[1], temp_max_dp[2]) + down_dp[2])
  for j in range(3):
    temp_min_dp[j] = min_dp[j]
    temp_max_dp[j] = max_dp[j]
if n == 1:
  print(max(down_dp),min(down_dp))
else:
  print(max(max_dp),min(min_dp))