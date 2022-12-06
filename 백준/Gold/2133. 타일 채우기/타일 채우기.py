import sys                                              #2133번 미완성본
N = int(sys.stdin.readline())
if N % 2:
  print(0)
else:
  tile_DP = [0 for i in range(N // 2 + 1)]
  tile_DP[0] = 1
  tile_DP[1] = 3
  for i in range(2, N // 2 + 1):
    tile_DP[i] = tile_DP[i-1] * 3
    for j in range(i-2,-1,-1):
      tile_DP[i] += (tile_DP[j] * 2)
  print(tile_DP[N // 2])