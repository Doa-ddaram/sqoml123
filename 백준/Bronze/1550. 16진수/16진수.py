###ord('B') - 55 = 11
###ord('1') - 48 = 1

import sys
total = 0
t = sys.stdin.readline().strip()
for i in range(len(t)):
  n = ord(t[i])
  if 48 <= n <= 57 :
    n -= 48
  else:
    n -= 55
  total += ((16 ** (len(t) - (i + 1))) * n)
print(total)