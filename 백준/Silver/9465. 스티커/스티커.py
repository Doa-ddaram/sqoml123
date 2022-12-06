import sys                                                          #9465번 미완성본
for _ in range(int(sys.stdin.readline())):
  n = int(sys.stdin.readline())
  if n == 1:
    fir = int(sys.stdin.readline())
    sec = int(sys.stdin.readline())
    print(max(fir,sec))
    continue
  fir_L = list(map(int,input().split()))
  sec_L = list(map(int,input().split()))
  stic_dp = [[0 for i in range(2)] for _ in range(n+1)]
  stic_dp[1] = [fir_L[0],sec_L[0]]
  stic_dp[2] = [fir_L[1] + sec_L[0], fir_L[0] + sec_L[1]]
  for i in range(3, n+1):
    stic_dp[i][0] = max(stic_dp[i-2][0],stic_dp[i-2][1], stic_dp[i-1][1]) + fir_L[i-1]
    stic_dp[i][1] = max(stic_dp[i-2][0],stic_dp[i-2][1],stic_dp[i-1][0]) + sec_L[i-1]
  print(max(stic_dp[n]))