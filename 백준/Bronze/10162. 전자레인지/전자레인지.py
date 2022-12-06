import sys
A, B, C, k = 0, 0, 0, 0
t = int(sys.stdin.readline())
if t % 10 != 0:
  k = 1
if t // 300 > 0:
  A = t // 300
  t -= ((t // 300) * 300)
if t // 60 > 0 :
  B = t // 60
  t -= ((t // 60) * 60)
C = t // 10
if k == 1:
  print(-1)
else :
  print(A, B, C)