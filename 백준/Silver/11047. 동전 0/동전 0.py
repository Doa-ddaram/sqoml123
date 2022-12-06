import sys
N, K = map(int,input().split())
coin_L = []
total = 0
for _ in range(N):
  coin_L.append(int(input()))
for i in range(N-1,-1,-1):
  if K == 0:
    break
  if K % coin_L[i] == 0:
    total = total + K // coin_L[i]
    K = 0
    continue
  if K % coin_L[i] != K:
    total = total + (K // coin_L[i])
    K %= coin_L[i]
print(total)