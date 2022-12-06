import sys
for _ in range(int(sys.stdin.readline())):
  L = list(map(int,sys.stdin.readline().split()))
  num = 0
  mean = (sum(L) - L[0]) / (len(L) - 1)
  for i in range(1,len(L)):
    if L[i] > mean:
      num += 1
  total = round(num / (len(L) - 1) * 100,3)
  print('%.3lf'%(total)+'%')