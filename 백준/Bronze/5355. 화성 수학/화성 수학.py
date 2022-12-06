import sys
n = int(sys.stdin.readline())
for i in range(0,n):
  L = list(input().split())
  k = float(L[0])
  for j in range(1,len(L)):
    if L[j] == '@':
      k *= 3
    elif L[j] == '#':
      k -= 7
    elif L[j] == '%':
      k += 5
  print('%.2lf' %k)