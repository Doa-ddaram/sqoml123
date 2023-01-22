import sys
input = sys.stdin.readline
k1, k2 = 100, 100
n = int(input())
for i in range(n):
  a, b = map(int,input().split())
  if a > b:
    k2 -= a
  elif a < b:
    k1 -= b
print(k1)
print(k2)