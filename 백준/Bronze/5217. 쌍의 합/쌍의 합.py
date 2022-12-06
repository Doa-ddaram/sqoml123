import sys
for _ in range(int(sys.stdin.readline())):
  n = int(sys.stdin.readline())
  L = []
  a, b = 1, n - 1
  while b > a:
    L.append('%d %d' %(a, b))
    a += 1
    b = n - a
  print('Pairs for %d:' %n, ', '.join(map(str, L)))