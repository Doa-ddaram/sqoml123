import sys
n = int(input())
total = 1
count = int(input())
seat_dp = [1,1,2,3,5] + [0 for i in range(36)]
for i in range(5,41):
  seat_dp[i] = seat_dp[i-2] + seat_dp[i-1]
if count == 1:
  dot = int(input())
  total *= seat_dp[dot - 1] * seat_dp[n-dot]
elif count == 0:
  total = seat_dp[n]
else:
  dot = int(input())
  total *= seat_dp[dot - 1]
  while count != 1:
    dot_2 = int(input())
    total *= seat_dp[dot_2 - dot - 1]
    dot = dot_2
    count -= 1
  total *= seat_dp[n-dot_2]
print(total)