import sys                          #17466번 미완성본(모듈로의 시작)
input = sys.stdin.readline
n, p = map(int,input().split())
def modul(n,m):
  res = n
  if n == 1:
    return res
  for i in range(n-1,0,-1):
    temp = res % m
    res = temp * i
  return temp
print(modul(n,p))