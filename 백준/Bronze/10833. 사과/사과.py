import sys
total = 0
for i in range(int(sys.stdin.readline())):
  a, b = map(int, sys.stdin.readline().split())
  total += (b % a)
print(total)