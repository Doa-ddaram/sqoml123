import sys
from math import factorial as fac
n = int(sys.stdin.readline())
t = fac(n)
count = 0
x = str(t)
for i in range(len(x)):
    if x[-1 * (i + 1)] != '0':
        break
    else:
      count += 1
print(count)