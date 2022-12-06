import sys
total = int(sys.stdin.readline())
ori_total = 0
for _ in range(int(sys.stdin.readline())):
  a,b = map(int, sys.stdin.readline().split())
  ori_total += (a * b)
if ori_total == total:
  print('Yes')
else:
  print('No')