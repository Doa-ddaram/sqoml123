import sys
a = int(sys.stdin.readline())
x = str(sys.stdin.readline())
b = x.split()
for i in range(len(b)):
  b[i] = int(b[i])
b.sort()
print(b[0] * b[-1])