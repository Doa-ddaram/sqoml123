import sys       #1010번 미완성본
for _ in range(int(sys.stdin.readline())):
  a, b = map(int, sys.stdin.readline().split())
  k = 1
  for i in range(a, 0, -1):
    k *= (b - a + i)
    k /= i
  print(round(k))