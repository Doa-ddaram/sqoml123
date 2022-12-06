import sys
k1, k2 = 100, 100
for i in range(0, int(sys.stdin.readline())):
  a, b = map(int,sys.stdin.readline().split())
  if a > b:
    k2 -= a
  elif a < b:
    k1 -= b
print(k1)
print(k2)