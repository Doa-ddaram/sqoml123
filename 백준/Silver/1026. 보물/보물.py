import sys
N = int(input())
trea_aL = list(map(int,input().split()))
trea_bL = list(map(int,input().split()))
trea_aL.sort()
trea_bL.sort()
at = trea_aL.count(0)
bt = trea_bL.count(0)
S = 0
if at + bt <= N:
  if at:
    for _ in range(at):
      del trea_aL[0],trea_bL[-1]
  if bt:
    for _ in range(bt):
      del trea_bL[0],trea_aL[-1]
  for i in range(len(trea_bL)):
    S += (trea_aL[i] * trea_bL[len(trea_bL)-i-1])
print(S)