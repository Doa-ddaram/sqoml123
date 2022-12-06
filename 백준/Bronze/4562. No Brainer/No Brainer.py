import sys
for _ in range(int(sys.stdin.readline())):
  a, b = map(int, sys.stdin.readline().split())
  if a < b :
    print('NO BRAINS')
  else:
    print('MMM BRAINS')