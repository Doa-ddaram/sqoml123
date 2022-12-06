import sys
input = sys.stdin.readline
L = 10 ** 9 + 7

def divpow(x):
  if x == 1:
    return 2
  temp = divpow(x//2)
  if x % 2:
    return (temp * temp * 2) % L
  else:
    return (temp * temp) % L
    
for _ in range(int(input())):
  n = int(input())
  if n == 1 or n == 2:
    print(1)
  else:
    print(divpow(n-2))