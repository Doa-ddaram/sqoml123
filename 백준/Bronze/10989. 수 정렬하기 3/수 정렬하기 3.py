import sys
input= sys.stdin.readline
N = int(input())
count_L = [0] * 10001

for i in range(N):
  a = int(input())
  count_L[a] = count_L[a] + 1
for i in range(10001):
  if count_L[i] != 0:
    for _ in range(count_L[i]):
      print(i)