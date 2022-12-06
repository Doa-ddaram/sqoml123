import sys
from math import ceil
n = int(sys.stdin.readline())
test_place = list(map(int,sys.stdin.readline().split()))
ma_re, sub_re = map(int,sys.stdin.readline().split())
total = n
for i in range(n):
  if test_place[i] - ma_re < 0:
    continue
  total += ceil((test_place[i] - ma_re) / sub_re)
print(total)