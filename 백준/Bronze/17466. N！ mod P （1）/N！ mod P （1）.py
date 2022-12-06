import sys                          #17466번 미완성본(모듈로의 시작)
input = sys.stdin.readline
n, p = map(int,input().split())
def modul(n,m):
  res = 1
  for i in range(n,0,-1):
    res = res * i
    res = res % p
  return res
print(modul(n,p))