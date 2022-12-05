import sys
input = sys.stdin.readline
m, n , c = map(int,input().split())
def divpow(a,m):
  if m == 1:
    return a % c
  temp = divpow(a,m//2)
  if m % 2:
    return temp * temp * a % c
  else:
    return temp * temp % c
print(divpow(m,n))